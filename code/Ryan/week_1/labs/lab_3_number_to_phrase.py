# Problem: Convert a given number into the English representation


number_input = "0"

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


#print(word_number[hundred == True])

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
# Try if statements to concantenate words
final_word = []

if len(number_input) == 3:
    digit_1 = word_number[number_input[0]]
    digit_2 = word_number[number_input[1]]
    digit_3 = word_number[number_input[2]]
    print(f"{digit_1} hundred and {digit_2}ty {digit_3}")

elif len(number_input) == 2:
    digit_1 = word_number[number_input[0]]
    digit_2 = word_number[number_input[1]]
    print(f"{digit_1}ty {digit_2}")

elif len(number_input) == 1:
    digit_1 = word_number[number_input[0]]
    print(digit_1)


