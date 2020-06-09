import unittest
from app.passenger_class import *


class PassengerTest(unittest.TestCase):
    def setUp(self):
        self.passenger_1 = Passenger('23456A', 'Bob', '55566ABC')

    def test_get_passport_no(self):
        self.assertEqual(self.passenger_1.get_passport_no(), '55566ABC')
        self.passenger_1.set_passport_no(2)
        self.assertEqual(self.passenger_1.get_passport_no(), 2)