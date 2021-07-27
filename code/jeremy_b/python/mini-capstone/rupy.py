# Import required libraries
import gps
import wl2k

"""

Author: Jeremy Bush
Project: Radio Utilities in Python (RUPy)
Version: 1
Date: 6/11/2021

"""
"""

Application notes:

This solution is unique to Windows.  Mac and Linux systems have several applications that can perform this type of
function, however none exists for Windows.  

"""


def menu_with_gps():
    while True:
        print(" Main Menu ".center(40, '*'))
        print("Choose an option:\n- Show current Maidenhead grid square\n- Show Current GPS Coordinates\n"
              "- Update Winlink station list\n- Get list of all Winlink stations\n- Get list of nearby stations by mode\n"
              "- Update Winlink Maidenhead grid square\n- Exit\nEnter 'help' to see a list of commands.")
        choice = input(">> ").lower()
        try:
            if choice == 'scg':
                print(f"Current Grid Square: {gps.get_current_grid_square()}")
            elif choice == 'gps':
                print(f"Current Coordinates: {gps.get_gps_coordinates()}")
            elif choice == 'uws':
                print(f"Updating list of Winlink stations...")
                wl2k.update_winlink_node_list()
            elif choice == 'wl-all':
                stations = wl2k.get_close_nodes(gps.get_current_grid_square())
                for station in range(len(stations) - 1):
                    print(f"Call: {stations[station]['Callsign']}  Mode: {stations[station]['Mode']}  "
                          f"Frequency: {stations[station]['Frequency']}  Distance: {stations[station]['Distance']}")
            elif choice == 'wl-mode':
                mode = int(input('Enter mode: '))
                stations = wl2k.get_close_nodes_by_mode(mode)
                for station in range(0,24):
                    print(f"Call: {stations[station]['Callsign']}  Mode: {stations[station]['Mode']}  "
                          f"Frequency: {stations[station]['Frequency']}  Distance: {stations[station]['Distance']}")
            elif choice == 'wl-upg':
                coords = gps.get_gps_coordinates()
                new_grid = gps.convert_to_grid(coords[0], coords[1])
                print(f"Listed Maindenhead grid square is {gps.get_current_grid_square()}.  Per GPS, current grid square"
                      f"is {gps.convert_to_grid(coords[0], coords[1])}.")
                print('Updating Winlink config with current grid square...')
                wl2k.update_winlink_config(new_grid)
                print(f"Successfully updated grid square to {gps.get_current_grid_square()}.")
            elif choice == 'help':
                help_list()
            elif choice == 'exit':
                break
            else:
                raise ValueError
        except ValueError:
            print("Please enter a valid menu option or enter 'help' for assistance.")


def menu_without_gps():
    while True:
        print(" Main Menu ".center(40, '*'))
        print("Choose an option:\n- Show current Maidenhead grid square\n- Update Winlink station list\n"
              "- Get list of all Winlink stations\n- Get list of stations by mode\n"
              "Enter 'help' to see a list of commands.")
        choice = input(">> ").lower()
        try:
            if choice == 'scg':
                print(f"Current Grid Square: {gps.get_current_grid_square()}")
            elif choice == 'gps':
                print(f"Current Coordinates: {gps.convert_to_latlong(gps.get_current_grid_square())}")
            elif choice == 'uws':
                print(f"Updating list of Winlink stations...")
                wl2k.update_winlink_node_list()
            elif choice == 'wl-all':
                stations = wl2k.get_close_nodes(gps.get_current_grid_square())
                for station in range(len(stations) - 1):
                    print(f"Call: {stations[station]['Callsign']}  Mode: {stations[station]['Mode']}  "
                          f"Frequency: {stations[station]['Frequency']}  Distance: {stations[station]['Distance']}")
            elif choice == 'wl-mode':
                mode = int(input('Enter mode: '))
                stations = wl2k.get_close_nodes_by_mode(mode)
                for station in range(0, 24):
                    print(f"Call: {stations[station]['Callsign']}  Frequency: {stations[station]['Frequency']}  "
                          f"Distance: {stations[station]['Distance']}")
            elif choice == 'help':
                help_list()
            elif choice == 'exit':
                break
            else:
                raise ValueError
        except ValueError:
            print("Please enter a valid menu option or enter 'help' for assistance.")


def help_list():
    print("Commands:\n'scg': Show current Maidenhead grid square\n'gps': Show current GPS coordinates\n"
          "'uws': Update Winlink station list\n'wl-all': Get list of all Winlink stations\n"
          "'wl-mode': Get list of nearby stations by operating mode\n'wl-upg': Update Winlink config with current grid"
          "\n'exit': Exit the program\n'help': Get list of commands")


if __name__ == "__main__":
    print(" Radio Utilities for Python ".center(40, "="))
    choice = input("Is GPS connected on COM7? (y/n)")
    try:
        if choice.lower() == 'y':
            menu_with_gps()
        elif choice.lower == 'n':
            menu_without_gps()
        else:
            raise ValueError
    except ValueError:
        print("Please enter 'y' or 'n'.")
    print("Thank you for Using RUPy!")
