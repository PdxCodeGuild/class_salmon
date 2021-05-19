"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 03
Version: 1
Date: 5/19/2021

"""


# Define function to translate 10s digit.
def get_tens_digit(digit):
    tens = {
        1: "teen",
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety",
        0: ""
    }
    return tens[digit]


# Define function to translate 1s digit.
def get_ones_digit(digit):
    ones = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        0: ""
    }

    return ones[digit]


# get number to convert to phrase
number = int(input("Enter an integer from 0 - 99: "))

# Check number is in range
if number > 99:
    print("Number entered is out of range.")

# Output translated number.
print(f"{get_tens_digit(number//10)}-{get_ones_digit(number%10)}")
