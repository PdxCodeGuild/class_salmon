# Lab 9: Compute Automated Readability Index

import string

with open('Alice_in_Wonderland.txt', encoding='utf-8') as f:
    contents = f.read()

def characters(contents):
    char_count = 0
    for char in contents:
        if char in string.printable:
            char_count += 1
    return char_count

def words(contents):
    word_count = contents.split()
    return len(word_count)

def sentences(contents):
    sentence_count = 0
    for char in contents:
        if char == '.' or char == '?' or char == '!':
            sentence_count += 1
    return sentence_count
 
characters = characters(contents)
words = words(contents)
sentences = sentences(contents)
f = 'Alice_in_Wonderland.txt'

ari = round(4.71 * (characters/words) + 0.5 * (words/sentences) - 21.43)

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

grade = ari_scale[ari]['grade_level']
age = ari_scale[ari]['ages']

print(f'The ARI for {f} is {ari}\nThis corresponds to a(n) {grade} Grade level of difficulty that is suitable for an average person {age} years old.')
