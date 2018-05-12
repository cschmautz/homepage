"""
testsuite.py

Module for aggregating unit tests into a suite for execution.
"""

import unittest
import sys
import os

if __name__ == '__main__':
    sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '../../../'))

import src.test.forms_tc as forms_tc
import src.test.utils.commext_tc as commext_tc

def suite():
    """
    Function to aggregate a bunch of different testing suites.
    """
    suite1 = unittest.TestLoader().loadTestsFromModule(forms_tc)
    suite2 = unittest.TestLoader().loadTestsFromModule(commext_tc)

    all_tests = unittest.TestSuite([suite1, suite2])

    return all_tests


if __name__ == '__main__':
    unittest.TextTestRunner(stream=sys.stdout, verbosity=2).run(suite())
