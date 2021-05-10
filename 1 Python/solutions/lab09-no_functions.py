# intro message
print('Welcome to the Distance Converter 5001™!')

# make sure user enters a number
while True:
    try:
        distance = float(input('Enter your distance: '))
        break
    except ValueError as e:
        pass

# make sure user enters a valid unit and standardize
while True:
    units = input('Enter your starting unit: ').lower()
    if units in ['m', 'meter', 'meters']:
        units = 'm'
    elif units in ['mi', 'mile', 'miles']:
        units = 'mi'
    elif units in ['ft', 'foot', 'feet']:
        units = 'ft'
    elif units in ['km', 'kilometer', 'kilometers']:
        units = 'km'
    elif units in ['yd', 'yard', 'yards']:
        units = 'yd'
    elif units in ['in', 'inch', 'inches']:
        units = 'in'
    else:
        units = ''
    if units:
        break

# make sure user enters a valid target unit and standardize
while True:
    target_units = input('What unit would you like to convert to?: ').lower()
    if target_units in ['m', 'meter', 'meters']:
        target_units = 'm'
    elif target_units in ['mi', 'mile', 'miles']:
        target_units = 'mi'
    elif target_units in ['ft', 'feet']:
        target_units = 'ft'
    elif target_units in ['km', 'kilometer', 'kilometers']:
        target_units = 'km'
    elif target_units in ['yd', 'yard', 'yards']:
        target_units = 'yd'
    elif target_units in ['in', 'inch', 'inches']:
        target_units = 'in'
    else:
        target_units = ''
    if target_units:
        break

# determine meters
if units == "mi":
    meters = distance * 1609.34
elif units == "ft":
    meters = distance * 0.3048
elif units == "km":
    meters = distance * 1000
elif units == "m":
    meters = distance * 1
elif units == "yd":
    meters = distance * 0.9144
elif units == "in":
    meters = distance * 0.0254

# determine results
if target_units == "mi":
    result = meters / 1609.34
elif target_units == "ft":
    result = meters / 0.3048
elif target_units == "km":
    result = meters / 1000
elif target_units == "m":
    result = meters / 1
elif target_units == "yd":
    result = meters / 0.9144
elif target_units == "in":
    result = meters / 0.0254

# print results
print(f'''
    Thank you for using the Distance Converter 5001™!
    You converted {distance}{units} to {target_units}.
    That equals {result}{target_units}!
    Remember the Distance Converter 5001™ for all your distance converting needs!
    ''')
    