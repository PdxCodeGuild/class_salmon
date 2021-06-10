''' ***MINI CAPSTONE*** '''
'''
AR Word of the Day
'''
'''
Steps:

1. import random English word

2. translate to Arabic

3. give user meaning in English 

*ideally, give user meaning in English and AR, plus additional AR synonyms/similar, plus English transliteration; ideally ideally give sentence example

'''
'''
installed: 

PyDictionary: https://pypi.org/project/PyDictionary/
RandomWords: https://randomwords.readthedocs.io/en/latest/how_to_use.html
deep-translator: https://pypi.org/project/deep-translator/
arabicscript: https://pypi.org/project/arabicscript/ (not for this lab, only tells what position each letter should be in, and booleans)

'''

from random_words import RandomWords
from PyDictionary import PyDictionary
from googletrans import Translator
from deep_translator import GoogleTranslator
# from pytime import PyTime

translator = Translator()
dictionary = PyDictionary()
rw = RandomWords()
word = rw.random_word
# pytime = PyTime()
# date = date.date

print("\nHere is your Arabic word for today, {date}: \n")

# 1 - Generate random word in English
word = rw.random_word() # random English word

'''
Issues:

Obviously, definitions aren't always perfect

If English word not found in Arabic, word is simply transliterated into AR - 
For example, 'brooks' returned the name 'Brooks' (no other definitions), and was phonetically spelled out in AR بروكس

Several definitions for the English word comes out as only one possible AR word -
For example, 'casts' only returns 'يلقي' meaning 'he throws/casts'

Synonyms seem to be off, as well -
For example, one synonym of 'sums' was 'red ink' and 'peanuts' (which gets translated into AR literally - no room for nuance)

'''

# 2 - translate EN word to AR
translated = GoogleTranslator(source='auto', target='ar').translate(text=word)
print(translated[::-1]) # correct direction R-L, all letters in isolated form
print(f'"{word}"\n')

# 3 - definition
definition = dictionary.meaning(word)
for key in definition.keys():
    print(f'{key}.')
    for i, meaning in enumerate(definition[key], start=1):
        print(f'{i}.', meaning)
    print()


# 3a - synonyms
synonyms = dictionary.synonym(word)
print (f'\nEnglish synonyms: {synonyms}\n') 
ar_list_o_syns = []
for kalima in synonyms: # kalima means 'word' in AR
    ar_syn = GoogleTranslator(source='auto', target='ar').translate(text=kalima)
    ar_list_o_syns.append(ar_syn)

print(f'Arabic synonyms: {ar_list_o_syns}\n')


# print('مرحبا')


# pytime.before('2015.5.17', '2years 3mon 23week 3d 2hr')     # 2years 3months 23weeks 3days 2hours before 2015.5.17
# datetime.datetime(2012, 9, 5, 22, 0)

# pytime.after(pytime.tomorrow('15.5.17'), '23month3dy29minu')   # 23months 3days 29minutes after 2015-5-17's next day
# datetime.datetime(2017, 4, 21, 0, 29)
# Parse nonregular datetime string to datetime:

# pytime.parse('April 3rd 2015')
# datetime.date(2015, 4, 3)
# pytime.parse('Oct, 1st. 2015')
# datetime.date(2015, 10, 1)
# pytime.parse('NOV21th2015')
# datetime.date(2015, 11, 21)
