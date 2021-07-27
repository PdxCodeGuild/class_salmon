# Conversion rate for feet to meter
conversion_table = {
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000,
    "yd": 0.9144,
    "in": 0.0254
}


def convert_input_distance(from_unit, to_unit, distance):
    from_unit = user_input_unit
    to_unit = user_output_unit
    distance = user_input_distance
    return (distance * conversion_table[from_unit]) / conversion_table[to_unit]


while True:
    # Prompt for the distance in feet
    user_input_distance = input("What is the distance?: ")

    # Prompt for input unit
    user_input_unit = input("Convert from unit: (ft/mi/m/km/yd/in): ")

    # Prompt for output unit
    user_output_unit = input("Convert to unit: (ft/mi/m/km/yd/in): ")

    # Convert user input to int
    user_input_distance = int(user_input_distance)

    # Convert the original input to meter output
    meter_conversion = convert_input_distance(user_input_unit, user_output_unit, user_input_distance)

    # Output result
    print(f"{user_input_distance} {user_input_unit} is {meter_conversion} {user_output_unit}.")