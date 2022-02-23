from difflib import unified_diff
import unittest
from city_functions import get_city_name

class TestCityName(unittest.TestCase):
    """Test's for 'city_functions.py'."""

    def test_city_country(self):
        """Do cities like 'Boston, Massachusetts' work?"""
        formated_name = get_city_name('boston', 'massachusetts')
        self.assertEqual(formated_name, 'Boston, Massachusetts')

unittest.main()