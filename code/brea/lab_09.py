import string, math


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

with open('C:\\Users\\CJ\\Documents\\book\\tell_tale_heart.txt', 'r', encoding='utf-8') as file_name:
    contents = file_name.read()



def character_counter(contents):
    characters = 0
    letters = string.ascii_letters
    for item in contents:
        if item in letters: 
            characters += 1
    return characters



def word_counter(contents):
    contents = contents.replace('  ', ' ')
    words = contents.split(' ')
    return len(words)



def sentence_counter(contents):  
    sentences = 0
    for item in contents:
       if item == '.' or item == '!' or item == '?':
           sentences += 1
    return sentences


characters = character_counter(contents)
words = word_counter(contents)
sentences = sentence_counter(contents)

ari = math.ceil(4.71 * (characters/words) + 0.5 * (words/sentences) - 21.43)

output = f'The ARI for the Tell Tale Heart by Edgar Allan Poe is: {ari} and suitable for an age group of: {ari_scale[ari]["ages"]} in the {ari_scale[ari]["grade_level"]}'
print(output)