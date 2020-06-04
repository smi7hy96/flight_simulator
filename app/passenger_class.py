from app.person_class import *


class Passenger(Person):
    def __init__(self, tax_number, name, passport_no):
        super().__init__(tax_number, name)
        self.passport_no = passport_no
