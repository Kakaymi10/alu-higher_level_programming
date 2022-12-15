#!/usr/bin/python3
"""Test cases for Base"""

import os
import unittest

from models.base import Base


class Test_Base(unittest.TestCase):
    """Test class for Base"""

    def test_basic(self):
        """Doc"""
        self.assertEqual(Base(), 1)
        self.assertEqual(Base(), 2)
        self.assertEqual(Base(89), 89)
