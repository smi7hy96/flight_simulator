import unittest
from app.aircraft_class import *


class AircraftTest(unittest.TestCase):
    def setUp(self):
        self.aircraft_1 = Aircraft('Airbus A380', 200, 5, 5)

    def test_get_name(self):
        self.assertEqual(self.aircraft_1.get_name(), 'Airbus A380')
        self.aircraft_1.set_name('Boeing 767')
        self.assertEqual(self.aircraft_1.get_name(), 'Boeing 767')

    def test_get_capacity(self):
        self.assertEqual(self.aircraft_1.get_capacity(), 200)
        self.aircraft_1.set_capacity(250)
        self.assertEqual(self.aircraft_1.get_capacity(), 250)
