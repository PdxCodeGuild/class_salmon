numeral_conversion = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C"
}

input_number = 6

input_number_floor = input_number // 10
input_number_mod = input_number % 10
print(input_number_floor)
print(input_number_mod)

# Roman numeral rules
# A letter can only be repeated 3x
# If 1>= letters are placed after another letter of greater value, add the amount
# VII = 7 (5 + 2 = 7)
# If a letter is placed before another letter of greater value, subtract that amount
# IX = 9 ( 10 – 1 = 9 )

if input_number_mod != 0 and input_number_mod < 4:
    first = numeral_conversion[1] * input_number_mod

if input_number_mod != 0 and input_number_mod >= 4:
    first = 5 - input_number_mod



"""
for n in numerals:

    if ones_digit == 0:
        ones_digit = ""

    elif ones_digit == n:
        ones_digit = numerals[n]

    if tens_digit == n < 4:
        tens_digit = "X" * n

    if tens_digit == n == 4:
        tens_digit = "XL"

    if tens_digit == n >= 5:
        tens_digit = "L"

"""


