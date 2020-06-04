import unittest
from app.staff_class import *


class StaffTest(unittest.TestCase):
    def setUp(self):
        self.staff_1 = Staff('4567F', 'Adam', 1)
