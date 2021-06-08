''' ***MINI CAPSTONE*** '''

'''
Modules installed:

pytz
Flask
nltk: https://github.com/ahmednabil950/Arabic_Parser_NLTK
adawat
transliterate: https://pypi.org/project/transliterate/
romanize3: https://pypi.org/project/romanize3/
franco-arabic-transliterator [ERROR: not installed]: https://github.com/AMR-KELEG/Franco-Arabic-Transliterator
fuzzywuzzy: https://github.com/seatgeek/fuzzywuzzy/blob/master/README.rst
lang-trans: https://pypi.org/project/lang-trans/
translate
Translator: https://github.com/OmarEinea/TranslateToArabic
selenium
pytest: https://pythonrepo.com/repo/nidhaloff-deep-translator-python-miscellaneous
-U textblob: https://kanoki.org/2019/11/06/python-detect-and-translate-language/
googletrans: https://www.thepythoncode.com/article/translate-text-in-python
'''

from transliterate import translit, get_available_language_codes

text = "Lorem ipsum dolor sit amet"
print(translit(text, 'el'))

from translate import Translator
translator= Translator(from_lang="english",to_lang="arabic")
translation = translator.translate("Hello")
print(translation[::-1]) # prints letters separately, but in correct order


# from Translator import Translator

# tr = Translator()

# text = input("Type Something: ")
# print(tr.translate(text))

# from textblob import TextBlob

# en_blob.translate(to='ar')

# print(translator.translate(u'التعلم الآلي هو موضوع مثير للاهتمام للتعلم', dest='en'))

''' ***FINAL CAPSTONE*** '''

'''
*language = AR (easier) or HEB (harder)

1. user searches for Arabic word using ascii letters and/or Arabic numerals *OR* user searches for Arabic word using Arabic letters

1a. detect if characters are AR or PER

2. convert characters into Arabic (transliterate)

3. output is list of possible words in Arabic that user is trying to find the definition/spelling/transliteration for; displays all three

3. by columns
    -possible transliterations
    -with vowels/7arikaat
    -EN translits
    -root
    -part of speech (noun, verb, etc.)
    -meaning and characteristics (fem. sg.,acc. indef., etc.)
'''

