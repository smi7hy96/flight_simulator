from collections import Counter

class Airport:
    def __init__(self, name, aircraft_list=None):
        self.__name = name
        if aircraft_list is None:
            aircraft_list = []
        self.__aircraft_list = aircraft_list

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_aircraft_list(self):
        return self.__aircraft_list

    def set_aircraft_list(self, aircraft_list):
        self.__aircraft_list = aircraft_list

    def add_aircraft_to_list(self, aircraft):
        if aircraft.get_available() > 0:
            self.__aircraft_list.append(aircraft)
            aircraft.set_available(aircraft.get_available() - 1)
        else:
            return "No more of this model available"

    def remove_aircraft_from_list(self, aircraft):
        if aircraft.get_available() < aircraft.get_quantity():
            self.__aircraft_list.remove(aircraft)
            aircraft.set_available(aircraft.get_available() + 1)
        else:
            return "This model not currently in use anywhere"

    def aircraft_quantities(self):
        og_list = self.get_aircraft_list()
        temp_list = Counter(og_list)
        new_list = []
        for key, value in temp_list.items():
            name = key.get_name()
            quantity = value
            new_list.append(f'{name}, {quantity} available')
        return new_list
