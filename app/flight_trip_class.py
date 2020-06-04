from app.staff_class import *
from app.passenger_class import *


class FlightTrip:
    def __init__(self, origin, destination, duration, plane, passenger_list=None):
        self.__origin = origin
        self.__destination = destination
        self.__duration = duration
        self.__plane = plane
        if passenger_list is None:
            passenger_list = {'staff': [], 'passengers': []}
        self.__passenger_list = passenger_list

    def get_origin(self):
        return self.__origin

    def set_origin(self, origin):
        self.__origin = origin

    def get_destination(self):
        return self.__destination

    def set_destination(self, destination):
        self.__destination = destination

    def get_duration(self):
        return self.__duration

    def set_duration(self, duration):
        self.__duration = duration

    def get_plane(self):
        return self.__plane

    def set_plane(self, plane):
        self.__plane = plane

    def get_passenger_list(self):
        return self.__passenger_list

    def set_passenger_list(self, passenger_list):
        self.__passenger_list = passenger_list

    def add_passenger_to_flight(self, passenger):
        if isinstance(passenger, Staff):
            self.__passenger_list['staff'].append(passenger)
        if isinstance(passenger, Passenger):
            self.__passenger_list['passengers'].append(passenger)

    def remove_passenger_from_flight(self, passenger):
        if isinstance(passenger, Staff):
            self.__passenger_list['staff'].remove(passenger)
        if isinstance(passenger, Passenger):
            self.__passenger_list['passengers'].remove(passenger)

