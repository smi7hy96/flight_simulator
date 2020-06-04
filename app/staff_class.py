from app.person_class import *


class Staff(Person):
    def __init__(self, tax_number, name, employee_no, work_location=None):
        super().__init__(tax_number, name)
        self.__employee_no = employee_no
        self.__work_location = work_location

    def get_employee_no(self):
        return self.__employee_no

    def set_employee_no(self, employee_no):
        self.__employee_no = employee_no

    def get_work_location(self):
        return self.__work_location

    def set_work_location(self, work_location):
        self.__work_location = work_location
