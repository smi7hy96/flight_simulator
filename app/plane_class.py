from app.aircraft_class import *


class Plane(Aircraft):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)
