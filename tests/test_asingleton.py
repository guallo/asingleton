import unittest
import doctest

import asingleton.asingleton


def load_tests(loader, standard_tests, pattern):
    standard_tests.addTests(doctest.DocTestSuite(asingleton.asingleton))
    return standard_tests
