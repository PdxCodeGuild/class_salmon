"""

Author: Jeremy Bush
Project: Radio Utilities in Python (RUPy)
Version: 1
Date: 6/8/2021

"""
"""

Application notes:

This solution is unique to Windows.  Mac and Linux systems have several applications that can perform this type of
function, however none exists for Windows.  

"""


# Import required libraries
import gps
import wl2k




def menu_with_gps():
    while True:
        print(" Main Menu ".center(40, '*'))
        print("Choose an option:\n- Show current Maidenhead grid square\n- Show Current GPS Coordinates\n"
              "- Update Winlink station list\n- Get list of all Winlink stations\n- Get list of nearby stations by mode\n"
              "- Update Winlink Maidenhead grid square\nEnter 'help' to see a list of commands.")
        choice = input(">> ")
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
                    print(f"Call: {stations[station]['Callsign']}  ")


def menu_without_gps():
    while True:
        print(" Main Menu ".center(40, '*'))
        print("Choose an option:\n- Show current Maidenhead grid square\n- Update Winlink station list\n"
              "- Get list of all Winlink stations\n- Get list of stations by mode\n"
              "Enter 'help' to see a list of commands.")


def help_list():
    print("Commands:\n'scg': Show current Maidenhead grid square\n'gps': Show current GPS coordinates\n"
          "'uws': Update Winlink station list\n'wl-all': Get list of all Winlink stations\n"
          "'wl-mode': Get list of nearby stations by operating mode\n'wl-upg': Update Winlink config with current grid"
          "'help': Get list of commands")


if __name__ == "__main__":
    print(" Radio Utilities for Python ".center(40, "="))
    print('=' for i in range(0, 39))
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
