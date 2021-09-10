# Conversion rate for feet to meter
conversion_table = {
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000,
    "yd": 0.9144,
    "in": 0.0254
}


def convert_input_distance(unit, distance):
    unit = user_input_unit
    distance = user_input_distance
    return distance * conversion_table[unit]


while True:
    # Prompt for the distance in feet
    user_input_distance = input("What is the distance?: ")

    # Prompt for input unit
    user_input_unit = input("Convert from unit: (ft/mi/m/km/yd/in): ")

    # Prompt for output unit
    user_output_unit = input("Convert to unit: (ft/mi/m/km/yd/in): ")

    # Convert user input to int
    user_input_distance = int(user_input_distance)

    # Call dictionary for conversion values
    convert_from =

    # Convert the original input to meter output
    meter_conversion_input = {convert_input_distance(user_input_unit, user_input_distance)}
    print(meter_conversion_input)

    # Output result
    print(f"{user_input_distance} {user_input_unit} is {convert_input_distance(user_input_unit, user_input_distance)} m.")

# Enter the distance
# Assign to base variable(base_num)

# enter the starting unit
# call dictionary for key value
# assign to variable(convert_from)

# enter the converting unit
# call dictionary for key value
# assign to variable(convert_to)

# Function
# given the base, convert_from, and convert_to value
# multiply the base and convert_from
# assign to variable(base_result)
# divide the (base_result) by the convert_to value
# assign to variable(final_result)
# return (final_result)

# output the (final_result)

