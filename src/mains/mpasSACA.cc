/*
 * (C) Copyright 2023 UCAR.
 *
 * This software is licensed under the terms of the Apache Licence Version 2.0
 * which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
 */

#include <oops/runs/AddIncrement.h>
#include <oops/runs/Run.h>

#include "mpasjedi/Traits.h"

int main(int argc,  char ** argv) {
  oops::Run run(argc, argv);
  oops::AddIncrement<mpas::Traits> addincrement;
  return run.execute(addincrement);
}
