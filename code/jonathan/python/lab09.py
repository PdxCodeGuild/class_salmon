import math
ari_scale = {
    1: {'ages': '5-6', 'grade_level': 'Kindergarten'},
    2: {'ages': '6-7', 'grade_level': '1st Grade'},
    3: {'ages': '7-8', 'grade_level': '2nd Grade'},
    4: {'ages': '8-9', 'grade_level': '3rd Grade'},
    5: {'ages': '9-10', 'grade_level': '4th Grade'},
    6: {'ages': '10-11', 'grade_level': '5th Grade'},
    7: {'ages': '11-12', 'grade_level': '6th Grade'},
    8: {'ages': '12-13', 'grade_level': '7th Grade'},
    9: {'ages': '13-14', 'grade_level': '8th Grade'},
    10: {'ages': '14-15', 'grade_level': '9th Grade'},
    11: {'ages': '15-16', 'grade_level': '10th Grade'},
    12: {'ages': '16-17', 'grade_level': '11th Grade'},
    13: {'ages': '17-18', 'grade_level': '12th Grade'},
    14: {'ages': '18-22', 'grade_level': 'College'}
}
# opens file
text = open('yourfilehere.txt', 'r', encoding='utf-8')
# saving the filename
filename = text.name
# turns file contents into a string
text_data = text.read()
# counts the number of words in the file
list_of_words = text_data.split()
# convert list into an integer
num_words_in_text = len(list_of_words)
# counts the number of periods in the file
periods_in_text = text_data.count('.')
# counts the number of exclamation in the file
exclamation_in_text = text_data.count('!')
# counts the number of question marks in the file
questions_in_text = text_data.count('?')
# combining the above three values to get an approximate number of sentences in the file
sentences_in_text = periods_in_text + exclamation_in_text + questions_in_text
sentences_in_text = int(sentences_in_text)
# remove spaces from the text
characters_in_text = text_data.replace(" ", "")
# finds the number of characters in the file
characters_in_text = len(characters_in_text)
# cast into an integer
characters_in_text = int(characters_in_text)
# ari formula
ari = 4.71 * (characters_in_text/num_words_in_text) + 0.5 * (num_words_in_text/sentences_in_text) - 21.43
# cast into a float
ari_float = float(ari)
# ceiling to round up to nearest integar
ari_int = math.ceil(ari_float)
# for cases where it is over 14
if ari_int > 14:
    ari_int = 14
# accessing grade level inside nested dictionary
grade_level = ari_scale[ari_int]['grade_level']
# accessing ages inside nested dictionary
age = ari_scale[ari_int]['ages']
# close loaded text
text.close()

print(f"""The ARI for {filename} is {ari_int}. This corresponds to 
a {grade_level} grade level of difficulty that is suitable for an 
average person {age} years old.""")