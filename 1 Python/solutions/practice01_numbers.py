
# Practice 1: Numbers & Arithmetic
# Copy and paste this file into your own "01_numbers.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 01_numbers.py"

# Is Even
# Write a function returns whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)

def is_even(a):
    return a%2 == 0
    # if a%2 == 0:
    #     return True
    # else:
    #     return False

def test_is_even():
    assert is_even(5) == False
    assert is_even(6) == True


# Ones Digit
# Write a function that returns the ones digit of a number

def ones_digit(num):
    return num%10

def test_ones_digit():
    assert ones_digit(3) == 3
    assert ones_digit(56) == 6
    assert ones_digit(812) == 2


# Tens Digit
# Write a function that returns the tens digit of a number

def tens_digit(num):
    return num//10%10

def test_tens_digit():
    assert tens_digit(3) == 0
    assert tens_digit(56) == 5
    assert tens_digit(812) == 1


# Percentage
# Write a function that takes two integers, a value and a maximum, and returns a string representing the percentage as an integer

def percentage(v, max):
    p = v/max*100
    p = int(p)
    return str(p) + '%'
    # return f'{p}%'

def test_precentage():
    assert percentage(1, 10) == '10%'
    assert percentage(600, 1200) == '50%'
    assert percentage(1, 3) == '33%'




