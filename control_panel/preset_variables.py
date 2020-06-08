from app.plane_class import *
from app.airport_class import *
from app.staff_class import *
from app.passenger_class import *
from app.flight_trip_class import *

plane_1 = Plane('Airbus A380', 200)
plane_2 = Plane('Airbus A220', 20)
plane_3 = Plane('Boeing 747', 160)
airport_1 = Airport('Madrid')
airport_2 = Airport('Gatwick', [plane_1, plane_2])
staff_1 = Staff('ABC123', 'Susan', 1, airport_2.get_name())
staff_2 = Staff('GHJ564', 'Brian', 2, airport_2.get_name())
staff_3 = Staff('LKJ789', 'Roger', 3, airport_1.get_name())
passenger_1 = Passenger('DEF456', 'Peter', '11112222LL')
passenger_2 = Passenger('MNB356', 'Nathan', '99965232PA')
passenger_3 = Passenger('UIW856', 'Helen', '48563215AS')
flight_1 = FlightTrip(airport_2, airport_1, 2.5, plane_1)

plane_list = [plane_1, plane_2, plane_3]
airport_list = [airport_1, airport_2]
staff_list = [staff_1, staff_2, staff_3]
passenger_list = [passenger_1, passenger_2, passenger_3]
flight_list = [flight_1]
completed_flights = []