# Version 1
# Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.
foot = {'meters': 0.3048}
number_of_feet = int(input(f'what is the distance in feet? '))
print(f"{foot['meters'] * number_of_feet:.4f}")

# Version 2
# Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.
convert_to_meters = {
    'ft': 0.3048,
    'mi': 1609.35,
    'm': 1,
    'km': 1000,

#  Version 3
# Add support for yards, and inches.
    'yd': 0.9144,
    'in': 0.0254
}

# Version 4
# Now we'll ask the user for the distance, the starting units, and the units to convert to.

distance = input("what is the distance? ")
input_units = input("what are the input units? ")
output_units = input("what are the output units? ")
total_meters = int(distance) * convert_to_meters[input_units]
final_conversion = total_meters / convert_to_meters[output_units]
print(f'{distance} {input_units} is {final_conversion:.4f} {output_units}')

    
