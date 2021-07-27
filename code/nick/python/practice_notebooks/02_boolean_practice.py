# Practice 2: Booleans, Comparisons, & Conditionals
# Copy and paste this file into your own "02_booleans.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 02_booleans.py"


# Go Hiking
# Write a function that takes a string indicating energy level and weather

#Ask user their energy level
energy = input("What is your energy level? spry or tired")
#Ask user the weather conditions
weather = input("What are the weather conditions? rainy or sunny")
def go_hiking(energy, weather):
    if energy == 'tired' and weather == 'rainy':
        return False
    elif energy == 'tired' and weather == 'sunny':
        return False
    elif energy == 'spry' and weather == 'rainy':
        return False
    elif energy == 'spry' and weather == 'sunny':
        return True
#Call the function to test it
print(go_hiking(energy, weather))
#right now, everything is returning True. Something not right. 

def test_go_hiking():
    assert go_hiking('tired', 'rainy') == False
    assert go_hiking('tired', 'sunny') == False
    assert go_hiking('spry', 'rainy') == False
    assert go_hiking('spry', 'sunny') == True

#stopped here 25May2021
# Double Digit
# Write a function that returns True if the number is a double digit
#ask the user for an input
'''num = int(input('Hey. I can count digits in a number. Pick any number: '))
def double_digit(num):
    #start a blank counter
    counter = 0
    discard = 0
    #while loop to count digits
    while (num > 0):
        #if number is greater than zero, remove last number
        discard = num.pop()
        #for each iteration add one to the counter
        counter += 1'''
    
#print(double_digit(num))
#something is not right in the print statement
def test_double_digit():
    assert double_digit(5) == False
    assert double_digit(55) == True
    assert double_digit(672) == False
    assert double_digit(-56) == True


# Opposite
# Write a function that takes two integers, `a` and `b`, and returns `True` if one is positive and the other is negative, and return `False` otherwise.

def opposite(a, b):
    ...

def test_opposite():
    assert opposite(10, -1) == True
    assert opposite(2, 3) == False
    assert opposite(-1, -1) == False


# Near 100
# Write a function that returns True if a number within 10 of 100.


def near_100(num):
    ...

def test_near_100():
    assert near_100(50) == False
    assert near_100(99) == True
    assert near_100(105) == True
    assert near_100(115) == False


# Maximum of Three
# Write a function that returns the maximum of 3 parameters.


def maximum_of_three(a, b, c):
    ...

def test_maximum_of_three():
    assert maximum_of_three(5,6,2) == 6
    assert maximum_of_three(-4,3,10) == 10

