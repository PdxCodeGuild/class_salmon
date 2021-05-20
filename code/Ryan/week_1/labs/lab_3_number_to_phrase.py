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
        digit_2 = word_number[number_input[1]]
        digit_3 = word_number[number_input[2]]
        output = f"{digit_1} hundred and {digit_2}ty {digit_3}"

    return output


if menu_select == "1":

    print(number_to_word(input("Enter a number: ")))

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
