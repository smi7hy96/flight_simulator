# FLIGHT SIMULATOR

## Introduction

This Flight Simulator Application is fully Object Orientated and is a system that manages a flight company. By executing the main file (control_panel/user_interface.py), a staff member can log-in and perform a number of different functions such as adding passengers and flights. It has a number of Classes and was developed using UnitTesting.

## To Start

Start this application by running the user_interface.py file (located in directory 'control_panel'). From there you will be welcomed and then asked to log-in. The password must be correct in order to gain access, the password is also hashed for a layer of security. There are some pre-created variables (some airports, planes and people) for the user so that the system is not completely empty when first run.

From here you will be see the admin control panel where you can access every feature of the application (to log out just type 'exit' in this panel)

## Admin Control Panel 

This is a switchboard styled interface, so in order to navigate the menu's successfully you will have to enter the number of the option you want. For example, for Passenger Settings enter '4'. Incorrect Numbers or Strings are checked for and will produce an error until you enter a valid option.

## Airport Settings

Here the user can; add a new airport, get a list of planes available for use at each airport, add a new plane to an airport (assuming there are some available and they're not already based at another airport), remove a plane from an airport and list all the airports currently in the system.

## Plane Settings

4 Options in this menu; 
- Buy new plane - used to get a completely new model of plane (if the model entered already exists in fleet, you will be recommended to buy more of them and adding again is not allowed)
 - Buy more planes - for models that already exists the user can get more of that particular model
 - Get capacity of each plane
 - Get list of all planes currently in the system - and it also shows how many are available (ie. planes not currently based at any airport)
 
 ## Staff Settings
 
 Manage the staff personnel in the system.
 - Add Staff
 - Get work location - Ie. where they're base airport is.
 - List of all staff currently hired
 - Remove staff - if they are no longer in employment they do not need to be in the system.
 
 ## Passenger Settings
 
 Much the same as the Staff Settings, the user can:
 - Add a passenger
 - Get list of passenegrs
 - Remove Passenger from System.
 
 ## Flight Settings
 The bulk of the functions in the application are situated here. In this section the user can:
 - Add a new flight - using origin and destination that must be airports, as well as assigning a plane that must belong at the origin airport. Price of each seat is calculated by the duration (duration x 60)
 - Add Passenger to Flight - add any passenger to a flight, can be repeated function but the same passenger cannot be  added twice. Price updated
 - Remove Passenger from Flight - Price will update
 - Add Staff to Flight - Add a member of staff to the flight, obviously they do not pay so the price will not increase here.
 - Remove Staff from Flight
 - Get all passengers in a certain flight. Retrieve all passengers from the flight
 - Change plane - Use a different plane (as long as that plane is still at the origin), say if more seats are needed, user can get a bigger plane
 - Get all flights - Get a list of all current flights that have not yet taken off.
 - Get completed flights - Get a list of all finished flights
 - Total Profits - total amount of money made - ONLY Applies to completed flights. 
 - TAKE OFF - THE MAIN FUNCTION. Select a flight to take off and send the passengers on holiday. Here the flight will now be completed, the profit total will be updated and the plane used in the flight will be taken off of the origin airport and will now be situated at the destination airport. Creating a network of travel.