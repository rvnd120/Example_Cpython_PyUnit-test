"""
This module is Test Suite for the python
python module fibonacci_py. Created this to
facilitate addition of new testing modules
in future to avoid multiple creation of suites.
This suite is a basic framework for Test Suite

"""

import unittest
import fibonacci_py

loader = unittest.TestLoader()
fibo_suite = unittest.TestSuite()

# New Test Modules can be included in below list to add it to #
# this Test Suite Framework #
for test in [fibonacci_py]:
    fibo_suite.addTests(loader.loadTestsFromModule(test))

#unittest.TextTestRunner(verbosity=2)
