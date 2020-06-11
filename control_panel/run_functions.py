import time
from control_panel.preset_variables import *


def check_if_number(number):
    if number.isnumeric():
        return True
    else:
        return False


def check_if_float(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


def check_admin_choice(number):
    if number == 1:
        airport_settings_choice()
    elif number == 2:
        plane_settings_choice()
    elif number == 3:
        staff_settings_choice()
    elif number == 4:
        passenger_settings_choice()
    elif number == 5:
        flight_settings_choice()


def add_airport():
    name = input("Enter name of the new Airport \n")
    airport_list.append(Airport(name))
    return f'{name} added'


def get_planes_in_airport():
    for x in range(1, len(airport_list)+1):
        print(f'{x}) {airport_list[x-1].get_name()} \n')
    user_choice = input("Pick an airport using the number guide \n")
    planes = []
    if check_if_number(user_choice):
        if int(user_choice) <= len(airport_list):
            for plane in airport_list[int(user_choice)-1].aircraft_quantities():
                planes.append(plane)
            if len(planes) == 0:
                planes = "No planes currently at this airport"
            return planes
        else:
            return "Invalid number selected"
    else:
        return "Invalid number selected"


def add_plane_to_airport():
    temp_list = []
    for x in range(1, len(airport_list) + 1):
        print(f'{x}) {airport_list[x - 1].get_name()} \n')
    user_choice = input("Pick an airport using the number guide \n")
    if check_if_number(user_choice):
        if int(user_choice) <= len(airport_list):
            selected_airport = airport_list[int(user_choice)-1]
            print(f'{selected_airport.get_name()} Selected \n')
            for x in range(1, len(plane_list) + 1):
                if plane_list[x-1].get_available() > 0:
                    temp_list.append(plane_list[x - 1])

            if len(temp_list) == 0:
                return "No more planes available, need to purchase more"
            for y in range(1, len(temp_list) + 1):
                print(f'{y}) {temp_list[y - 1].get_name()} \n')
            user_choice = input("Now pick a plane to add \n")
            if check_if_number(user_choice):
                if int(user_choice) <= len(temp_list):
                    selected_airport.add_aircraft_to_list(temp_list[int(user_choice)-1])
                    return f'{temp_list[int(user_choice)-1].get_name()} added'
                else:
                    return "Invalid number selected"
            else:
                return "Invalid number selected"
        else:
            return "Invalid number selected"
    else:
        return "Invalid number selected"


def remove_plane_from_airport():
    for x in range(1, len(airport_list)+1):
        print(f'{x}) {airport_list[x-1].get_name()} \n')
    planes = []
    planes_found = False
    selected_airport = ''
    while not planes_found:
        user_choice = input("Pick an airport using the number guide \n")
        if check_if_number(user_choice):
            if int(user_choice) <= len(airport_list):
                selected_airport = airport_list[int(user_choice)-1]
                for plane in airport_list[int(user_choice)-1].get_aircraft_list():
                    planes.append(plane)
                if len(planes) == 0:
                    planes = "No planes currently at this airport"
                planes_found = True
            else:
                return "Invalid number selected"
        else:
            return "Invalid number selected"
    for x in range(1, len(planes) + 1):
        print(f'{x}) {planes[x - 1].get_name()} \n')
    user_choice = input("Now pick a plane to remove \n")
    print(planes[int(user_choice) - 1].get_name())
    selected_airport.remove_aircraft_from_list(planes[int(user_choice) - 1])
    return f'{planes[int(user_choice) - 1].get_name()} removed'


def get_all_airports():
    airport_names = []
    for airport in airport_list:
        airport_names.append(airport.get_name())
    return airport_names


def print_airport_panel():
    print("AIRPORT CONTROL: \n")
    print("1) Add Airport")
    print("2) Get List of Planes")
    print("3) Add Plane")
    print("4) Remove Plane")
    print("5) List of Airports")


def airport_settings_choice():
    print_airport_panel()
    back_code = False
    while not back_code:
        user_choice = input("Pick a number 1-5 to navigate the menu. type 'back' if you want to return to the Admin menu \n")
        if user_choice == 'back':
            back_code = True
        else:
            if check_if_number(user_choice):
                check_airport_choice(int(user_choice))
                print_airport_panel()


def check_airport_choice(number):
    if number == 1:
        print(add_airport())
    elif number == 2:
        print(get_planes_in_airport())
    elif number == 3:
        print(add_plane_to_airport())
    elif number == 4:
        print(remove_plane_from_airport())
    elif number == 5:
        print(get_all_airports())


def print_plane_panel():
    print("PLANE CONTROL: \n")
    print("1) Buy New Plane")
    print("2) Buy More Planes")
    print("3) Get Capacity")
    print("4) Get List of Planes")


def plane_settings_choice():
    print_plane_panel()
    back_code = False
    while not back_code:
        user_choice = input(
            "Pick a number 1-4 to navigate the menu. type 'back' if you want to return to the Admin menu \n")
        if user_choice == 'back':
            back_code = True
        else:
            if check_if_number(user_choice):
                check_plane_choice(int(user_choice))
                print_plane_panel()


def check_plane_choice(number):
    if number == 1:
        print(add_plane())
    elif number == 2:
        print(add_more_planes())
    elif number == 3:
        print(get_capacity())
    elif number == 4:
        print(get_all_planes())


def add_plane():
    name = input("Enter name of the new Plane \n")
    for x in range(len(plane_list)):
        if name == plane_list[x].get_name():
            return "Plane already in fleet, try buying more instead"
    input_check = False
    while not input_check:
        capacity = input(f'Enter capacity of the {name} \n')
        if check_if_number(capacity):
            input_check = True
    input_check = False
    while not input_check:
        quantity = input(f'Enter Quantity of the {name} \n')
        if check_if_number(quantity):
            plane_list.append(Plane(name, int(capacity), int(quantity), int(quantity)))
            input_check = True
    return f'{name} added'


def add_more_planes():
    for x in range(1, len(plane_list) + 1):
        print(f'{x}) {plane_list[x-1].get_name()} \n')
    user_correct = False
    while not user_correct:
        user_choice = input("Pick a plane using the number guide \n")
        if check_if_number(user_choice):
            if int(user_choice) <= len(plane_list):
                selected_plane = plane_list[int(user_choice) - 1]
                user_correct = True
            else:
                return "Invalid number selected"
        else:
            return "Invalid number selected"
    user_correct = False
    while not user_correct:
        quantity = input(f'How many {selected_plane.get_name()} do you want to purchase? \n')
        if check_if_number(user_choice):
            selected_plane.buy_planes(int(quantity))
            user_correct = True
        else:
            return "Invalid number selected"


def get_all_planes():
    planes_names = []
    for plane in plane_list:
        planes_names.append(f'{plane.get_name()}, {plane.get_available()} available')
    return planes_names


def get_capacity():
    for x in range(1, len(plane_list) + 1):
        print(f'{x}) {plane_list[x-1].get_name()} \n')
    input_correct = False
    while not input_correct:
        user_choice = input("Pick a plane using the number guide \n")
        if check_if_number(user_choice):
            if int(user_choice) <= len(plane_list):
                input_correct = True
                return plane_list[int(user_choice) - 1].get_capacity()
            else:
                return "Invalid number selected"
        else:
            return "Invalid number selected"


def print_staff_panel():
    print("STAFF CONTROL: \n")
    print("1) Add Staff")
    print("2) Get Work Location")
    print("3) Get List of Staff")
    print("4) Remove Member of Staff")


def staff_settings_choice():
    print_staff_panel()
    back_code = False
    while not back_code:
        user_choice = input(
            "Pick a number 1-4 to navigate the menu. type 'back' if you want to return to the Admin menu \n")
        if user_choice == 'back':
            back_code = True
        else:
            if check_if_number(user_choice):
                check_staff_choice(int(user_choice))
                print_staff_panel()


def check_staff_choice(number):
    if number == 1:
        print(add_staff())
    elif number == 2:
        print(get_work_location())
    elif number == 3:
        print(get_all_staff())
    elif number == 4:
        print(remove_staff())


def add_staff():
    name = input("Enter name of the new Staff Member \n")
    tax = input(f'Enter Tax No. for {name} \n')
    for x in range(1, len(airport_list) + 1):
        print(f'{x}) {airport_list[x - 1].get_name()} \n')
    airport_selection = False
    while not airport_selection:
        user_choice = input(f'Enter Location for {name} using number guide of airport\n')
        if check_if_number(user_choice):
            if int(user_choice) <= len(airport_list):
                selected_airport = airport_list[int(user_choice)-1]
                print(f'{selected_airport.get_name()} Selected \n')
                location = selected_airport.get_name()
                airport_selection = True
            else:
                print("Invalid number selected")
        else:
            print("Invalid number selected")

    input_check = False
    while not input_check:
        emp_no = input(f'Enter Employee No. for {name} \n')
        if check_if_number(emp_no):
            staff_list.append(Staff(tax, name, int(emp_no), location))
            input_check = True
    return f'{name} added'


def get_work_location():
    for x in range(1, len(staff_list) + 1):
        print(f'{x}) {staff_list[x-1].get_name()} (Emp No: {staff_list[x-1].get_employee_no()})\n')
    user_choice = input("Pick an Employee using the number guide \n")
    if check_if_number(user_choice):
        if int(user_choice) <= len(staff_list):
            return staff_list[int(user_choice) - 1].get_work_location()
        else:
            return "Invalid number selected"
    else:
        return "Invalid number selected"


def get_all_staff():
    staff_names = []
    for staff in staff_list:
        staff_names.append(staff.get_name())
    return staff_names


def remove_staff():
    for x in range(1, len(staff_list) + 1):
        print(f'{x}) {staff_list[x-1].get_name()} (Emp No: {staff_list[x-1].get_employee_no()})\n')
    user_choice = input("Pick an Employee using the number guide \n")
    if check_if_number(user_choice):
        if int(user_choice) <= len(staff_list):
            staff_member = staff_list[int(user_choice) - 1]
            staff_list.remove(staff_member)
            return f'{staff_member.get_name()} removed from company'
        else:
            return "Invalid number selected"
    else:
        return "Invalid number selected"


def print_passenger_panel():
    print("PASSENGER CONTROL: \n")
    print("1) Add Passenger")
    print("2) Get List of Passengers")
    print("3) Remove Passenger from Database")


def passenger_settings_choice():
    print_passenger_panel()
    back_code = False
    while not back_code:
        user_choice = input(
            "Pick a number 1-3 to navigate the menu. type 'back' if you want to return to the Admin menu \n")
        if user_choice == 'back':
            back_code = True
        else:
            if check_if_number(user_choice):
                check_passenger_choice(int(user_choice))
                print_passenger_panel()


def check_passenger_choice(number):
    if number == 1:
        print(add_passenger())
    elif number == 2:
        print(get_all_passengers())
    elif number == 3:
        print(remove_passenger())


def add_passenger():
    name = input("Enter name of the new Passenger \n")
    tax = input(f'Enter Tax No. for {name} \n')
    passport = input(f'Enter Passport No. for {name} \n')
    passenger_list.append(Passenger(tax, name, passport))
    return f'{name} added'


def get_all_passengers():
    passenger_names = []
    for passenger in passenger_list:
        passenger_names.append(passenger.get_name())
    return passenger_names


def remove_passenger():
    for x in range(1, len(passenger_list) + 1):
        print(f'{x}) {passenger_list[x-1].get_name()} (Passport No: {passenger_list[x-1].get_passport_no()})\n')
    user_choice = input("Pick a Passenger using the number guide \n")
    if check_if_number(user_choice):
        if int(user_choice) <= len(staff_list):
            passenger = passenger_list[int(user_choice) - 1]
            passenger_list.remove(passenger)
            return f'{passenger.get_name()} removed from company'
        else:
            return "Invalid number selected"
    else:
        return "Invalid number selected"


def print_flight_panel():
    print("FLIGHT CONTROL: \n")
    print(" 1) Add Flight")
    print(" 2) Add Passenger to Flight")
    print(" 3) Remove Passenger From Flight")
    print(" 4) Add Staff to Flight")
    print(" 5) Remove Staff From Flight")
    print(" 6) Get All Passengers in Flight")
    print(" 7) Change Plane")
    print(" 8) Get All Flights")
    print(" 9) Get Completed Flights")
    print("10) Total Profits!")
    print("11) TAKE OFF!!!!!!!")


def flight_settings_choice():
    print_flight_panel()
    back_code = False
    while not back_code:
        user_choice = input(
            "Pick a number 1-11 to navigate the menu. type 'back' if you want to return to the Admin menu \n")
        if user_choice == 'back':
            back_code = True
        else:
            if check_if_number(user_choice):
                check_flight_choice(int(user_choice))
                print_flight_panel()


def check_flight_choice(number):
    if number == 1:
        print(add_flight())
    elif number == 2:
        print(add_passenger_to_flight())
    elif number == 3:
        print(remove_passenger_from_flight())
    elif number == 4:
        print(add_staff_to_flight())
    elif number == 5:
        print(remove_staff_from_flight())
    elif number == 6:
        print(get_all_passengers_in_flight())
    elif number == 7:
        print(change_plane())
    elif number == 8:
        get_all_flights()
    elif number == 9:
        print(get_completed_flights())
    elif number == 10:
        print(get_total_profits())
    elif number == 11:
        take_off()


def add_flight():
    temp_airports = list(airport_list)
    temp_planes = []
    origin = ''
    destination = ''
    a_plane = ''
    for x in range(1, len(temp_airports) + 1):
        print(f'{x}) {temp_airports[x - 1].get_name()} \n')
    user_choice = input("Pick an airport using the number guide \n")
    if check_if_number(user_choice):
        if int(user_choice) <= len(temp_airports):
            selected_airport = temp_airports[int(user_choice)-1]
            origin = selected_airport
            temp_airports.remove(selected_airport)
            print(f'{selected_airport.get_name()} Selected \n')
            for x in range(1, len(plane_list) + 1):
                if plane_list[x - 1] in selected_airport.get_aircraft_list():
                    temp_planes.append(plane_list[x-1])
            if len(temp_planes) == 0:
                return "No planes currently available"
            for y in range(1, len(temp_planes) + 1):
                print(f'{y}) {temp_planes[y - 1].get_name()} \n')
            user_choice = input("Now pick a plane to use \n")
            if check_if_number(user_choice):
                if int(user_choice) <= len(temp_planes):
                    a_plane = temp_planes[int(user_choice)-1]
                else:
                    print("Invalid number selected")
            else:
                print("Invalid number selected")
        else:
            print("Invalid number selected")
    else:
        print("Invalid number selected")

    for x in range(1, len(temp_airports) + 1):
        print(f'{x}) {temp_airports[x - 1].get_name()} \n')
    user_choice = input("Now, pick a destination airport using the number guide \n")
    if check_if_number(user_choice):
        if int(user_choice) <= len(temp_airports):
            selected_airport = temp_airports[int(user_choice)-1]
            destination = selected_airport
            print(f'{selected_airport.get_name()} Selected \n')
        else:
            print("Invalid number selected")
    else:
        print("Invalid number selected")
    duration_check = False
    while not duration_check:
        duration = input("How long will the flight be?")
        if check_if_float(duration):
            flight_list.append(FlightTrip(origin, destination, float(duration), a_plane))
            duration_check = True
        else:
            print("Invalid Number")
    return f'Flight From {origin.get_name()} to {destination.get_name()} Added!'


def add_passenger_to_flight():
    selected_flight = ''
    flight_num = False
    for x in range(1, len(flight_list) + 1):
        if flight_list[x - 1].count_people_in_flight(flight_list[x - 1].get_passenger_list()['staff'], flight_list[x - 1].get_passenger_list()['passengers']) < flight_list[x - 1].get_plane().get_capacity():
            print(f'{x}) Flying from {flight_list[x - 1].get_origin().get_name()} to {flight_list[x - 1].get_destination().get_name()}\n')
        else:
            return "All flights already full!"
    while not flight_num:
        user_choice = input("Pick a Flight to add Passenger to using the number guide \n")
        if check_if_number(user_choice):
            if int(user_choice) <= len(flight_list):
                selected_flight = flight_list[int(user_choice) - 1]
                flight_num = True
            else:
                print("Invalid number selected")
        else:
            print("Invalid number selected")
    passenger_num = False
    result = False
    for x in range(1, len(passenger_list) + 1):
        if passenger_list[x - 1] not in selected_flight.get_passenger_list()['passengers']:
            print(f'{x}) {passenger_list[x - 1].get_name()} (Passport No: {passenger_list[x - 1].get_passport_no()})\n')
            result = True
    if not result:
        return "All passengers already on board this flight"
    while not passenger_num:
        user_choice = input("Pick a Passenger to add using the number guide \n")
        if check_if_number(user_choice):
            if int(user_choice) <= len(passenger_list):
                selected_flight.add_passenger_to_flight(passenger_list[int(user_choice) - 1])
                passenger_num = True
                return f'{passenger_list[int(user_choice) - 1].get_name()} added to flight!'
            else:
                print("Invalid number selected")
        else:
            print("Invalid number selected")


def remove_passenger_from_flight():
    selected_flight = ''
    flight_num = False
    for x in range(1, len(flight_list) + 1):
        if flight_list[x - 1].count_people_in_flight(flight_list[x - 1].get_passenger_list()['staff'],
                                                     flight_list[x - 1].get_passenger_list()['passengers']) > 0:
            print(
                f'{x}) Flying from {flight_list[x - 1].get_origin().get_name()} to {flight_list[x - 1].get_destination().get_name()}\n')
        else:
            return "All flights already empty!"
    while not flight_num:
        user_choice = input("Pick a Flight to remove Passenger from using the number guide \n")
        if check_if_number(user_choice):
            if int(user_choice) <= len(flight_list):
                selected_flight = flight_list[int(user_choice) - 1]
                flight_num = True
            else:
                print("Invalid number selected")
        else:
            print("Invalid number selected")
    passenger_num = False
    if len(selected_flight.get_passenger_list()['passengers']) == 0:
        return "Flight is Empty!"
    else:
        for x in range(1, len(selected_flight.get_passenger_list()['passengers']) + 1):
            print(f'{x}) {selected_flight.get_passenger_list()["passengers"][x - 1].get_name()} (Passport No: {selected_flight.get_passenger_list()["passengers"][x - 1].get_passport_no()})\n')

    while not passenger_num:
        user_choice = input("Pick a Passenger to remove using the number guide \n")
        if check_if_number(user_choice):
            if int(user_choice) <= len(selected_flight.get_passenger_list()["passengers"]):
                removed_passenger = selected_flight.get_passenger_list()["passengers"][int(user_choice) - 1]
                selected_flight.remove_passenger_from_flight(removed_passenger)
                passenger_num = True
                return f'{removed_passenger.get_name()} removed from flight!'
            else:
                print("Invalid number selected")
        else:
            print("Invalid number selected")


def add_staff_to_flight():
    selected_flight = ''
    flight_num = False
    for x in range(1, len(flight_list) + 1):
        if flight_list[x - 1].count_people_in_flight(flight_list[x - 1].get_passenger_list()['staff'], flight_list[x - 1].get_passenger_list()['passengers']) < flight_list[x - 1].get_plane().get_capacity():
            print(f'{x}) Flying from {flight_list[x - 1].get_origin().get_name()} to {flight_list[x - 1].get_destination().get_name()}\n')
        else:
            return "All flights already full!"
    while not flight_num:
        user_choice = input("Pick a Flight to add Staff to using the number guide \n")
        if check_if_number(user_choice):
            if int(user_choice) <= len(flight_list):
                selected_flight = flight_list[int(user_choice) - 1]
                flight_num = True
            else:
                print("Invalid number selected")
        else:
            print("Invalid number selected")
    passenger_num = False
    result = False
    for x in range(1, len(staff_list) + 1):
        if staff_list[x - 1] not in selected_flight.get_passenger_list()['staff']:
            print(f'{x}) {staff_list[x - 1].get_name()} (Emp No: {staff_list[x - 1].get_employee_no()})\n')
            result = True
    if not result:
        return "All passengers already on board this flight"
    while not passenger_num:
        user_choice = input("Pick Staff Member to add using the number guide \n")
        if check_if_number(user_choice):
            if int(user_choice) <= len(staff_list):
                selected_flight.add_passenger_to_flight(staff_list[int(user_choice) - 1])
                passenger_num = True
                return f'{staff_list[int(user_choice) - 1].get_name()} added to flight!'
            else:
                print("Invalid number selected")
        else:
            print("Invalid number selected")


def remove_staff_from_flight():
    selected_flight = ''
    flight_num = False
    for x in range(1, len(flight_list) + 1):
        if flight_list[x - 1].count_people_in_flight(flight_list[x - 1].get_passenger_list()['staff'],
                                                     flight_list[x - 1].get_passenger_list()['passengers']) < \
                flight_list[x - 1].get_plane().get_capacity():
            print(
                f'{x}) Flying from {flight_list[x - 1].get_origin().get_name()} to {flight_list[x - 1].get_destination().get_name()}\n')
        else:
            return "All flights already full!"
    while not flight_num:
        user_choice = input("Pick a Flight to remove Staff from using the number guide \n")
        if check_if_number(user_choice):
            if int(user_choice) <= len(flight_list):
                selected_flight = flight_list[int(user_choice) - 1]
                flight_num = True
            else:
                print("Invalid number selected")
        else:
            print("Invalid number selected")
    passenger_num = False
    if len(selected_flight.get_passenger_list()['staff']) == 0:
        return "Flight is Empty!"
    else:
        for x in range(1, len(selected_flight.get_passenger_list()['staff']) + 1):
            print(f'{x}) {selected_flight.get_passenger_list()["staff"][x - 1].get_name()} (Employee No: {selected_flight.get_passenger_list()["staff"][x - 1].get_employee_no()})\n')

    while not passenger_num:
        user_choice = input("Pick a Staff Member to remove using the number guide \n")
        if check_if_number(user_choice):
            if int(user_choice) <= len(selected_flight.get_passenger_list()["staff"]):
                removed_passenger = selected_flight.get_passenger_list()["staff"][int(user_choice) - 1]
                selected_flight.remove_passenger_from_flight(removed_passenger)
                passenger_num = True
                return f'{removed_passenger.get_name()} removed from flight!'
            else:
                print("Invalid number selected")
        else:
            print("Invalid number selected")


def get_all_passengers_in_flight():
    flight_num = False
    results = False
    for x in range(1, len(flight_list) + 1):
        if len(flight_list[int(x) - 1].get_passenger_list()['passengers']) > 0:
            results = True
            print(
                f'{x}) Flying from {flight_list[x - 1].get_origin().get_name()} to {flight_list[x - 1].get_destination().get_name()}\n')
    if not results:
        return "All flights empty!"
    while not flight_num:
        user_choice = input("Pick a Flight to get Passengers to using the number guide \n")
        if check_if_number(user_choice):
            if int(user_choice) <= len(flight_list):
                flight_num = True
                return flight_list[int(user_choice) - 1].produce_list_of_passengers()
            else:
                print("Invalid number selected")
        else:
            print("Invalid number selected")


def change_plane():
    flight_num = False
    current_plane = ''
    current_flight = ''
    temp_plane_list = list(plane_list)
    another_plane_list = []
    if len(flight_list) > 0:
        for x in range(1, len(flight_list) + 1):
            print(f'{x}) Flying from {flight_list[x - 1].get_origin().get_name()} to {flight_list[x - 1].get_destination().get_name()}\n')
        while not flight_num:
            user_choice = input("Pick a Flight to change its plane using the number guide \n")
            if check_if_number(user_choice):
                if int(user_choice) <= len(flight_list):
                    flight_num = True
                    current_flight = flight_list[x-1]
                    current_plane = current_flight.get_plane()
                    print(f'Current plane is the {current_plane.get_name()}')
                else:
                    print("Invalid number selected")
            else:
                print("Invalid number selected")
        temp_plane_list.remove(current_plane)
        if len(temp_plane_list) > 0:
            for x in range(1, len(temp_plane_list) + 1):
                if temp_plane_list[x-1] in current_flight.get_origin().get_aircraft_list():
                    another_plane_list.append(temp_plane_list[x-1])
            if len(another_plane_list) == 0:
                return "No other planes to choose"
            for y in range(1, len(another_plane_list) + 1):
                print(f'{y}) {another_plane_list[y-1].get_name()}')
            plane_num = False
            while not plane_num:
                user_choice = input("Pick a new plane using the number guide \n")
                if check_if_number(user_choice):
                    if int(user_choice) <= len(another_plane_list):
                        plane_num = True
                        new_plane = another_plane_list[int(user_choice)-1]
                        current_flight.set_plane(new_plane)
                        return f'New plane is the {new_plane.get_name()}'
                    else:
                        print("Invalid number selected")
                else:
                    print("Invalid number selected")
        else:
            return "No more available planes"
    else:
        return "No current flights"


def get_all_flights():
    if len(flight_list) > 0:
        for x in range(1, len(flight_list) + 1):
            print(f'{x}) Flying from {flight_list[x - 1].get_origin().get_name()} to {flight_list[x - 1].get_destination().get_name()}, duration: {flight_list[x - 1].get_duration()} hours, profit (once completed): £{flight_list[x - 1].get_revenue()} \n')
    else:
        return "No available flights"


def get_completed_flights():
    if len(completed_flights) > 0:
        for x in range(1, len(completed_flights) + 1):
            print(f'{x}) Flying from {completed_flights[x - 1].get_origin().get_name()} to {completed_flights[x - 1].get_destination().get_name()}, duration: {completed_flights[x - 1].get_duration()} hours, profit: £{completed_flights[x - 1].get_revenue()}  \n')
    else:
        return "No completed flights"


def get_total_profits():
    total_profit = 0
    if len(completed_flights) > 0:
        for x in range(1, len(completed_flights) + 1):
            total_profit += completed_flights[x-1].get_revenue()
    return f'Total Money made so far is £{total_profit}'


def take_off():
    flight_num = False
    current_flight = ''
    if len(flight_list) > 0:
        for x in range(1, len(flight_list) + 1):
            print(
                f'{x}) Flying from {flight_list[x - 1].get_origin().get_name()} to {flight_list[x - 1].get_destination().get_name()}\n')
        while not flight_num:
            user_choice = input("Pick a Flight to take off using the number guide \n")
            if check_if_number(user_choice):
                if int(user_choice) <= len(flight_list):
                    flight_num = True
                    current_flight = flight_list[x - 1]
                    print("Preparing for take off, please ensure you are seated!")
                    time.sleep(2)
                    current_flight.departure()
                    print(f'AND WE ARE OFF! It will take {current_flight.get_duration()} hours to get to {current_flight.get_destination().get_name()}')
                    time.sleep(current_flight.get_duration() * 2)
                    print("Preparing for Landing.......")
                    current_flight.arrive()
                    flight_list.remove(current_flight)
                    completed_flights.append(current_flight)
                    print("Thank you for travelling with Smith Airlines! Have a lovely holiday!")
                    time.sleep(2)
                else:
                    print("Invalid number selected")
            else:
                print("Invalid number selected")