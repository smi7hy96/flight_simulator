import unittest
from app.flight_trip_class import *
from app.staff_class import *
from app.passenger_class import *
from app.airport_class import *


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
        airport_1 = Airport('Madrid')
        staff_1 = Staff('ABC123', 'Susan', 1, airport_1.get_name())
        passenger_1 = Passenger('DEF456', 'Peter', '11112222LL')

        self.flight_trip_1.add_passenger_to_flight(staff_1)
        self.assertEqual(self.flight_trip_1.get_passenger_list()['staff'][0].get_name(), 'Susan')
        self.flight_trip_1.add_passenger_to_flight(passenger_1)
        self.assertEqual(self.flight_trip_1.get_passenger_list()['passengers'][0].get_name(), 'Peter')

    def test_remove_passenger(self):
        airport_1 = Airport('Madrid')
        staff_1 = Staff('ABC123', 'Susan', 1, airport_1.get_name())
        passenger_1 = Passenger('DEF456', 'Peter', '11112222LL')

        self.flight_trip_1.set_passenger_list({'staff': [staff_1], 'passengers': [passenger_1]})
        self.flight_trip_1.remove_passenger_from_flight(passenger_1)
        self.assertEqual(self.flight_trip_1.get_passenger_list()['passengers'], [])
        self.assertEqual(self.flight_trip_1.get_passenger_list()['staff'][0].get_name(), 'Susan')
        self.flight_trip_1.remove_passenger_from_flight(staff_1)
        self.assertEqual(self.flight_trip_1.get_passenger_list()['staff'], [])
