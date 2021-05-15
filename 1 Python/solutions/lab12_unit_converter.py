units = {'ft' : 0.3048, 'mt' : 1, 'mi' : 1609.34, 'km' : 1000, 'in' : 0.0254, 'yd' : 0.9144 }
distance = int(input("What is the distance?"))
units_inp = input("What are the units?")
units_out = input("What are the output units?")
distance_meters = distance * units[units_inp]
x = distance_meters / units[units_out]
print(x)