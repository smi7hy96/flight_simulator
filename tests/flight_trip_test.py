import unittest
from app.flight_trip_class import *


class FlightTripTest(unittest.TestCase):
    def setUp(self):
        self.flight_trip_1 = FlightTrip('Gatwick', 'Madrid', 2, 'Airbus A380')

    def test_get_origin(self):
        self.assertEqual(self.flight_trip_1.get_origin(), 'Gatwick')
        self.flight_trip_1.set_origin('Heathrow')
        self.assertEqual(self.flight_trip_1.get_origin(), 'Heathrow')

    def test_get_destination(self):
        self.assertEqual(self.flight_trip_1.get_destination(), 'Madrid')
        self.flight_trip_1.set_destination('Barcelona')
        self.assertEqual(self.flight_trip_1.get_destination(), 'Barcelona')

    def test_get_duration(self):
        self.assertEqual(self.flight_trip_1.get_duration(), 2)
        self.flight_trip_1.set_duration(2.5)
        self.assertEqual(self.flight_trip_1.get_duration(), 2.5)

    def test_get_origin(self):
        self.assertEqual(self.flight_trip_1.get_origin(), 'Gatwick')
        self.flight_trip_1.set_origin('Heathrow')
        self.assertEqual(self.flight_trip_1.get_origin(), 'Heathrow')

    def test_get_plane(self):
        self.assertEqual(self.flight_trip_1.get_plane(), 'Airbus A380')
        self.flight_trip_1.set_plane('Boeing 767')
        self.assertEqual(self.flight_trip_1.get_plane(), 'Boeing 767')

    def test_add_passenger(self):
        self.flight_trip_1.add_passenger_to_flight('Roger')
        self.assertEqual(self.flight_trip_1.get_passenger_list(), ['Roger'])

    def test_remove_passenger(self):
        self.flight_trip_1.set_passenger_list(['Roger', 'Mary'])
        self.flight_trip_1.remove_passenger_from_flight('Roger')
        self.assertEqual(self.flight_trip_1.get_passenger_list(), ['Mary'])
