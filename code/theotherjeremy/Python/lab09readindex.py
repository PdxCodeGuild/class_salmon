import math
with open('./other/origin.txt', encoding='utf-8') as orig:
    contents = orig.read()

alpha = 'abcdefg[hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

characters_only = ''.join(i for i in contents if i in alpha)


num_of_characters = len(characters_only)
print(f'Number of characters: {num_of_characters}')


words_only = contents.split()
num_of_words = len(words_only)
print(f'Number of words: {num_of_words}')

break1 = contents.count('?')
break2 = contents.count('!')
break3 = contents.count('.')
num_of_sentences = break1 + break2 + break3
print(f'Number of sentences: {num_of_sentences}')


ari = math.ceil((4.71*(num_of_characters/num_of_words)) +
                (.5 * (num_of_words/num_of_sentences)) - 21.43)

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

print(
    f'The ARI for origin.txt is {ari}.  \nThis corresponds to a {ari_scale[ari]["grade_level"]} level of difficulty.  \nThat is suitable for an average person {ari_scale[ari]["ages"]} years old. ')
