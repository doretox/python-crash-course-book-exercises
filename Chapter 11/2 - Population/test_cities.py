import unittest
from city_functions import get_city_name

class TestCityName(unittest.TestCase):
    """Test's for 'city_functions.py'."""

    def test_city_country(self):
        """Do cities like 'Boston, Massachusetts' work?"""
        formated_name = get_city_name('boston', 'massachusetts')
        self.assertEqual(formated_name, 'Boston, Massachusetts')

    def test_city_country_population(self):
        """Do cities like 'Dallas, Texas - 1331000' work?"""
        formated_name = get_city_name('dallas', 'texas', '1331000')
        self.assertEqual(formated_name, 'Dallas, Texas - 1331000')

unittest.main()