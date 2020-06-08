from control_panel.preset_variables import *


def check_if_number(number):
    if number.isnumeric():
        return True
    else:
        return False


def check_admin_choice(number):
    if number == 1:
        airport_settings_choice()
    # elif number == 2:
    #     plane_settings_choice()
    # elif number == 3:
    #     staff_settings_choice()
    # elif number == 4:
    #     passenger_settings_choice()
    # elif number == 5:
    #     make_a_flight_choice()




def add_airport():
    print(airport_1.get_name())


def get_planes_in_airport():
    pass


def add_plane_to_airport():
    pass


def remove_plane_from_airport():
    pass


def get_all_airports():
    pass


def airport_settings_choice():
    print("AIRPORT CONTROL: \n")
    print("1) Add Airport")
    print("2) Get List of Planes")
    print("3) Add Plane")
    print("4) Remove Plane")
    print("5) List of Airports")
    back_code = False
    while not back_code:
        user_choice = input("Pick a number 1-5 to navigate the menu. type 'back' if you want to return to the Admin menu \n")
        if user_choice == 'back':

            back_code = True
        else:
            if check_if_number(user_choice):
                check_airport_choice(int(user_choice))


def check_airport_choice(number):
    if number == 1:
        add_airport()
    elif number == 2:
        get_planes_in_airport()
    elif number == 3:
        add_plane_to_airport()
    elif number == 4:
        remove_plane_from_airport()
    elif number == 5:
        get_all_airports()