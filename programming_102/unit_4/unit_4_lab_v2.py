# Create a dictionary of letters, where each letter has a value
base_letters_value = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}


# Examine dictionary
# print(base_letters_value)
# print(type(base_letters_value))
# Every letter has a unique value
# Test for 1 letter and find the value

# letter = "a"
# word = "varmilo"
# Check if the letter is in the dictionary
# print(f"{letter in base_letters_value}")

# Print the value of the letter
# print(base_letters_value.get(letter))

# Assign a value to the number
# letter_value = base_letters_value.get(letter)
# print(letter_value)

# Create a function to add up letter values
def word_value(word):
    # Running total value
    total_value = 0

    # Convert a string into a list of letters
    for w in word:
        # print(w)
        # Look in the dictionary for the value and assign to variable
        value = base_letters_value.get(w)
        # print(value)
        # Add the letter values together
        total_value = total_value + value

    return total_value


# Create a list of words and test the function output against each
list_words = [
    input("Enter the first word: ").lower(),
    input("Enter the second word: ").lower(),
    # "sun",
]

variable_counter = 0

# Loop through the list of words and find the values for each
for words in list_words:
    # print(f"Total letter value of {words} is {word_value(words)}")

    if variable_counter == 0:

        word_1_value = {word_value(words)}

        variable_counter += 1

    elif variable_counter >= 1:

        word_2_value = {word_value(words)}



# print(word_1_value)
# print(word_2_value)

# Compare the results
if word_1_value != word_2_value:
    print(f"{list_words[0]} and {list_words[1]} are not anagrams")

elif word_1_value == word_2_value:
    print(f"'{list_words[0]}' and '{list_words[1]}' are anagrams")

# ------------------------------------------------------------------- #
"""
Version 1

# Import the characters module
import string

# letters = "test"
# print(letters)

# Function to parse the alphabet letters and assign a numeric value
def letter_number(letters):
    alpha_number = {}
    # Start with 0
    number = 0

    # Foreach letter in the list
    for l in letters:
        # Add to dictionary and assign next sequential number
        alpha_number.update({l: number})
        number += 1
    return alpha_number


def sum_numbers(numbers):
    # Start with zero total
    total = 0

    # For each number in the numbers list
    for number in numbers:
        total = total + number

    return total


def total(word):
    start_dict = letter_number(letters)
    print(f" {start_dict}")

    numbers = start_dict.keys()
    new_nums = sum_numbers(numbers)
    print(f"The total of {word} is {new_nums}")
    return new_nums


def find_num_value(word):

    for w in word:

        start_letters = string.ascii_letters
        base_set = letter_number(start_letters)

        # Look at the base set and find the number value of the letter
        #value = letter_number(base_set).keys(w)
        #print(value)

    return

word = "test"
print(find_num_value(word))

start_letters = string.ascii_letters
base_set = letter_number(start_letters)
value = letter_number(base_set)

for v in value:
    print({v})


print(base_set)
print(value)


start_letters = string.ascii_letters
base_set = letter_number(start_letters) 
print(base_set)


# Capture the input of word 1 and convert to numeric value
first_word = input("Enter the first word: ")
letters = first_word
first_word_value = total(first_word)
# print(first_word_value)

# Capture the input of word 2 and convert to numeric value
second_word = input("Enter the second word: ")
letters = second_word
second_word_value = total(second_word)
# print(second_word_value)

if first_word_value != second_word_value:
    print(f"{first_word} and {second_word} are not anagrams")

else:
    print(f"{first_word} and {second_word} are anagrams")

"""
