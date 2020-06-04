import unittest
from app.passenger_class import *


class PassengerTest(unittest.TestCase):
    def setUp(self):
        self.passenger_1 = Passenger('23456A', 'Bob', '55566ABC')
