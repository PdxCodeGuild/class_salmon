"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 03
Version: 1
Date: 5/19/2021

"""


# define function to translate 100s digit
def translate_hundreds_digit(number):
    # Hundreds digit
    hundreds = {
        1: "one hundred",
        2: "two hundred",
        3: "three Hundred",
        4: "four hundred",
        5: "five hundred",
        6: "six hundred",
        7: "seven hundred",
        8: "eight hundred",
        9: "nine hundred"
    }
    return hundreds[number]


# Define function to translate 10s digit.
def translate_tens_digit(number):

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
    return tens[number]


def translate_ones_digit(number):
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
        0: "zero"
    }

    return ones[number]


def special_tens_digit(number):
    # Get rid of hundreds digit if it exists.
    if len(number) == 3:
        number.pop(0)

    # calculate 10s digit.
    if number[0] == 1 and number[1] == 0:
        tens_digit = 'ten'
    elif number[0] == 1 and number[1] in [1, 2, 3, 5]:
        if number[1] == 1:
            tens_digit = "eleven"
        elif number[1] == 2:
            tens_digit = "twelve"
        elif number[1] == 3:
            tens_digit = "thirteen"
        elif number[1] == 5:
            tens_digit = "fifteen"
    else:
        tens_digit = translate_tens_digit(number)

    return tens_digit


# get number to convert to phrase
number_to_translate = input("Enter an integer from 0 - 999: ")

# Convert number to string of ints
number_to_translate = [int(number) for number in number_to_translate]  # Some more list comprehension
if len(number_to_translate) == 1:
    print(translate_ones_digit(number_to_translate[0]))

elif len(number_to_translate) == 2 and (number_to_translate[0] == 1 and number_to_translate[1] in [0, 1, 2, 3, 5]):
    print(special_tens_digit(number_to_translate))

elif len(number_to_translate) == 2 and (number_to_translate[0] == 1 and number_to_translate[1] not in [0, 1, 2, 3, 5]):
    print(f"{translate_ones_digit(number_to_translate[1])}{translate_tens_digit(number_to_translate[0])}")

elif (len(number_to_translate) == 3) and (number_to_translate[0] == 1 and number_to_translate[1] in [0, 1, 2, 3, 5]):
    print(f"{translate_hundreds_digit(number_to_translate[0])} {special_tens_digit(number_to_translate)}")

elif len(number_to_translate) == 2 and (number_to_translate[0] == 1 and number_to_translate[1] not in [0, 1, 2, 3, 5]):
    print(f"{translate_hundreds_digit(number_to_translate[0])} {translate_ones_digit(number_to_translate[2])}"
          f"{translate_tens_digit(number_to_translate[1])}")

else:
    print(f"{translate_hundreds_digit(number_to_translate[0])} {translate_tens_digit(number_to_translate[1])}-"
          f"{translate_ones_digit(number_to_translate[2])}")
