distance = float(input("What is the distance? "))
unit = input("What are the units? ")
convert_to = input("What unit do you want to convert to? ")

measures = {'ft': .3048, 'mi': 1609.34, 'm': 1, 'km': 1000, 'yard': .9144, 'inch': .0254}
conversions = {'ft': 1 / .3048, 'mi': 1 / 1609.34, 'm': 1, 'km': 1 / 1000}

meters = round(measures[unit] * distance, 4)
print(f"{int(distance)} {unit} is {round(conversions[convert_to] * meters, 2)} {convert_to}.")