import unittest
from app.airport_class import *


class AirportTest(unittest.TestCase):
    def setUp(self):
        self.airport_1 = Airport('Madrid')

    def test_get_name(self):
        self.assertEqual(self.airport_1.get_name(), 'Madrid')
        self.airport_1.set_name('Heathrow')
        self.assertEqual(self.airport_1.get_name(), 'Heathrow')

    def test_get_aircraft_list(self):
        self.assertEqual(self.airport_1.get_aircraft_list(), [])
        self.airport_1.set_aircraft_list(['airbus1', 'airbus2'])
        self.assertEqual(self.airport_1.get_aircraft_list(), ['airbus1', 'airbus2'])

    def test_add_aircraft_to_list(self):
        self.airport_1.add_aircraft_to_list('Airbus1')
        self.assertEqual(self.airport_1.get_aircraft_list(), ['Airbus1'])

    def test_remove_aircraft_to_list(self):
        self.airport_1.set_aircraft_list(['airbus1', 'small jet'])
        self.airport_1.remove_aircraft_from_list('airbus1')
        self.assertEqual(self.airport_1.get_aircraft_list(), ['small jet'])
