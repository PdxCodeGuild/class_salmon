#Version 1
#Ask user for number of feet then print meters
dist_feet = float(input("What is the distance in feet?"))
def distance_feet(dist_feet):
    dist_meters = dist_feet * 0.3048
    return print("The distance in meters is " + str(dist_meters))

distance_feet(dist_feet) 

#Version 2
#Let the user pick a unit
units = str(input("What are the units: ft, mi, m, km?"))
conversion_factors = {'ft':0.3048, 'mi': 1609.34, 'm': 1, 'km':1000}
dist_any = float(input("What is the distance?"))
print(f'The distance is {dist_any * conversion_factors[units]} meters.')

#Version 3
#include yards and inches
conversion_factors['yard'] = 0.9144
conversion_factors['inch'] = 0.0254

#Version 4
new_distance = float(input("What is the distance?"))
starting_units = str(input("What are the starting units?"))


meters = new_distance * conversion_factors[starting_units]
print(f'The distance is {meters} meters')

convert_to = str(input("What units would you like to convert to?"))

distance_converted = meters / conversion_factors[convert_to]
print(f'The converted distance is {distance_converted} {convert_to}.')