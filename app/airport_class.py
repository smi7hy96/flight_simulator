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
        self.__aircraft_list.append(aircraft)

    def remove_aircraft_from_list(self, aircraft):
        self.__aircraft_list.remove(aircraft)
