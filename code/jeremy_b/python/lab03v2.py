"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 03
Version: 2
Date: 5/27/2021

This version is based on feedback from Pete and John.

"""

hundreds = {
    0: "",
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

# Tens digit
tens = {
    0: "",
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
special_tens = {
    1: "eleven",
    2: "twelve",
    3: "thirteen",
    5: "fifteen",
    8: "eighteen"
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


# get number to convert to phrase
number_to_translate = input("Enter an integer from 0 - 999: ")

# Fill to always get 3 digits.
if len(number_to_translate) < 3:
    number_to_translate = number_to_translate.zfill(3)

# Convert number to string of ints
number_to_translate = [int(number) for number in number_to_translate]  # Some more list comprehension

# Perform the translation
# hundreds digit
hundreds_digit = hundreds[number_to_translate[0]]

# tens digit
if number_to_translate[1] == 1 and number_to_translate[2] in [1, 2, 3, 5, 8]:
    tens_digit = special_tens[number_to_translate[2]]
else:
    tens_digit = tens[number_to_translate[1]]

# ones digit
if number_to_translate[1] == 1 and number_to_translate[2] in [1, 2, 3, 5, 8]:
    ones_digit = ""
else:
    ones_digit = ones[number_to_translate[2]]

# print the final value:
if number_to_translate[1] == 1 and number_to_translate[2] in [1, 2, 3, 5, 8]:
    print(f"{hundreds_digit} {tens_digit}")
elif number_to_translate[1] == 1 and number_to_translate[2] not in [1, 2, 3, 5, 8]:
    print(f"{hundreds_digit} {ones_digit}{tens_digit}")
else:
    print(f"{hundreds_digit} {tens_digit}-{ones_digit}")
