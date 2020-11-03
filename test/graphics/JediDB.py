#!/usr/bin/env python3

import config as conf
from copy import deepcopy
import glob
from JediDBArgs import \
  obsFKey, geoFKey, diagFKey, default_path, fPrefixes
import logging
from netCDF4 import Dataset
import numpy as np
import os
import plot_utils as pu
import var_utils as vu
import sys

_logger = logging.getLogger(__name__)

MAXINT32  = np.int32(1e9)
MAXFLOAT  = np.float32(1.e12)
MAXDOUBLE = np.float64(1.e12)

class JediDB:
    '''This class provides access to UFO feedback files.'''
    def __init__(self,data_path=default_path,fileExt='nc4'
        ,osKeySelect=[]
        ):
        # data_path: location of feedback files
        # fileExt: extention of feedback files
        # osKeySelect (optional): allows for the selection of particular osKey's

        if 'nc' in fileExt:
            self.initHandles = self.initHandlesNC
            self.varList     = self.varListNC
            self.readVars    = self.readVarsNC
        # elif 'odb' in fileExt:
        #     self.initHandles = self.initHandlesODB
        #     self.varList     = self.varListODB
        #     self.readVars    = self.readVarsODB
        else:
            _logger.error('unsupported file extension => '+fileExt)

        self.filePrefixes = {}
        for key, prefix in fPrefixes.items():
            self.filePrefixes[key] = prefix

        # catalog all relevant files
        allFiles = {}
        for fileType, prefix in self.filePrefixes.items():
            allFiles[fileType] = []
            for File in glob.glob(data_path+'/'+prefix+'*.'+fileExt):
                allFiles[fileType].append(File)

        # Group files by experiment-ObsSpace combination
        #  Must fit the format filePrefixes[fileType]+"_"+osKey+"_"+PE+"."+fileExt,
        #  where osKey includes strings associated with both the experiment and ObsSpaceName
        #  and where each group contains files from all PE's,
        #  which is the 4-digit processor rank [0000 to XXXX]
        #  examples:
        #   +  obsout_3dvar_sondes_0000.nc4, where
        # osKey = "3dvar_sondes"
        #
        #   +  obsout_3denvar_bumploc_amsua_n19_0000.nc4, where
        # osKey = "3denvar_bumploc_amsua_n19"
        #
        #   +  obsout_3dvar_bumpcov_bumploc_amsua_n19_0000.nc4, where
        # osKey = "3dvar_bumpcov_bumploc_amsua_n19"
        #
        #   +  obsout_abi_g16_0000.nc4, where
        # osKey = "abi_g16"

        self.Files = {}
        for fileType, files in allFiles.items():
            for fileName in files:
                # fileBase excludes the path
                fileBase = fileName.split("/")[-1]

                # osKey excludes everything outside the first/final '_'
                osKey =  '_'.join(fileBase.split("_")[1:][:-1])
                if osKey not in self.Files:
                    self.Files[osKey] = {}
                if fileType not in self.Files[osKey]:
                    self.Files[osKey][fileType] = []
                self.Files[osKey][fileType].append(fileName)

        # error checking
        self.nObsFiles = {}
        self.exists = {}
        self.loggers = {}
        for osKey, fileGroups in self.Files.items():
            self.loggers[osKey] = logging.getLogger(__name__+'.'+osKey)
            nObsFiles = len(fileGroups.get(obsFKey,[]))
            # force crash when there are no obsFKey files available for an osKey
            if nObsFiles < 1:
                self.loggers[osKey].error('''
                           There are no '''+obsFKey+'''
                           feedback files with prefix '''+self.filePrefixes[obsFKey]+'''
                           osKey = '''+osKey)
            self.nObsFiles[osKey] = nObsFiles
            self.exists[osKey] = {}
            self.exists[osKey][obsFKey] = True
            # force crash when # of non-obs files is > 1 but ~= # of obsFKey files
            for key, prefix in self.filePrefixes.items():
                if key == obsFKey: continue
                self.exists[osKey][key] = False
                nFiles = len(fileGroups.get(key,[]))
                if nFiles > 0 and nFiles < nObsFiles:
                    self.loggers[osKey].error('''
                               There are not enough '''+key+'''
                               feedback files with prefix '''+prefix+'''
                               #'''+obsFKey+' = '+str(nObsFiles)+'''
                               #'''+key+' = '+str(nFiles)+'''
                               osKey = '''+osKey)
                elif nFiles > 0:
                    self.exists[osKey][key] = True

        # eliminate osKeys that are designated to not be processed
        self.ObsSpaceName = {}
        self.ObsSpaceGroup = {}
        for osKey in list(self.Files.keys()):
            # determine ObsSpace from osKey string
            # and only process valid ObsSpaceNames
            expt_parts = osKey.split("_")
            nstr = len(expt_parts)
            ObsSpaceInfo = conf.nullDiagSpaceInfo
            for i in range(0,nstr):
                ObsSpaceName_ = '_'.join(expt_parts[i:nstr])
                ObsSpaceInfo_ = conf.DiagSpaceConfig.get( ObsSpaceName_,conf.nullDiagSpaceInfo)
                if ObsSpaceInfo_['process']:
                    ObsSpaceName = deepcopy(ObsSpaceName_)
                    ObsSpaceInfo = deepcopy(ObsSpaceInfo_)
            if ((len(osKeySelect)>0 and osKey not in osKeySelect) or
                not ObsSpaceInfo['process'] or
                ObsSpaceInfo.get('DiagSpaceGrp',conf.model_s) == conf.model_s):
                del self.Files[osKey]
            else:
                self.ObsSpaceName[osKey] = deepcopy(ObsSpaceName)
                self.ObsSpaceGroup[osKey] = deepcopy(ObsSpaceInfo['DiagSpaceGrp'])

        # sort remaining files by PE
        for osKey, fileGroups in self.Files.items():
            for fileType, files in fileGroups.items():
                PEs = []
                for fileName in files:
                    PE = ''.join(fileName.split("_")[-1].split(".")[0])
                    PEs.append(int(PE))
                indices = list(range(len(files)))
                indices.sort(key=PEs.__getitem__)
                self.Files[osKey][fileType] = \
                    list(map(files.__getitem__, indices))

        self.Handles = {}

    # TODO: add function that concatenates files together, then
    # TODO: replaces the original Files and/or Handles
    #
    # TODO: first step would be to check if concatenated version exists,
    # TODO: then only initialize a single Handle for combined file
    #
    # TODO: enable __init__ function to check for concatenated version
    # TODO: of osKey files


    def initHandlesNC(self,osKey):
    #initialize Handles for osKey
    # osKey (string) - experiment-ObsSpace key
        self.loggers[osKey].info('Initializing UFO file handles...')

        self.Handles[osKey] = {}
        for fileType in self.filePrefixes.keys():
            self.Handles[osKey][fileType] = []

        for fileType, files in self.Files[osKey].items():
            if len(files) == self.nObsFiles[osKey]:
                self.loggers[osKey].info(' fileType = '+fileType)
                for ii, File in enumerate(files):
                    self.Handles[osKey][fileType].append(
                        Dataset(File, 'r'))
                    self.Handles[osKey][fileType][ii].set_auto_mask(False)


    def destroyHandles(self,osKey):
    #destroys file handles for osKey
    # osKey (string) - experiment-ObsSpace key
        if osKey in self.Handles:
            del self.Handles[osKey]


    def varListNC(self,osKey,fileType,selectGrp):
    #return a list of variable names that fits the input parameters
    # osKey (string)     - experiment-ObsSpace key
    # selectGrp (string) - variable group name desired from self.Files
    # fileType (string)  - file type key for self.Files[osKey]

        # extract file handles
        fHandles = self.Handles[osKey].get(fileType,[])
        if len(fHandles) < 1:
            self.loggers[osKey].error('no files exist => '+fileType)

        # select departure variables with the suffix selectGrp
        #  from fHandles[0]
        allvarlist = fHandles[0].variables.keys()
        varlist = []
        if fileType == obsFKey:
            for vargrp in allvarlist:
                var, grp = vu.splitObsVarGrp(vargrp)
                if grp == selectGrp: varlist.append(var)
# NOT CURRENTLY USED
#        elif ((fileType == diagFKey and vu.diagGroup in selectGrp and self.exists[osKey][diagFKey]) or
#              (fileType == geoFKey and vu.geoGroup in selectGrp and self.exists[osKey][geoFKey])):
#            for vargrp in allvarlist:
#                var, grp = vu.splitObsVarGrp(vargrp)
#                varlist.append(var)
        else:
            self.loggers[osKey].error('varListNC not implemented for '+fileType)


        # sort varlist alphabetically or
        # by integer suffix for uniform dictName (e.g., channel number)
        indices = list(range(len(varlist)))
        dictName0, suf = vu.splitIntSuffix(varlist[0])
        intlist = []
        sortbyInt = True
        for var in varlist:
            dictName, suf = vu.splitIntSuffix(var)
            if not pu.isint(suf) or dictName != dictName0:
                sortbyInt = False
                break
            intlist.append(suf)

        if sortbyInt:
            indices.sort(key=[int(i) for i in intlist].__getitem__)
        else:
            indices.sort(key=varlist.__getitem__)
        varlist = list(map(varlist.__getitem__, indices))

        return varlist


    def readVarsNC(self,osKey,dbVars):
    # osKey (string)  - experiment-ObsSpace key
    # dbVars (string) - list of variables desired from self.Handles[osKey]

        self.loggers[osKey].info('Reading requested variables from UFO file(s)...')

        obsHandles  = self.Handles[osKey][obsFKey]
        diagHandles = self.Handles[osKey][diagFKey]
        geoHandles  = self.Handles[osKey][geoFKey]

        #TODO: enable multiple levels of ObsDiagnostics and GeoVaLs
        diagLev = 0
        geoLev  = 0

        # Construct output dictionary
        varsVals = {}
        for varGrp in pu.uniqueMembers(dbVars):
            # self.loggers[osKey].info(varGrp)
            varName, grpName = vu.splitObsVarGrp(varGrp)
            if varGrp in obsHandles[0].variables:
                #TODO: pre-allocate numpy array (np.empty(nlocs))
                #    determine nlocs during handle definitions by summing nlocs attribute from ncfiles
                varsVals[varGrp] = np.asarray([])
                dtype = obsHandles[0].variables[varGrp].datatype
                if 'byte' in dtype.name:
                    for h in obsHandles:
                        tmp = []
                        for bytelist in h.variables[varGrp][:]:
                            tmp.append(b''.join(bytelist).decode("utf-8"))

                        varsVals[varGrp] = np.append( varsVals[varGrp], tmp )
                else:
                    for h in obsHandles:
                        varsVals[varGrp] = np.append( varsVals[varGrp], h.variables[varGrp][:] )

                # convert pressure from Pa to hPa if needed (kludge)
                if (vu.obsVarPrs in varGrp and np.max(varsVals[varGrp]) > 10000.0):
                    varsVals[varGrp] = np.divide(varsVals[varGrp],100.0)

            elif vu.diagGroup in grpName and self.exists[osKey][diagFKey]:
                if varName in diagHandles[0].variables:
                    #TODO: pre-allocate numpy array (np.empty,ndiaglevs)
                    varsVals[varGrp] = np.asarray([])
                    for h in diagHandles:
                        varsVals[varGrp] = np.append( varsVals[varGrp],
                            np.transpose(np.asarray(h.variables[varName][:]))[diagLev][:] )
                    dtype = h.variables[varName].datatype

            elif vu.geoGroup in grpName and self.exists[osKey][geoFKey]:
                if varName in geoHandles[0].variables:
                    #TODO: pre-allocate numpy array (np.empty(nlocs,ngeolevs))
                    # ngeolevs=?ndiaglevs, often ngeolevs==1...handle cases
                    varsVals[varGrp] = np.asarray([])
                    for h in geoHandles:
                        varsVals[varGrp] = np.append( varsVals[varGrp],
                            np.transpose(np.asarray(h.variables[varName][:]))[geoLev][:] )
                    dtype = h.variables[varName].datatype

            else:
                self.loggers[osKey].error('varGrp not found => '+varGrp)

            if 'int32' in dtype.name:
                missing = np.greater(np.abs(varsVals[varGrp]), MAXINT32)
            elif 'float32' in dtype.name:
                missing = np.greater(np.abs(varsVals[varGrp]), MAXFLOAT)
            elif 'float64' in dtype.name:
                missing = np.greater(np.abs(varsVals[varGrp]), MAXDOUBLE)
            else:
                missing = np.full_like(varsVals[varGrp],False,dtype=bool)
            varsVals[varGrp][missing] = np.NaN

        return varsVals
