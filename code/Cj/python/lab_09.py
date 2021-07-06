import math
import string

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
##'C:\\Users\\Joshua\\Desktop\\stranger_in_a_strange_land.txt'##
##'C:\Users\Joshua\Desktop\stranger_in_a_strange_land.txt'##
#'C:/Users/Joshua/Desktop/stranger_in_a_strange_land.txt'


#file_path = input('Choose a text file to get the reading level of the material by entering a file path:\n ')# User enters own input

file_path = 'C:\\Users\\Joshua\\Desktop\\stranger_in_a_strange_land.txt'

with open(file_path, 'r', encoding='utf-8') as f:
    contents = f.read()


def count_characters(text_file):
    counter = 0
    letters_list = string.ascii_letters
    for char in text_file:
        if char in letters_list:
           counter += 1
        else:
            pass
    return counter


def count_words(text_file):
    OUT = 0
    IN = 1
    word_count = 0
    status = OUT
    for char in range(len(text_file)):
        if (text_file[char] == ' ' or text_file[char] == '\n' or text_file[char] == '\t'):
            status = OUT
        elif status == OUT:
            status = IN
            word_count += 1
    return word_count


def count_sentences(text_file):
    OUT = 0
    IN = 1
    counter = 0
    status = OUT
    letters_list = string.ascii_letters
    for char in range(len(text_file)):
        if (text_file[char] == '.' or text_file[char] == '!' or text_file[char] == '?'):
            if (text_file[char+1] == ' ' or text_file[char+1] == '\n' or text_file[char+1] == '\t'):
                status = OUT
        elif status == OUT and text_file[char] in letters_list:
            status = IN
            counter += 1
    return counter

total_chars = count_characters(contents)
total_words = count_words(contents)
total_sentences = count_sentences(contents)
# print(total_chars, total_words, total_sentences)

ari = math.ceil(((total_chars / total_words) * 4.71) + 0.5 * (total_words / total_sentences) - 21.43)


output = f'The reading level of this material is for age groups: {ari_scale[ari]["ages"]}, and for {ari_scale[ari]["grade_level"]} level '

print(output)
# print(ari_scale[ari])
# ((chars / words) * 4.71) + (total words / total sentences + 5) - 21.43


