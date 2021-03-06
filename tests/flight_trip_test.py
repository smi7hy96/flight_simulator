import unittest
from app.flight_trip_class import *
from app.staff_class import *
from app.passenger_class import *
from app.airport_class import *
from app.plane_class import *


class FlightTripTest(unittest.TestCase):
    def setUp(self):
        plane_1 = Plane('Airbus A380', 250)
        airport_1 = Airport('Madrid')
        airport_2 = Airport('Gatwick', [plane_1])
        self.flight_trip_1 = FlightTrip(airport_2, airport_1, 2, plane_1)

    def test_get_origin(self):
        airport_3 = Airport('Heathrow')
        self.assertEqual(self.flight_trip_1.get_origin().get_name(), 'Gatwick')
        self.flight_trip_1.set_origin(airport_3)
        self.assertEqual(self.flight_trip_1.get_origin().get_name(), 'Heathrow')

    def test_get_destination(self):
        airport_4 = Airport('Barcelona')
        self.assertEqual(self.flight_trip_1.get_destination().get_name(), 'Madrid')
        self.flight_trip_1.set_destination(airport_4)
        self.assertEqual(self.flight_trip_1.get_destination().get_name(), 'Barcelona')

    def test_get_duration(self):
        self.assertEqual(self.flight_trip_1.get_duration(), 2)
        self.flight_trip_1.set_duration(2.5)
        self.assertEqual(self.flight_trip_1.get_duration(), 2.5)

    def test_get_plane(self):
        plane_2 = Plane('Boeing 767', 250)
        self.assertEqual(self.flight_trip_1.get_plane().get_name(), 'Airbus A380')
        self.flight_trip_1.set_plane(plane_2)
        self.assertEqual(self.flight_trip_1.get_plane().get_name(), 'Boeing 767')

    def test_get_cost(self):
        self.assertEqual(self.flight_trip_1.get_cost(), 120)
        self.flight_trip_1.set_cost(180)
        self.assertEqual(self.flight_trip_1.get_cost(), 180)

    def test_add_passenger(self):
        airport_1 = Airport('Madrid')
        staff_1 = Staff('ABC123', 'Susan', 1, airport_1.get_name())
        passenger_1 = Passenger('DEF456', 'Peter', '11112222LL')

        self.flight_trip_1.add_passenger_to_flight(staff_1)
        self.assertEqual(self.flight_trip_1.get_passenger_list()['staff'][0].get_name(), 'Susan')
        self.flight_trip_1.add_passenger_to_flight(passenger_1)
        self.assertEqual(self.flight_trip_1.get_passenger_list()['passengers'][0].get_name(), 'Peter')

    def test_if_flight_full(self):
        airport_1 = Airport('Madrid')
        staff_1 = Staff('ABC123', 'Susan', 1, airport_1.get_name())
        plane_2 = Plane('Airbus1', 0)
        pass_list = {'staff': [staff_1], 'passengers': []}
        self.flight_trip_1.set_plane(plane_2)
        self.assertEqual(self.flight_trip_1.add_passenger_to_flight(staff_1), 'flight full')
        self.assertEqual(self.flight_trip_1.set_passenger_list(pass_list), 'too many people in list')

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

    def test_if_flight_empty(self):
        airport_1 = Airport('Madrid')
        staff_1 = Staff('ABC123', 'Susan', 1, airport_1.get_name())
        plane_2 = Plane('Airbus1', 0)
        self.assertEqual(self.flight_trip_1.remove_passenger_from_flight(staff_1), 'flight already empty')

    def test_if_passenger_not_on_flight(self):
        airport_1 = Airport('Madrid')
        staff_1 = Staff('ABC123', 'Susan', 1, airport_1.get_name())
        passenger_1 = Passenger('DEF456', 'Peter', '11112222LL')
        self.flight_trip_1.add_passenger_to_flight(staff_1)
        self.assertEqual(self.flight_trip_1.remove_passenger_from_flight(passenger_1), 'passenger not on flight')

    def test_produce_list(self):
        passenger_1 = Passenger('DEF456', 'Peter', '11112222LL')
        self.flight_trip_1.add_passenger_to_flight(passenger_1)
        self.assertEqual(self.flight_trip_1.produce_list_of_passengers(), 'Peter : 11112222LL')

    def test_departure(self):
        self.assertEqual(self.flight_trip_1.get_origin().get_aircraft_list()[0].get_name(), 'Airbus A380')
        self.assertEqual(self.flight_trip_1.departure(), 'Plane has departed! Enjoy your flight!!')
        self.assertEqual(self.flight_trip_1.get_origin().get_aircraft_list(), [])

    def test_arrive(self):
        self.flight_trip_1.departure()
        self.assertEqual(self.flight_trip_1.arrive(), 'Your plane has safely landed, thank you for travelling!')
        self.assertEqual(self.flight_trip_1.get_destination().get_aircraft_list()[0].get_name(), 'Airbus A380')
