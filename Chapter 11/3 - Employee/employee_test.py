from difflib import unified_diff
import unittest


import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test for the module employee."""

    def setUp(self):
        """Make an employee for the test."""
        self.jax = Employee('jax', 'teller', 75000)

    def test_give_default_raise(self):
        """Test the default raise."""
        self.jax.give_raise()
        self.assertEqual(self.jax.salary, 80000)

    def test_give_custom_raise(self):
        """Test giving a custom raise"""
        self.jax.give_raise(15000)
        self.assertAlmostEqual(self.jax.salary, 90000)
        
if __name__ == '__main__':
    unittest.main()