#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest


max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittest for max_integer([..])."""

    def test_list_integer1(self):
        """Test for list of integers."""
        list_int1 = [1, 2, 3, 4]
        self.assertEqual(max_integer(list_int1), 4)

    def test_list_integer2(self):
        """Test for list of unordered integers."""
        list_int2 = [1, 2, 4, 3]
        self.assertEqual(max_integer(list_int2), 4)

    def test_list_integer3(self):
        """Test for list of one integer."""
        list_int3 = [4]
        self.assertEqual(max_integer(list_int3), 4)

    def test_list_empty(self):
        """Test for an empty list."""
        list_empty = []
        self.assertEqual(max_integer(list_empty), None)

    def test_list_floats(self):
        """Test for list of floats."""
        list_floats = [-1.2, 2.8, 3.6, 4.1]
        self.assertEqual(max_integer(list_floats), 4.1)

    def test_string(self):
        """Test for a string."""
        str1 = "Elias"
        self.assertEqual(max_integer(str1), 's')

    def test_string_empty(self):
        """Test for an empty string."""
        str2 = ""
        self.assertEqual(max_integer(str2), None)

    def test_list_strings(self):
        """Test for a list of strings."""
        list_string = ["Elias", "Dewa", "Ahmed"]
        self.assertEqual(max_integer(list_string), "Elias")
