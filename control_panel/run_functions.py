from control_panel.preset_variables import *


def check_if_number(number):
    if number.isnumeric():
        return True
    else:
        return False


def check_admin_choice(number):
    if number == 1:
        airport_settings_choice()
    elif number == 2:
        plane_settings_choice()
    # elif number == 3:
    #     staff_settings_choice()
    # elif number == 4:
    #     passenger_settings_choice()
    # elif number == 5:
    #     make_a_flight_choice()


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
            for plane in airport_list[int(user_choice)-1].get_aircraft_list():
                planes.append(plane.get_name())
            if len(planes) == 0:
                planes = "No planes currently at this airport"
            return planes
        else:
            return "Invalid number selected"
    else:
        return "Invalid number selected"


def add_plane_to_airport():
    for x in range(1, len(airport_list) + 1):
        print(f'{x}) {airport_list[x - 1].get_name()} \n')
    user_choice = input("Pick an airport using the number guide \n")
    if check_if_number(user_choice):
        if int(user_choice) <= len(airport_list):
            selected_airport = airport_list[int(user_choice)-1]
            print(f'{selected_airport.get_name()} Selected \n')
            for x in range(1, len(plane_list) + 1):
                print(f'{x}) {plane_list[x - 1].get_name()} \n')
            user_choice = input("Now pick a plane to add \n")
            if check_if_number(user_choice):
                if int(user_choice) <= len(plane_list):
                    selected_airport.add_aircraft_to_list(plane_list[int(user_choice)-1])
                    return f'{plane_list[int(user_choice)-1].get_name()} added'
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
    print("AIRPORT CONTROL: \n")
    print("1) Add Plane")
    print("2) Get Capacity")
    print("3) Get List of Planes")


def plane_settings_choice():
    print_plane_panel()
    back_code = False
    while not back_code:
        user_choice = input(
            "Pick a number 1-3 to navigate the menu. type 'back' if you want to return to the Admin menu \n")
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
        print(get_capacity())
    elif number == 3:
        print(get_all_planes())


def add_plane():
    name = input("Enter name of the new Plane \n")
    input_check = False
    while not input_check:
        capacity = input(f'Enter capacity of the {name} \n')
        if check_if_number(capacity):
            plane_list.append(Plane(name, int(capacity)))
            input_check = True
    return f'{name} added'


def get_all_planes():
    planes_names = []
    for plane in plane_list:
        planes_names.append(plane.get_name())
    return planes_names

def get_capacity():
    for x in range(1, len(plane_list) + 1):
        print(f'{x}) {plane_list[x-1].get_name()} \n')
    user_choice = input("Pick a plane using the number guide \n")
    if check_if_number(user_choice):
        if int(user_choice) <= len(plane_list):
            return plane_list[int(user_choice) - 1].get_capacity()
        else:
            return "Invalid number selected"
    else:
        return "Invalid number selected"
