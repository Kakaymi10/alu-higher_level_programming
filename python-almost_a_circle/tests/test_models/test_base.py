#!/usr/bin/python3
"""
    Unittest for Base
"""

import unittest
from models import base
Base = base.Base



class TestBase(unittest.TestCase):
    """
        test for Base
    """
    def test_creation_id(self):
        """
            test if value of id has the good assignment
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base(-5)
        b6 = Base(6.3)
        b7 = Base()
        b8 = Base(None)

        self.assertEqual(Base(), 1)
        self.assertEqual(Base(), 2)
        self.assertEqual(Base(), 3)
        self.assertEqual(Base(12), 12)
        self.assertEqual(Base(18), 18)
        self.assertEqual(Base(6), 6)
        self.assertEqual(Base(), 4)
        self.assertEqual(Base(None), 5)

        
if __name__ == '__main__':
    unittest.main()
