# Problem: Convert a given number into the English representation

menu_select = (input(f"""
Welcome to numbers and words

Would you like to convert a number to:

1) Word version

2) Roman Numerals 

3) Time

q) Quit

Make a choice by number: """))
word_number = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}

tens_word = {
    "10": "Ten",
    "11": "Eleven",
    "12": "Twelve",
    "13": "Thirteen",
    "15": "Fifteen",
    "20": "Twenty",
    "30": "Thirty",
    "50": "Fifty"
}

def second_digit(number):
    number_input = number

    # Check for special words first
    for w in tens_word:
        if number_input == w:
            print(tens_word[w])
            exit()

        else:
            continue

    # If statements to concatenate words
    if number_input[0] == "1":
        output = word_number[number_input[1]] + "teen"

    elif number_input[0] == "2":
        output = "Twenty" + " " + word_number[number_input[1]]

    elif number_input[0] == "3":
        output = "Thirty" + " " + word_number[number_input[1]]

    elif number_input[0] == "5":
        output = "Fifty" + " " + word_number[number_input[1]]

    else:
        output = word_number[number_input[0]] + "ty" + " " + word_number[number_input[1]]

    return output

def number_to_word(number):
    number_input = number
    # print(number_input)

    # Use for numbers < 10
    for w in word_number:
        if number_input == w:
            output = word_number[w]

        else:
            continue

    # If number is 2 digits long
    if len(number_input) == 2:
        print(second_digit(number_input))

    # If number is 3 digits long
    if len(number_input) == 3:
        digit_1 = word_number[number_input[0]]

        if word_number[number_input[1]] == "Zero":
            digit_2 = ""
        elif word_number[number_input[1]] != "Zero":
            digit_2 = f"and {word_number[number_input[1]]}ty"

        if word_number[number_input[2]] == "Zero":
            digit_3 = ""
        elif word_number[number_input[2]] != "Zero":
            digit_3 = f" {word_number[number_input[2]]}"

        output = f"{digit_1} hundred {digit_2}{digit_3}"

    return output

def number_to_numeral(number):
    numeral_conversion = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C"
    }

    input_number = number

    input_number_ceiling = input_number // 100
    input_number_floor = input_number // 10
    input_number_mod = input_number % 10
    #print(input_number_floor)
    #print(input_number_mod)

    final_output = []

    # ------------------------------- First Digit -------------------------------#
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
            final_output.append(numeral_conversion[5] + count_i)

        # What if the modulus can't be divided by 5?
        # Print the "i"s
        elif not input_number_mod // 5:
            count_i = "I" * input_number_mod
            final_output.append(count_i)

    # ------------------------------- Second Digit -------------------------------#

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

    # ------------------------------- Third Digit -------------------------------#
    # Any numbers in the 90's range have XC prefix
    if input_number_floor >= 10:
        final_output.append(numeral_conversion[100])

    final_output.reverse()
    final_output_string = "".join(final_output)
    #print(final_output_string)

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
    return final_output_string


if menu_select == "1":

    print(number_to_word(input("Enter a number: ")))

if menu_select == "2":

    print(number_to_numeral(int(input("Enter a number: "))))

else:
    exit()

# ---------------------- Tried and failed ideas ---------------------- #
# Function to separate numbers
"""
def separate_digits(number_input):
    # Separate digits
    # number_input = "67"
    # print(number_input[0], number_input[1])
    # Make a list of individual digits
    i_digits = []

    for digit in number_input:
        i_digit = digit[0]
        # print(i_digit)
        # Add each digit to list
        i_digits += i_digit

    return i_digits


print(separate_digits(number_input))
numbers_list = separate_digits(number_input)
print(numbers_list)

hundred = len(number_input) >= 3
"""

# print(word_number[hundred == True])

# print(word_number)
# print("6" in word_number)

"""
# Add "ty" if theres more that 2 digits
if len(numbers_list) >= 2:
    # print("ty")
    suffix = "ty"

# Convert the number to word
for number in numbers_list:

    if number in word_number:
        # print(word_number[number])
        prefix = word_number[number]

    print(f"{prefix}{suffix}")
"""

"""
    elif len(number_input) == 1:
        digit_1 = word_number[number_input[0]]
        output = digit_1
"""
