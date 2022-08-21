#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """defines unittests for max_integer([..])"""
    
    def test_number_list(self):
        """tests the function max_integer with number lists."""
        self.assertEqual(max_integer([1, 4, 5]), 5)
        self.assertEqual(max_integer([-4, -5]), -4)
        self.assertEqual(max_integer([12.34, 4.5, 12.4]), 12.4)
        self.assertEqual(max_integer([-4.2, -3.9 -5.1]), -4.2)
        self.assertEqual(max_integer([-4.2, -9 -5.1]), -4.2)
        
    def test_empty_list(self):
        """tests the function max_integer with empty list."""
        self.assertEqual(max_integer([]), None)
    
    def test_list_of_one_element(self):
        """tests the function max_integer with one element list."""
        self.assertEqual(max_integer([7]), 7)

    
    def test_strings(self):
        """tests the function max_integer with strings."""
        strings = ["youtube", "podcast", "vlog"]
        self.assertEqual(max_integer(strings), 'youtube')
        self.assertEqual(max_integer("string"), 't')

if __name__ == '__main__':
    unittest.main()
