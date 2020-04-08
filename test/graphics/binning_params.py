from collections import defaultdict
from copy import deepcopy


# allSCIErrParams is a dictionary of lookup tabls for symmetric cloud impact (SCI)
# The structure of allSCIErrParams keys is as follows:
#allSCIErrParams[
#    ({int: MPAS forecast resoultion},{str: bias correction type})][
#    {str: instrument name}][({int: channel number},{str: SCI method})]
allSCIErrParams = {}

# Individual SCIErrParams dictionaries below are generated
# automatically when AGGREGATEFC_StatsComposite figures are
# created with plot_stats_timeseries.py

# More keys can be added as they become available

## 120 km 6-hr MPAS Forecast from MPAS-JEDI analysis 2018041500 to 2018051412
## /glade/scratch/wuyl/test2/pandac/test_120km/ben_FC
## VARIATIONAL BIAS CORRECTION
SCIErrParams = defaultdict(dict)
#EMPTY
allSCIErrParams[(120,'varbc')] = deepcopy(SCIErrParams)


## CONSTANT BIAS CORRECTION
SCIErrParams = defaultdict(dict)
SCIErrParams['abi_g16'][ (7, 'Okamoto') ]   =  {'X': [1, 29.37], 'ERR': [3.48, 18.7]}
SCIErrParams['abi_g16'][ (8, 'Okamoto') ]   =  {'X': [1, 12.54], 'ERR': [1.98, 16.04]}
SCIErrParams['abi_g16'][ (9, 'Okamoto') ]   =  {'X': [1, 15.15], 'ERR': [2.05, 18.2]}
SCIErrParams['abi_g16'][ (10, 'Okamoto') ]   =  {'X': [1, 17.18], 'ERR': [2.07, 19.14]}
SCIErrParams['abi_g16'][ (11, 'Okamoto') ]   =  {'X': [1, 25.68], 'ERR': [2.24, 26.2]}
SCIErrParams['abi_g16'][ (13, 'Okamoto') ]   =  {'X': [1, 28.04], 'ERR': [2.41, 28.7]}
SCIErrParams['abi_g16'][ (14, 'Okamoto') ]   =  {'X': [1, 28.0], 'ERR': [2.44, 29.02]}
SCIErrParams['abi_g16'][ (15, 'Okamoto') ]   =  {'X': [1, 27.13], 'ERR': [2.39, 28.69]}
SCIErrParams['abi_g16'][ (16, 'Okamoto') ]   =  {'X': [1, 23.71], 'ERR': [2.18, 24.68]}
#For UFO YAML config:
#  X0: [1, 1, 1, 1, 1, 1, 1, 1, 1]
#  X1: [29.37, 12.54, 15.15, 17.18, 25.68, 28.04, 28.0, 27.13, 23.71]
#  ERR0: [3.48, 1.98, 2.05, 2.07, 2.24, 2.41, 2.44, 2.39, 2.18]
#  ERR1: [18.7, 16.04, 18.2, 19.14, 26.2, 28.7, 29.02, 28.69, 24.68]
SCIErrParams['abi_g16'][ (7, 'ScaledOkamoto') ]   =  {'X': [0, 30.07], 'ERR': [4.31, 18.53]}
SCIErrParams['abi_g16'][ (8, 'ScaledOkamoto') ]   =  {'X': [0, 11.62], 'ERR': [2.34, 14.68]}
SCIErrParams['abi_g16'][ (9, 'ScaledOkamoto') ]   =  {'X': [0, 14.15], 'ERR': [2.36, 16.99]}
SCIErrParams['abi_g16'][ (10, 'ScaledOkamoto') ]   =  {'X': [0, 16.46], 'ERR': [2.07, 18.67]}
SCIErrParams['abi_g16'][ (11, 'ScaledOkamoto') ]   =  {'X': [0, 25.45], 'ERR': [2.79, 25.99]}
SCIErrParams['abi_g16'][ (13, 'ScaledOkamoto') ]   =  {'X': [0, 27.53], 'ERR': [3.11, 28.6]}
SCIErrParams['abi_g16'][ (14, 'ScaledOkamoto') ]   =  {'X': [0, 27.45], 'ERR': [3.28, 28.86]}
SCIErrParams['abi_g16'][ (15, 'ScaledOkamoto') ]   =  {'X': [0, 27.0], 'ERR': [3.1, 28.6]}
SCIErrParams['abi_g16'][ (16, 'ScaledOkamoto') ]   =  {'X': [0, 23.53], 'ERR': [2.22, 24.6]}
#For UFO YAML config:
#  X0: [0, 0, 0, 0, 0, 0, 0, 0, 0]
#  X1: [30.07, 11.62, 14.15, 16.46, 25.45, 27.53, 27.45, 27.0, 23.53]
#  ERR0: [4.31, 2.34, 2.36, 2.07, 2.79, 3.11, 3.28, 3.1, 2.22]
#  ERR1: [18.53, 14.68, 16.99, 18.67, 25.99, 28.6, 28.86, 28.6, 24.6]
allSCIErrParams[(120,'constant')] = deepcopy(SCIErrParams)


## NO BIAS CORRECTION
SCIErrParams = defaultdict(dict)
SCIErrParams['abi_g16'][ (7, 'Okamoto') ]   =  {'X': [1, 30.22], 'ERR': [3.42, 18.67]}
SCIErrParams['abi_g16'][ (8, 'Okamoto') ]   =  {'X': [1, 13.31], 'ERR': [1.9, 17.38]}
SCIErrParams['abi_g16'][ (9, 'Okamoto') ]   =  {'X': [1, 15.92], 'ERR': [1.83, 19.85]}
SCIErrParams['abi_g16'][ (10, 'Okamoto') ]   =  {'X': [1, 17.2], 'ERR': [2.04, 19.28]}
SCIErrParams['abi_g16'][ (11, 'Okamoto') ]   =  {'X': [1, 26.59], 'ERR': [2.07, 25.85]}
SCIErrParams['abi_g16'][ (13, 'Okamoto') ]   =  {'X': [1, 28.89], 'ERR': [2.28, 28.41]}
SCIErrParams['abi_g16'][ (14, 'Okamoto') ]   =  {'X': [1, 28.28], 'ERR': [2.35, 28.87]}
SCIErrParams['abi_g16'][ (15, 'Okamoto') ]   =  {'X': [1, 27.85], 'ERR': [2.39, 28.47]}
SCIErrParams['abi_g16'][ (16, 'Okamoto') ]   =  {'X': [1, 24.58], 'ERR': [1.85, 24.31]}
#For UFO YAML config:
#  X0: [1, 1, 1, 1, 1, 1, 1, 1, 1]
#  X1: [30.22, 13.31, 15.92, 17.2, 26.59, 28.89, 28.28, 27.85, 24.58]
#  ERR0: [3.42, 1.9, 1.83, 2.04, 2.07, 2.28, 2.35, 2.39, 1.85]
#  ERR1: [18.67, 17.38, 19.85, 19.28, 25.85, 28.41, 28.87, 28.47, 24.31]
SCIErrParams['abi_g16'][ (7, 'ScaledOkamoto') ]   =  {'X': [0, 30.98], 'ERR': [4.24, 18.51]}
SCIErrParams['abi_g16'][ (8, 'ScaledOkamoto') ]   =  {'X': [0, 11.81], 'ERR': [2.34, 15.74]}
SCIErrParams['abi_g16'][ (9, 'ScaledOkamoto') ]   =  {'X': [0, 14.49], 'ERR': [2.42, 18.42]}
SCIErrParams['abi_g16'][ (10, 'ScaledOkamoto') ]   =  {'X': [0, 16.42], 'ERR': [2.07, 18.74]}
SCIErrParams['abi_g16'][ (11, 'ScaledOkamoto') ]   =  {'X': [0, 26.34], 'ERR': [2.75, 25.65]}
SCIErrParams['abi_g16'][ (13, 'ScaledOkamoto') ]   =  {'X': [0, 28.33], 'ERR': [3.08, 28.31]}
SCIErrParams['abi_g16'][ (14, 'ScaledOkamoto') ]   =  {'X': [0, 27.7], 'ERR': [3.22, 28.7]}
SCIErrParams['abi_g16'][ (15, 'ScaledOkamoto') ]   =  {'X': [0, 26.85], 'ERR': [2.94, 28.41]}
SCIErrParams['abi_g16'][ (16, 'ScaledOkamoto') ]   =  {'X': [0, 24.34], 'ERR': [2.18, 24.18]}
#For UFO YAML config:
#  X0: [0, 0, 0, 0, 0, 0, 0, 0, 0]
#  X1: [30.98, 11.81, 14.49, 16.42, 26.34, 28.33, 27.7, 26.85, 24.34]
#  ERR0: [4.24, 2.34, 2.42, 2.07, 2.75, 3.08, 3.22, 2.94, 2.18]
#  ERR1: [18.51, 15.74, 18.42, 18.74, 25.65, 28.31, 28.7, 28.41, 24.18]
allSCIErrParams[(120,None)] = deepcopy(SCIErrParams)


## 30 km 6-hr MPAS Forecasts from GFSANA 2018041500 to 2018042200
## /glade/scratch/wuyl/test2/pandac/test_30km_cld/FC
## VARIATIONAL BIAS CORRECTION
SCIErrParams = defaultdict(dict)
#EMPTY
allSCIErrParams[(30,'varbc')] = deepcopy(SCIErrParams)


## CONSTANT BIAS CORRECTION
SCIErrParams = defaultdict(dict)
#EMPTY
allSCIErrParams[(30,'varbc')] = deepcopy(SCIErrParams)


## NO BIAS CORRECTION
SCIErrParams = defaultdict(dict)
SCIErrParams['abi_g16'][ (7, 'Okamoto') ]   =  {'X': [1.0, 30.05], 'ERR': [2.18, 28.22]}
SCIErrParams['abi_g16'][ (8, 'Okamoto') ]   =  {'X': [1.0, 29.09], 'ERR': [2.06, 27.64]}
SCIErrParams['abi_g16'][ (9, 'Okamoto') ]   =  {'X': [1.0, 24.19], 'ERR': [1.35, 22.93]}
SCIErrParams['abi_g16'][ (10, 'Okamoto') ]   =  {'X': [1.0, 32.35], 'ERR': [3.1, 21.59]}
SCIErrParams['abi_g16'][ (11, 'Okamoto') ]   =  {'X': [1.0, 11.59], 'ERR': [1.62, 14.68]}
SCIErrParams['abi_g16'][ (13, 'Okamoto') ]   =  {'X': [1.0, 15.35], 'ERR': [1.54, 17.25]}
SCIErrParams['abi_g16'][ (14, 'Okamoto') ]   =  {'X': [0.0, 21.21], 'ERR': [1.33, 17.77]}
SCIErrParams['abi_g16'][ (15, 'Okamoto') ]   =  {'X': [1.0, 28.32], 'ERR': [1.77, 25.72]}
SCIErrParams['abi_g16'][ (16, 'Okamoto') ]   =  {'X': [1.0, 29.77], 'ERR': [1.94, 27.92]}

SCIErrParams['abi_g16'][ (7, 'ScaledOkamoto') ]   =  {'X': [0.0, 29.88], 'ERR': [4.71, 26.16]}
SCIErrParams['abi_g16'][ (8, 'ScaledOkamoto') ]   =  {'X': [0.0, 29.5], 'ERR': [4.58, 25.65]}
SCIErrParams['abi_g16'][ (9, 'ScaledOkamoto') ]   =  {'X': [0.0, 25.89], 'ERR': [3.65, 21.35]}
SCIErrParams['abi_g16'][ (10, 'ScaledOkamoto') ]   =  {'X': [0.0, 34.01], 'ERR': [4.43, 21.59]}
SCIErrParams['abi_g16'][ (11, 'ScaledOkamoto') ]   =  {'X': [0.0, 11.52], 'ERR': [1.68, 13.42]}
SCIErrParams['abi_g16'][ (13, 'ScaledOkamoto') ]   =  {'X': [0.0, 15.97], 'ERR': [2.12, 16.01]}
SCIErrParams['abi_g16'][ (14, 'ScaledOkamoto') ]   =  {'X': [0.0, 22.32], 'ERR': [2.62, 17.68]}
SCIErrParams['abi_g16'][ (15, 'ScaledOkamoto') ]   =  {'X': [0.0, 30.89], 'ERR': [4.32, 24.42]}
SCIErrParams['abi_g16'][ (16, 'ScaledOkamoto') ]   =  {'X': [0.0, 30.02], 'ERR': [4.56, 25.96]}

#SCIErrParams['abi_g16'][ (7, 'ModHarnisch') ]   =  {'X': [0.0, 30.61], 'ERR': [2.83, 28.13]}
#SCIErrParams['abi_g16'][ (8, 'ModHarnisch') ]   =  {'X': [0.0, 29.45], 'ERR': [2.46, 27.5]}
#SCIErrParams['abi_g16'][ (9, 'ModHarnisch') ]   =  {'X': [1.0, 24.16], 'ERR': [1.22, 22.92]}
#SCIErrParams['abi_g16'][ (10, 'ModHarnisch') ]   =  {'X': [0.0, 33.15], 'ERR': [4.17, 21.59]}
#SCIErrParams['abi_g16'][ (11, 'ModHarnisch') ]   =  {'X': [0.0, 11.03], 'ERR': [1.46, 12.98]}
#SCIErrParams['abi_g16'][ (13, 'ModHarnisch') ]   =  {'X': [0.0, 14.47], 'ERR': [1.57, 15.88]}
#SCIErrParams['abi_g16'][ (14, 'ModHarnisch') ]   =  {'X': [0.0, 21.49], 'ERR': [1.79, 17.77]}
#SCIErrParams['abi_g16'][ (15, 'ModHarnisch') ]   =  {'X': [1.0, 28.29], 'ERR': [1.56, 25.72]}
#SCIErrParams['abi_g16'][ (16, 'ModHarnisch') ]   =  {'X': [1.0, 30.01], 'ERR': [1.8, 27.81]}

#SCIErrParams['abi_g16'][ (7, 'ScaledModHarnisch') ]   =  {'X': [0.0, 29.96], 'ERR': [4.79, 26.16]}
#SCIErrParams['abi_g16'][ (8, 'ScaledModHarnisch') ]   =  {'X': [0.0, 29.55], 'ERR': [4.64, 25.64]}
#SCIErrParams['abi_g16'][ (9, 'ScaledModHarnisch') ]   =  {'X': [0.0, 25.92], 'ERR': [3.68, 21.35]}
#SCIErrParams['abi_g16'][ (10, 'ScaledModHarnisch') ]   =  {'X': [0.0, 34.42], 'ERR': [4.79, 21.59]}
#SCIErrParams['abi_g16'][ (11, 'ScaledModHarnisch') ]   =  {'X': [0.0, 11.43], 'ERR': [1.87, 12.53]}
#SCIErrParams['abi_g16'][ (13, 'ScaledModHarnisch') ]   =  {'X': [0.0, 16.17], 'ERR': [2.24, 15.63]}
#SCIErrParams['abi_g16'][ (14, 'ScaledModHarnisch') ]   =  {'X': [0.0, 21.63], 'ERR': [2.63, 17.43]}
#SCIErrParams['abi_g16'][ (15, 'ScaledModHarnisch') ]   =  {'X': [0.0, 30.94], 'ERR': [4.39, 24.42]}
#SCIErrParams['abi_g16'][ (16, 'ScaledModHarnisch') ]   =  {'X': [0.0, 30.11], 'ERR': [4.64, 25.98]}
allSCIErrParams[(30,None)] = deepcopy(SCIErrParams)
