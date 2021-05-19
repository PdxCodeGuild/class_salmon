"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 03
Version: 1
Date: 5/19/2021

"""


# Define function to translate 10s digit.
def translate_number(number):

    # Tens digit
    tens = {
        1: "teen",  # Only for numbers 14 & 16 - 19
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

    # Ones digit
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

    # calculate 10s digit.
    if number == 10:
        tens_digit = 'ten'
    elif 10 < number < 16:
        if number == 11:
            tens_digit = "eleven"
        elif number == 12:
            tens_digit = "twelve"
        elif number == 13:
            tens_digit = "thirteen"
        elif number == 15:
            tens_digit = "fifteen"
    elif number == 0:
        tens_digit = ""
    else:
        tens_digit = tens[number // 10]

    # Calculate 1s digit
    ones_digit = ones[number % 10]

    # Translate the number from digits to string.
    if (10 < number < 16) and number != 14:
        return tens_digit
    elif number < 20:
        return ones_digit + tens_digit
    else:
        return tens_digit + '-' + ones_digit


# get number to convert to phrase
number_to_translate = int(input("Enter an integer from 0 - 99: "))

# Check number is in range
if number_to_translate > 99:
    print("Number entered is out of range.")

# Output translated number.
print(translate_number(number_to_translate))
