from app.person_class import *


class Passenger(Person):
    def __init__(self, tax_number, name, passport_no):
        super().__init__(tax_number, name)
        self.__passport_no = passport_no

    def get_passport_no(self):
        return self.__passport_no

    def set_passport_no(self, passport_no):
        self.__passport_no = passport_no
