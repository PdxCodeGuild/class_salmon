import string
import re
#with open('Gettysburg.txt', 'r') as txt:
   # contents = (txt.read()).lower() 
def ari(txt_file):
    ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st'},
     3: {'ages':   '7-8', 'grade_level':    '2nd'},
     4: {'ages':   '8-9', 'grade_level':    '3rd'},
     5: {'ages':  '9-10', 'grade_level':    '4th'},
     6: {'ages': '10-11', 'grade_level':    '5th'},
     7: {'ages': '11-12', 'grade_level':    '6th'},
     8: {'ages': '12-13', 'grade_level':    '7th'},
     9: {'ages': '13-14', 'grade_level':    '8th'},
    10: {'ages': '14-15', 'grade_level':    '9th'},
    11: {'ages': '15-16', 'grade_level':   '10th'},
    12: {'ages': '16-17', 'grade_level':   '11th'},
    13: {'ages': '17-18', 'grade_level':   '12th'},
    14: {'ages': '18-22', 'grade_level':'College'}
    }
    #with open(txt_file, 'r') as txt:
    #    contents = (txt.read()).lower() 
    contents = txt_file                                                                
    contents = contents.replace('\t', '').replace('\n', '')
    sentences = len((''.join([char if char not in ('!,.,?') else '_&_' for char in contents])).split('_&_'))
    words = len(contents.split(" "))
    chars = len([1 for char in contents if char.isalpha()])
    print(sentences,words,chars)
    ari =int((4.71 * (chars / words)) + (0.5 * (words / sentences)) - 21.43 + 1)
    print (ari)
    if ari > 14 :
        ari = 14
    elif ari <1:
        ari = 1
    return 'The ARI for' + "non" + 'is' + str(ari) + '\nThis corresponds to a ' + ari_scale[ari]['grade_level'] + ' grade level of difficulty\nthat is suitable for an average person ' + ari_scale[ari]['ages'] + ' years old.'
    #return ari
apple = '''Ever since Lincoln wrote it in 1864, this version has been the most often reproduced, notably on the walls of the Lincoln Memorial in Washington. It is named after Colonel Alexander Bliss, stepson of historian George Bancroft. Bancroft asked President Lincoln for a copy to use as a fundraiser for soldiers (see "Bancroft Copy" below). However, because Lincoln wrote on both sides of the paper, the speech could not be reprinted, so Lincoln made another copy at Bliss's request. It is the last known copy written by Lincoln and the only one signed and dated by him. Today it is on display at the Lincoln Room of the White House.

Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.

Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.

But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.

Abraham Lincoln
November 19, 1863'''
print(ari(apple))