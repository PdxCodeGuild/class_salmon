"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 09
Version: 1
Date: 5/25/2021

"""

# import libraries
import os
import re
import math

# Dict for ARI scale.
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
     10: {'ages': '14-15', 'grade_level':    '9th Grade'},
     11: {'ages': '15-16', 'grade_level':   '10th Grade'},
     12: {'ages': '16-17', 'grade_level':   '11th Grade'},
     13: {'ages': '17-18', 'grade_level':   '12th Grade'},
     14: {'ages': '18-22', 'grade_level':      'College'}
}


def calculate_ari(words, characters, sentences):
    global ari_scale
    ari = (4.71 * (characters/words)) + (.5 * (words/sentences)) - 21.43
    print(f"ARI: {ari}; Rounded ARI: {math.ceil(ari)}")
    print(f"Chars: {characters}, Words: {words}, Sentences: {sentences}")
    ari = math.ceil(ari)
    return f"The ARI for this text is {math.ceil(ari)}. This corresponds to the {ari_scale[ari]['grade_level']} level of " \
           f"difficulty that is suitable for an average person {ari_scale[ari]['ages']} years old."


# function for opening and reading a file.
def fread():
    # get filename from user.
    filename = input("Please enter filename: ")

    # get the current working directory and create a complete path to file.
    file_path = os.path.join(os.getcwd(), "lab09", filename)

    # Open file for reading and return error if file doesn't exist.

    try:
        with open(filename, "r+") as file_to_check:
            print("File is ready for use!")
            text = file_to_check.read()

            return calculate_ari(wordcount(text), charactercount(text), sentencecount(text))

    except FileNotFoundError:
        print(f"{filename} does not exist in the current directory!")


def wordcount(text):
    return len(re.findall(r"[a-zA-Z]\w*", text))


def charactercount(text):
    return len(re.findall(r"[A-Za-z]\s*", text))


def sentencecount(text):
    return len(re.findall(r"[A-Z][^\.!?]*[\.!?]", text))



def end():
    print("Thank you for using!")


"""# Trying something new for funsies  -- sort of a command pattern.
menu_options = {
    1: "fread",
    2: "end"
}"""

# Run the program
print("ARI Calculator".center(28, "="))
while True:
    print("Please select from the menu:")
    print("1) Calculate ARI for a file\n2) Exit")
    choice = int(input("Choice: "))
    try:
        if choice == 1:
            print(fread())

        elif choice == 2:
            end()
            break
        else:
            raise ValueError
    except ValueError:
        print("Please enter a valid option!")
