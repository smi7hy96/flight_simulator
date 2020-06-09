class Aircraft:
    def __init__(self, name, capacity, quantity, available):
        self.__name = name
        self.__capacity = capacity
        self.__quantity = quantity
        self.__available = available

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def get_available(self):
        return self.__available

    def set_available(self, available):
        self.__available = available

    def buy_planes(self, quantity):
        self.set_quantity(self.get_quantity() + quantity)
        self.set_available(self.get_available() + quantity)
