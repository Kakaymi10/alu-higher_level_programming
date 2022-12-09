#!/usr/bin/python3
"""Importi unittest for testing base file"""


import unittest
from models import base
Base = base.Base


"""impoerting Pep package for pep validation"""
import pep8


"""Classes for pep8 validation for models/base.py and tests/test_models/test_base.py"""
class TestPep8(unittest.TestCase):
    """Pep8 models/base.py & tests/test_models/test_base.py"""
    def test_pep8(self):
        """Pep8"""
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        files = ["models/base.py", "tests/test_models/test_base.py"]
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')
        

"""Test class for models/bae file"""
class TestBase(unittest.TestCase):

    """call set up at the beginning of test"""
    def setUp(self):
        print("SETUP called...")

    """call tear down at the end of test"""
    def tearDown(self):
        print("TEARDOWN called...")

    """Test functions for the 2nd task"""
    """Test attributes"""
    def test_id_given(self):
        """Test ids match when given"""
        self.assertTrue(Base(999), self.id == 999)
        self.assertTrue(Base(0), self.id == 0)
        self.assertTrue(Base(1), self.id == 1)
        self.assertTrue(Base(-80), self.id == -80)

    def test_id_not_given(self):
        """Test ids match incremented nb_objects when not given"""
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)
        


if __name__ == "__main__":
    unittest.main()
