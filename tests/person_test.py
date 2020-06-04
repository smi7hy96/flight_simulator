import unittest
from app.person_class import *


class PersonTest(unittest.TestCase):
    def setUp(self):
        self.person_1 = Person('12345D', 'Ryan')

    def test_get_name(self):
        self.assertEqual(self.person_1.get_name(), 'Ryan')
        self.person_1.set_name('Harry')
        self.assertEqual(self.person_1.get_name(), 'Harry')

    def test_get_tax_number(self):
        self.assertEqual(self.person_1.get_tax_number(), '12345D')
        self.person_1.set_tax_number('123A')
        self.assertEqual(self.person_1.get_tax_number(), '123A')
