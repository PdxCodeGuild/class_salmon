import math

#the goal of this exercise is to determine document readability
#ask the user for the name of their text
title = input('what is the name of your text?')
#you could ask for the directory name but I will not here
#read the contents of the file
#testing this by adding a text file to my repo folder (absolute path)
with open('some.txt', 'r') as f:
    contents = f.read()
    #define variables from the ARI formula
    #start tallying the sentences, characters, words
    sentences = contents.count('.')
    #.strip() would not work in the characters_list, used replace() instead
    characters_list = len(contents.replace(' ', ''))
#I do not really know how to count the words without doing this from a list...
#make a list? of the words
    words_list = list(contents.split(' '))
    words = 0
    for i in words_list:
        words += 1
    #words = words_list.count(words_list[:])
#check variables with print functions
#There are 21 words in my test file
#there are 3 sentences in my test file
#there are 110 characters, including spaces. To exclude spaces, remove them and put in list.
print(words)#this was wrong (cannot divide by zero in ARI function)
print(sentences)
print(characters_list)

#Instructions say always round up. Not sure. I found the .ceil method in the math library, I think does this.
ARI = 4.71 *(characters_list/words) + 0.5 * (words/sentences)-21.43
ARI_ceiling = math.ceil(ARI)
print(f"The ARI is with decimal places is {ARI}.")
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
#get a list of keys for the dict
#keys = ari_scale.keys()
#print(keys)
#extract a grade level
ages_grade = ari_scale[ARI_ceiling]
grade_level = ages_grade['grade_level']
age_group = ages_grade['ages']
#print(grade_level)
#make an output sentence function
print(f"The ARI for {title} is {ARI_ceiling}. \
This corresponds to a {grade_level} level of difficulty that is suitable \
for an average person {age_group} years old.")

