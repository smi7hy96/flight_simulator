class Person:
    def __init__(self, tax_number, name):
        self.__tax_number = tax_number
        self.__name = name

    def get_tax_number(self):
        return self.__tax_number

    def set_tax_number(self, tax_number):
        self.__tax_number = tax_number

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

