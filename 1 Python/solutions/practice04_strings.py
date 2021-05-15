




# Practice 4: Strings
# Copy and paste this file into your own "04_strings.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 04_strings.py"

# Loud Text ====================================================================
# Capitalize text and insert dashes between each letter

def loud_text(text):
    # upper, split, join
    
    text = text.upper()
    # text = list(text)
    return '-'.join(text)

def test_loud_test():
    assert loud_text('hello') == 'H-E-L-L-O'
    assert loud_text('this is loud text') == 'T-H-I-S- -I-S- -L-O-U-D- -T-E-X-T'



# Double Letters
# Return a string with the letters doubled

def double_letters(word):
    output = ''
    for char in word:
        output += char * 2
        print(output)
    return output

def test_double_letters():
    assert double_letters('hello') == 'hheelllloo'

# Count Letter
# Count the number of letter occurances in a string

def count_letter(letter, word):

    # return word.count(letter)

    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count


def test_count_letter():
    assert count_letter('i', 'antidisestablishmentterianism') == 5
    assert count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis') == 2


# Latest Letter
# Return the letter that appears the latest in the english alphabet.

def latest_letter(word):

    # convert the string into a list of characters
    word = list(word)
    # sort the list of characters
    word.sort()
    # return the last element

    # len is 4
    #               0         1         2        3
    # fruits = ['apples', 'bananas', 'pears', 'kiwi']
    last_index = len(word)-1
    return word[last_index]


def test_latest_letter():
    assert latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis') == 'v'


# Count Hi
# Write a function that returns the number of occurances of 'hi' in a given string.

def count_hi(text):
  ...

def test_count_hi():
    assert count_hi('hihi') == 2
    assert count_hi('hello hi llama hill') == 2






# Snake Case
# Write a function that converts text to snake case (all lowercase, underscores for spaces, no special characters).

import string

def remove_punctuation(text):
    # remove all punctuation
    for llama in text:
        if llama in string.punctuation:
            text = text.replace(llama, '')

    # for punc_char in string.punctuation:
    #     text = text.replace(punc_char, '')

    # output = ''
    # for char in text:
    #     if char not in string.punctuation:
    #         output += char
    # text = output

    return text


def snake_case(text):
    text = text.lower()

    text = remove_punctuation(text)
    


    text = text.replace(' ', '_')

    return text

# print(snake_case('Hello World!'))

# import string
# print(string.ascii_lowercase) # 'abcdefghijklmnopqrstuvwxyz'
# print(string.punctuation) # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'


def test_snake_case(text):
    assert snake_case('Hello World!') ==  'hello_world'
    assert snake_case('This is another example.') == 'this_is_another_example'






# Camel Case
# Write a function that converts text to camel case (no spaces, no special characters, leading capitals except the first).

def camel_case(text):

    text = remove_punctuation(text)

    text = text.split(' ')
    # text = text.replace(' ', '')
    text[0] = text[0].lower()
    for i in range(1, len(text)):
        text[i] = text[i].title()
    # for word in text:
    #     word = word.lower()
    text = ''.join(text)
    print(text)


# print(camel_case('Hello beauTiful WORld!')) # helloBeautifulWorld



# this_is_snake_case
# thisIsCamelCase
# ThisIsTitleCaseOrPascalCase
# THIS_IS_SCREAM_CASE



def test_camel_case():
    assert camel_case('Hello World!') == 'helloWorld'
    assert camel_case('This is another example.') == 'thisIsAnotherExample'

## Alternating Case
# Write a function that converts text to alternating case.

def alternating_case(text):
    ...

def test_alternating_case():
    assert alternating_case('Hello World!') ==  'HeLlO WoRlD!'
    assert alternating_case('This is another example.') == 'ThIs iS AnOtHeR ExAmPle.'





# Scramble Letters
# Write a function `scramble_letters` to scramble the internal letters of words, but keep first and last letter the same.
# https://www.douglastwitchell.com/scrambled_words.php
def scramble_letters(text):
    

    # split text into a list of words ['hello', 'world']
    words = text.split(' ')
    # print(words)

    output = []

    # iterate over the words
    for word in words:
        # for i in range(1, len(word)-1):
        # print(word[1:len(word)-1])

        # take the internal letters out
        mixed_list = list(word[1:len(word)-1])
        random.shuffle(mixed_list)
        mixed_list.insert(0, word[0])
        mixed_list.append(word[len(word)-1])

        output.append(''.join(mixed_list))
        # shuffle them
        # put the word back together
    # put the text back together
    return ' '.join(output)
    
# print(scramble_letters('hello world kerfuffle embiggened')) # hlelo wlrod
# print(scramble_letters('this is hard to read')) # tihs is hrad to raed
# print(scramble_letters('droop here most learnedly delivered adr ‘widow dido’ said as midnight fated mated dryden’s version 470 makest a blemish but that no use of milan antonio i myself you speak the king stephano 225 for i 2 scene iii 3 17 prospero master and expenses including obsolete old cock a refund if it can he be relieved by the construction seems to your ways open eyed with the dropsy drown their noses as in the project gutenberg tm license and rotten carcass of noises 130 my child hanmer 96 sir mark me and that would i have bloody thoughts pros'))




# Truncate Text
# Write a function that takes a string and an integer representing a character limit. If the input string is less than the character limit, return the original string. If the string exeeds the character limit, truncate it and add '...'

def truncate_text(text, character_limit):
    if len(text) > character_limit:
        text = text[:character_limit] + '...'
    return text

# print(truncate_text('hello!', 10)) # hello!
# print(truncate_text('hello world! the sun is bright', 10)) # hello wor...
# print(truncate_text('hello world! the sun is bright', 12)) # hello world!...


# Wrap Text
# insert newlines at the correct points within a string

def wrap_text(text, character_limit):
    line_count = len(text) // character_limit + 1
    print(line_count)
    output = ''
    for i in range(0, len(text)):
        if i%character_limit == 0:
            # i is 10, 20, 30
            # when i is 10, we want the substring of text from 0 to 10
            # when i is 20, we want the substring of text from 10 to 20
            # when i is 30, we want the substring of text from 20 to 30
            # print(f'insert new line at index {i}')
            output += text[i:i+character_limit] + '\n'
            # output += text[:i] + '\\n' + text[i:]
    output = output[:len(output)-1] # remove the last character
    # print(output)
    return output

# hello worl\nd! the sun\n is very b\nright
print(wrap_text('hello world! the sun is very bright', 10)) 








# for i in range(10): # 0 1 2 ... 9
# for i in range(5, 10) # 5 6 ... 9
# for i in range(5, 10, 2) # 5 7 9
# for i in range(10, 4, -2): # 10 8 6


# Pretty Numbers
# Convert an integer into a pretty string with commas `12345678` to `12,345,678`

def pretty_number(num):

    # go from the back to the front
    # insert a comma every third character

    # convert our int into a list of single-character strings
    num = str(num)
    num = list(num)
    pretty_number = []
    counter = 0
    # loop in reverse (i will go 8, 7, 6, 5, ... 2, 1, 0)
    for i in range(len(num)-1, -1, -1):
        # append the number to our output
        pretty_number.append(num[i])
        # increment our counter
        counter += 1
        # if we've gone over 3 numbers and we're not on the last iteration
        if counter == 3 and i != 0:
            # append a comma
            pretty_number.append(',')
            # reset our counter
            counter = 0
    # reverse it
    pretty_number.reverse()
    # join it
    pretty_number = ''.join(pretty_number)

    # KLUGE
    # if pretty_number[0] == ',':
    #     pretty_number = pretty_number[1:]

    return pretty_number

# https://stackoverflow.com/questions/1823058/how-to-print-number-with-commas-as-thousands-separators
# def pretty_number(num):
#     return f'{num:,}'

# print(pretty_number(1))
# print(pretty_number(12))
# print(pretty_number(123))
# print(pretty_number(1234))
# print(pretty_number(12345))
# print(pretty_number(123456))
# print(pretty_number(1234567))
# print(pretty_number(1234593874509238475203489)) # 12,345,678
# print(pretty_number(12345678)) # 12,345,678
# print(pretty_number(5721)) # 5,721
# print(pretty_number(10)) # 10




# Pretty Bytes
# Convert a number of bytes `1567123` into a pretty form `1.5 mb`. The `round` function can take two parameters, the number and the number of decimal places to round to `print(round(1.2345, 2))` will print `1.23`.

def pretty_bytes(bytes):
    ...
# print(pretty_bytes(200)) # 200 b
# print(pretty_bytes(1567123)) # 1.5 mb
# print(pretty_bytes(7321000000)) # 7.32 gb 


# Palindrome
# A palindrome is a word that's the same forwards or backwards, e.g. racecar. Another way to think of it is as a word that's equal to its own reverse. Write a function `check_palindrome(word)` which takes a string, and returns True if the string's a palindrome, or False if it's not.


def check_palindrome(word):
    return word == word[::-1]

    word = list(word)
    reverse_word = word.copy()
    reverse_word.reverse()
    if word == reverse_word:
        return True
    else:
        return False
    
# print(check_palindrome('racecar')) # True
# print(check_palindrome('palindrome')) # False
# print(check_palindrome('tacocat')) # True
# print(check_palindrome('noon')) # True

# Anagram
# Two words are anagrams of eachother if the letters of one can be rearranged to fit the other. e.g. `anagram` and `nag a ram`. Write another function `check_anagram(word1, word2)` that takes two strings as parameters and returns True if they're anagrams of eachother, False if they're not. The procedure for comparing the two strings is as follow:
# 1. Convert each word to lower case (`lower`)
# 2. Remove all the spaces from each word (`replace`)
# 3. Sort the letters of each word (`sorted`)
# 4. Check if the two are equal

def check_anagram(word1, word2):
    ...
# print(check_anagram('anagram', 'nag a ram')) # True
# print(check_anagram('sheep', 'goat')) # False












