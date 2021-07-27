file_name = 'frankenstein.txt'

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

def ARI(file_name):
    with open(file_name, 'r') as f:
        contents = f.read()
        word_count = contents.count(' ')
        sentence_count = contents.count('.') + contents.count('!') + contents.count('?')
        # print("sentences:", sentence_count)
        # print("words: ", word_count)
        char_num = len(contents.replace(" ", ""))
        # print("characters: ", char_num)
        return (4.71 * (char_num / word_count) + .5 * (word_count / sentence_count) - 21.4)

# print("ARI: ", ARI(file_name))

ARI = ARI(file_name)
if ARI % 1 != 0 and ARI % 1 <= .5:
    ARI = round(ARI) + 1
    if ARI > 14:
        ARI = 14
elif ARI % 1 != 0 and ARI % 1 > .5:
    ARI = round(ARI)



print("-----------------------------------------------------\n")
print(f"The ARI for {file_name} is {ARI}")
print(f"This corresponds to a {ari_scale[ARI]['grade_level']} Grade level of difficulty")
print(f"That is suitable for an average person {ari_scale[ARI]['ages']} years old.\n")
print("-----------------------------------------------------")