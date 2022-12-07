#!/usr/bin/python3
"""Importi unittest for testing base file"""


import unittest
from models import base
Base = base.Base


"""impoerting Pep package for pep validation"""


import pep8


"""Classes for pep8 validation for models/base.py and tests/test_models/test_base.py"""


class Pep8Test(unittest.TestCase):
    def test_pep8(self):
        


"""Test class for models/bae file"""


class TestBase(unittest.TestCase):

    """call set up at the beginning of test"""
    def setUp(self):
        print("SETUP called...")

    """call tear down at the end of test"""
    def tearDown(self):
        print("TEARDOWN called...")

    """Test functions for the 2nd task"""
    def test_base_1_id(self):
        


if __name__ == "__main__":
    unittest.main()
