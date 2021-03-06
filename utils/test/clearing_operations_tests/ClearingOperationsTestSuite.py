#------------------------------------------------------------------------------
# Copyright 2017 Esri
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#------------------------------------------------------------------------------

import unittest
import logging
import Configuration

from . import ClearingOperationsCreateGRGFromPointTestCase
from . import ClearingOperationsCreateGRGFromAreaTestCase
from . import ClearingOperationsNumberFeaturesTestCase
from . import CreateReferenceSystemGRGFromAreaTestCase

''' Test suite for all tools in the Clearing Operationss Tools toolbox '''

def getTestSuite():

    if Configuration.DEBUG == True:
        print("      ClearingOperationsTestSuite.getSuite")

    testSuite = unittest.TestSuite()

    ''' Add the Clearing Operations tests '''

    loader = unittest.TestLoader()

    #Clearing Operations
    testSuite.addTest(loader.loadTestsFromTestCase(ClearingOperationsCreateGRGFromAreaTestCase.ClearingOperationsCreateGRGFromAreaTestCase))
    testSuite.addTest(loader.loadTestsFromTestCase(ClearingOperationsNumberFeaturesTestCase.ClearingOperationsNumberFeaturesTestCase))
    testSuite.addTest(loader.loadTestsFromTestCase(ClearingOperationsCreateGRGFromPointTestCase.ClearingOperationsCreateGRGFromPointTestCase))

    #Gridded Reference Graphic
    testSuite.addTest(loader.loadTestsFromTestCase(CreateReferenceSystemGRGFromAreaTestCase.CreateReferenceSystemGRGFromAreaTestCase))

    return testSuite
