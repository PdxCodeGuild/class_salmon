# There's 100 cars
cars = 100
# Every car holds 4 people
space_in_a_car = 4
# There are 30 drivers
drivers = 30
# and 90 passengers
passengers = 90
# Every car that doesn't have a driver is not driven
cars_not_driven = cars - drivers
# A driven car has a driver
cars_driven = drivers
# Carpool capacity is based off seats per car, and only if there's a driver
carpool_capacity = cars_driven * space_in_a_car
# What is the average amount of passengers per driven car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# Study Drills
# NameError: The variable 'car_pool_capacity' was not existent at line 7. The correct variable would've been 'carpool_capacity'
# 1) 4.0 is not necessary. The script executes fine without the float (converted to integer), besides you can't have half a person
# 2) n/a
# 3) n/a
# 4) n/a
# 5) n/a
# 6) Output:
# >>> x = 5
# >>> i = 20
# >>> x + i
# 25
# >>> j = x + i
# >>> print(j)
# 25
