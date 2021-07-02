name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# Study Drills
# 1) Remove my_
# 2) Write variables that convert inches & pounds to centimeters and kilograms

centimeter_to_inch = 0.39 * int(height)
pound_to_kilogram = 0.45 * int(weight)

print(f"In centimeters, {name} is {centimeter_to_inch} centimeters tall.")
print(f"In kilograms, {name} is {pound_to_kilogram} kilograms heavy.")
