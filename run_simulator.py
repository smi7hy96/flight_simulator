from control.presets import *
import time

print('WELCOME! You have the honour of joining the most prestigious airline in the world! CONGRATS!')
time.sleep(1)
print('As our new admin, you will be in charge of managing the airports, planes, staff and passengers in our database. \nAnd then letting our holidaymakers take flight!!')
time.sleep(0.5)
print("Your password will be 'adminplane' if you need to make changes to details of a flight. \n What would you like to do first?")
print("ADMIN CONTROL: \n")
print("1) Airport Settings")
print("2) Plane Settings")
print("3) Staff Settings")
print("4) Passenger Settings")
print("5) Make a flight!")

exit_code = False
while not exit_code:
    user_choice = input("Pick a number 1-5 to navigate the menu. type 'exit' when you want to log out \n")
    if user_choice == 'exit':
        exit_code = True
    else:
        if check_if_number(user_choice):
            check_admin_choice(int(user_choice))
