from app.staff_class import *
from app.passenger_class import *


class FlightTrip:
    def __init__(self, origin, destination, duration, plane, passenger_list=None, cost=0):
        self.__origin = origin
        self.__destination = destination
        self.__duration = duration
        self.__plane = plane
        cost = duration * 60
        self.__cost = cost
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

    def get_cost(self):
        return self.__cost

    def set_cost(self, cost):
        self.__cost = cost

    def get_passenger_list(self):
        return self.__passenger_list

    def get_revenue(self):
        num_of_passengers = len(self.get_passenger_list()['passengers'])
        return self.get_cost() * num_of_passengers

    def set_passenger_list(self, passenger_list):
        if self.count_people_in_flight(passenger_list['staff'], passenger_list['passengers']) < self.get_plane().get_capacity():
            self.__passenger_list = passenger_list
        else:
            return 'too many people in list'

    def add_passenger_to_flight(self, passenger):
        if self.count_people_in_flight(self.get_passenger_list()['staff'], self.get_passenger_list()['passengers']) < self.get_plane().get_capacity():
            if isinstance(passenger, Staff):
                self.__passenger_list['staff'].append(passenger)
            if isinstance(passenger, Passenger):
                self.__passenger_list['passengers'].append(passenger)
        else:
            return 'flight full'

    def remove_passenger_from_flight(self, passenger):
        if self.count_people_in_flight(self.get_passenger_list()['staff'], self.get_passenger_list()['passengers']) > 0:
            if isinstance(passenger, Staff):
                if self.__check_if_on_flight(passenger, self.__passenger_list['staff']):
                    self.__passenger_list['staff'].remove(passenger)
                else:
                    return 'passenger not on flight'
            if isinstance(passenger, Passenger):
                if self.__check_if_on_flight(passenger, self.__passenger_list['passengers']):
                    self.__passenger_list['passengers'].remove(passenger)
                else:
                    return 'passenger not on flight'
        else:
            return 'flight already empty'

    def __check_if_on_flight(self, passenger, the_list):
        for name in the_list:
            if passenger == name:
                return True
        return False

    def produce_list_of_passengers(self):
        names = self.__get_all_passenger_names()
        passport_nos = self.__get_all_passenger_passports()
        for x in range(len(names)):
            names[x] = names[x] + " : " + passport_nos[x]
        return '\n'.join(names)

    def __get_all_passenger_names(self):
        names_list = []
        for name in self.get_passenger_list()['passengers']:
            names_list.append(name.get_name())
        return names_list

    def __get_all_passenger_passports(self):
        passport_list = []
        for passport in self.get_passenger_list()['passengers']:
            passport_list.append(passport.get_passport_no())
        return passport_list

    def count_people_in_flight(self, all_staff, all_passengers):
        count_total = 0
        count_staff = 0
        count_passengers = 0
        for staff in all_staff:
            count_staff += 1
        for passenger in all_passengers:
            count_passengers += 1
        count_total = count_staff + count_passengers
        return count_total

    def departure(self):
        self.get_origin().remove_aircraft_from_list(self.get_plane())
        return 'Plane has departed! Enjoy your flight!!'

    def arrive(self):
        self.get_destination().add_aircraft_to_list(self.get_plane())
        return 'Your plane has safely landed, thank you for travelling!'

