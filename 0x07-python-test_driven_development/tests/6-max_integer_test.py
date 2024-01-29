#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_positive_numbers(self):
        """Test max_integer with a list of positive numbers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test max_integer with a list of negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_numbers(self):
        """Test max_integer with a list of mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 0, 1]), 1)
        self.assertEqual(max_integer([-1, 0, 1, -2]), 1)

    def test_empty_list(self):
        """Test max_integer with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test max_integer with a list containing one element"""
        self.assertEqual(max_integer([5]), 5)

    def test_float_numbers(self):
        """Test max_integer with a list containing floating point numbers"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)
        self.assertEqual(max_integer([1.5, -2.5, 3.5]), 3.5)

    def test_strings(self):
        """Test max_integer with a list of strings"""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")

    def test_mixed_types(self):
        """Test max_integer with a list containing mixed types"""
        with self.assertRaises(TypeError):
            max_integer([1, "a", 3, "b"])

if __name__ == "__main__":
    unittest.main()
