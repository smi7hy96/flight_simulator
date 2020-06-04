import unittest
from app.staff_class import *


class StaffTest(unittest.TestCase):
    def setUp(self):
        self.staff_1 = Staff('4567F', 'Adam', 1)

    def test_get_employee_no(self):
        self.assertEqual(self.staff_1.get_employee_no(), 1)
        self.staff_1.set_employee_no(2)
        self.assertEqual(self.staff_1.get_employee_no(), 2)

    def test_get_tax_number(self):
        self.assertEqual(self.staff_1.get_work_location(), None)
        self.staff_1.set_tax_number('Barcelona')
        self.assertEqual(self.staff_1.get_tax_number(), 'Barcelona')
