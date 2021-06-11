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

installed: 

PyDictionary: https://pypi.org/project/PyDictionary/
RandomWords: https://randomwords.readthedocs.io/en/latest/how_to_use.html
deep-translator: https://pypi.org/project/deep-translator/
easygui: https://github.com/robertlugg/easygui

'''
from random_words import RandomWords
from PyDictionary import PyDictionary
from googletrans import Translator
from deep_translator import GoogleTranslator
import datetime
import easygui as ezgui # idk why I decided to save myself two letters

translator = Translator()
dictionary = PyDictionary()
rw = RandomWords()
word = rw.random_word
x = datetime.datetime.now()

# Intro w/date
date = x.strftime("%x")
day = x.strftime("%A")
print(f"\nHere is your Arabic word for today, {day}, {date}: \n")
ezgui.msgbox(f"\nHere is your Arabic word for today, {day}, {date}: \n", 'Arabic Word of the Day')

# 1 - Generate random word in English
word = rw.random_word() # random English word

# 2 - translate EN word to AR
translated = GoogleTranslator(source='auto', target='ar').translate(text=word)
print(f'{translated[::-1]}\n{word}') # AR written R-L
ezgui.ynbox(f'{translated}\n"{word}"','Know the definition?' ) 

# 3 - definition
definitions = []
definition = dictionary.meaning(word)
for key in definition.keys():
    print(f'\n{key}.')
    for i, meaning in enumerate(definition[key], start=1):
        print(f'{i}.', meaning) # closing parens don't print?
        definitions.append(f'\n{key} {i}. {meaning}')
        # ezgui.msgbox(f'{key}\n{i}. {meaning}') # new card for every def
    print()
    
ezgui.msgbox(definitions, 'Definitions') # wished this looked cleaner, and that each part of speech (noun, verb) was its own card

# # 3a - synonyms
en_syns = dictionary.synonym(word)
print(f'\nEnglish synonyms: {en_syns}\n') 

ar_list_o_syns = []
for kalima in en_syns: # kalima means 'word' in AR
    ar_syn = GoogleTranslator(source='auto', target='ar').translate(text=kalima)
    ar_list_o_syns.append(ar_syn)  
print(f'Arabic synonyms: {ar_list_o_syns}\n') # letters reversed in terminal

synonyms = dict(zip(en_syns, ar_list_o_syns)) # takes a long time to generate
print(synonyms)
print()
ezgui.msgbox(f'{synonyms}','Synonyms', '*')
 

'''
Issues:

Obviously, definitions aren't always perfect

Buttons in GUI aren't functional, except to move forward 

If English word not found in Arabic, word is simply transliterated into AR - 
For example, 'brooks' returned the name 'Brooks' (no other definitions), and was phonetically spelled out in AR بروكس

Several definitions for the English word comes out as only one possible AR word -
For example, 'casts' only returns 'يلقي' meaning 'he throws/casts'

If first line is description, description is listed as a definition - 
For example, 'firmware' printed 'Noun. 1. (computer science)'

Synonyms seem to be off, as well -
For example, one synonym of 'sums' was 'red ink' and 'peanuts' (which gets translated into AR literally - no room for nuance)

If a synonyms has no AR equivalent, prints EN word (but backwards) - 'slue': 'euls'

So far, only nouns and verbs have produced - no adj., adv., etc.

'''


