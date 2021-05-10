"""
Lab 9: convert the given distance and units to the target units
we have four types of units: meters (m), miles (mi), feet (ft), and kilometers (km)
we could handle each case individually
    e.g. if from_units == 'm' and to_units == 'miles'
instead, we'll just convert to meters, then convert to the target units
"""

# 1) get the distance from the user
# 2) convert that distance to a float
# 3) get the units for that distance from the user
# 4) get the units that the user wants to convert to
# 4) convert the distance to meters
# 5) convert the distance from meters to the target


# 1 mile is 1609.34 meters
# 1 foot is 0.3048 meters
# 1 kilometer is 1000 meters
# 1 meter is 1 meter
# 1 yard is 0.9144 meters
# 1 inch is 0.0254 meters

units_in_meters = {
    'mi': 1609.34,
    'ft': 0.3048,
    'km': 1000,
    'm': 1,
    'yd': 0.9144,
    'in': 0.0254
}

# convert the given distance from the given units to meters
def to_meters(distance, units):
    return distance * units_in_meters[units]

# convert the given distance (in meters) to the target units
def from_meters(distance, units):
    return distance / units_in_meters[units]

def standardize_units(units):
    if units in ['m', 'meter', 'meters']:
        return 'm'
    elif units in ['mi', 'mile', 'miles']:
        return 'mi'
    elif units in ['ft', 'feet']:
        return 'ft'
    elif units in ['km', 'kilometer', 'kilometers']:
        return 'km'
    elif units in ['yd', 'yard', 'yards']:
        return 'yd'
    elif units in ['in', 'inch', 'inches']:
        return 'in'

def main():
    print('Welcome to the Distance Converter 5001™')

    while True:
        try:
            distance = float(input('Enter your distance: '))
            break
        except ValueError as e:
            pass
            # print(e)
            # print('Error: Please enter a number')

    while True:
        units = standardize_units(input('Enter your units: '))
        if units:
            break

    while True:
        target_units = standardize_units(input('Enter your desired units: '))
        if target_units:
            break

    # convert distance to meters from units in
    distance_to_meters = to_meters(distance, units)
    # convert distance in meters to desired units
    meters_to_units = from_meters(distance_to_meters, target_units)

    # print output
    print(f'{distance} {units} is {round(meters_to_units, 4)} {target_units}')

main()

