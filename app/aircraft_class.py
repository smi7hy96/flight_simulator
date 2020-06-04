class Aircraft:
    def __init__(self, name, capacity):
        self.__name = name
        self.__capacity = capacity

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, capacity):
        self.__capacity = capacity
