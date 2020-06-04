from app.person_class import *


class Staff(Person):
    def __init__(self, tax_number, name, employee_no, work_location=None):
        super().__init__(tax_number, name)
        self.employee_no = employee_no
        self.work_location = work_location
