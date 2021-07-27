"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 01
Version: 1
Date: 5/18/2021

"""

# dict with conversion units
units = {
    'ft': .3048,
    'm': 1,
    'mi': 1609.34,
    'km': 1000,
    'yd': .9144,
    'in': .0254
}

# Get the number and unit you want to convert
original_length = int(input("Enter original length: "))
print("Choose from the following:\nft/m/mi/km/yd/in")
original_unit = input("Enter unit to convert from: ")
conversion_unit = input("Enter unit to convert to: ")

# Convert original length to meters.
length_in_meters = original_length * (units[original_unit])
# Convert from meters to final units.
print(f"Converted length: {length_in_meters * (1/units[conversion_unit]):.2f} {conversion_unit}")
input("Press any key to continue.")


"""
Notes:

FYI, This lab is the same as lab 3 of programming 102.

"""
