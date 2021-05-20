numeral_conversion = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C"
}

input_number = int(input("Enter a number: "))

input_number_ceiling = input_number // 100
input_number_floor = input_number // 10
input_number_mod = input_number % 10
print(input_number_floor)
print(input_number_mod)

final_output = []

#------------------------------- First Digit -------------------------------#
# If modulus of first digit is 0, do nothing
if input_number_mod:

    # Is the modulus a 9?
    # If so, assign "one less than 10"
    if input_number_mod == 9:
        final_output.append(numeral_conversion[1] + numeral_conversion[10])

    # Is the modulus a 4?
    # If yes, assign "one less than 5"
    elif input_number_mod == 4:
        final_output.append(numeral_conversion[1] + numeral_conversion[5])

    # Can the current modulus be divided by 5?
    # If yes, call the value of 5
    elif input_number_mod // 5:
        # Remove the remainder
        input_number_mod = input_number_mod - 5
        # Add the remaining "i"
        count_i = "I" * input_number_mod
        final_output.append(numeral_conversion[5]+count_i)

    # What if the modulus can't be divided by 5?
    # Print the "i"s
    elif not input_number_mod // 5:
        count_i = "I" * input_number_mod
        final_output.append(count_i)

#------------------------------- Second Digit -------------------------------#

# Up to 40, numbers will be assigned an "X" for each modulus
if input_number_floor < 4:
    final_output.append(numeral_conversion[10] * input_number_floor)

# Any numbers in the 40's range have XL prefix
if input_number_floor == 4:
    final_output.append(numeral_conversion[10] + numeral_conversion[50])

# Any numbers above 50 have a "L" first
# Following "X"s  are decided by the remaining floor
if 9 > input_number_floor >= 5:
    count_x = numeral_conversion[10] * (input_number_floor - 5)
    final_output.append(numeral_conversion[50] + count_x)

# Any numbers in the 90's range have XC prefix
if input_number_floor == 9:
    final_output.append(numeral_conversion[10] + numeral_conversion[100])

#------------------------------- Third Digit -------------------------------#
# Any numbers in the 90's range have XC prefix
if input_number_floor >= 10:
    final_output.append(numeral_conversion[100])

final_output.reverse()
final_output_string = "".join(final_output)
print(final_output_string)

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


