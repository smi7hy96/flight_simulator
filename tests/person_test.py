import unittest
from app.person_class import *


class PersonTest(unittest.TestCase):
    def setUp(self):
        self.person_1 = Person('12345D', 'Ryan')
