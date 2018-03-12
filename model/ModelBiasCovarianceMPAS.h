/*
 * (C) Copyright 2017 UCAR
 * 
 * This software is licensed under the terms of the Apache Licence Version 2.0
 * which can be obtained at http://www.apache.org/licenses/LICENSE-2.0. 
 */

#ifndef MPAS_MODEL_MODELBIASCOVARIANCEMPAS_H_
#define MPAS_MODEL_MODELBIASCOVARIANCEMPAS_H_

#include <ostream>
#include <string>
#include <boost/noncopyable.hpp>

#include "eckit/config/LocalConfiguration.h"
#include "util/ObjectCounter.h"
#include "util/Printable.h"

namespace mpas {
  class ModelBiasMPAS;
  class ModelBiasIncrementMPAS;
  class GeometryMPAS;

// -----------------------------------------------------------------------------

class ModelBiasCovarianceMPAS : public util::Printable,
                                 private boost::noncopyable,
                                 private util::ObjectCounter<ModelBiasCovarianceMPAS> {
 public:
  static const std::string classname() {return "mpas::ModelBiasCovarianceMPAS";}

/// Constructor, destructor
  ModelBiasCovarianceMPAS(const eckit::Configuration & conf, const GeometryMPAS &): conf_(conf) {}
  ~ModelBiasCovarianceMPAS() {}

/// Linear algebra operators
  void linearize(const ModelBiasMPAS &, const GeometryMPAS &) {}
  void multiply(const ModelBiasIncrementMPAS &, ModelBiasIncrementMPAS) const {}
  void inverseMultiply(const ModelBiasIncrementMPAS &, ModelBiasIncrementMPAS) const {}
  void randomize(ModelBiasIncrementMPAS &) const {}

  const eckit::Configuration & config() const {return conf_;}

 private:
  void print(std::ostream & os) const {}
  const eckit::LocalConfiguration conf_;
};

// -----------------------------------------------------------------------------

}  // namespace mpas

#endif  // MPAS_MODEL_MODELBIASCOVARIANCEMPAS_H_
