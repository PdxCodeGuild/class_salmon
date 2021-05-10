"""
lab 13: rot 13
"""

# start with a blank output string
# loop through every character of the string that the user entered
# find the index of that character in the alphabet
# using that index, find the character in the rotated alphabet
# append that character to the output string
def rot13(text):

    alphabet         = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_rotated = 'nopqrstuvwxyzabcdefghijklm'

    output = ''
    for char in text:
        index = alphabet.find(char)
        output += alphabet_rotated[index]
    return output

def rotn(text, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    for char in text:
        index = alphabet.find(char)
        index += n

        while index >= len(alphabet):
            index -= len(alphabet)

        #if index >= len(alphabet):
        #    index -= len(alphabet)
        output += alphabet[index]
    return output

print(rotn('hello', 2))

# solution using dictionary containing translations
def rot13_v2(text):
    translations = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', }
    output = ''
    for char in text:
        char = char.lower()
        if char in translations.keys():
            output += translations[char]
        else: # handle non-alphabet characters 
            output += char 
    return output

print(rot13_v2('hello'))

# add support for non-letter characters
# use the modulus operator to wrap the index around
def rotn_v2(text, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    for char in text:
        index = alphabet.find(char)
        if index == -1:
            output += char
        else:
            index += n
            index %= len(alphabet)
            output += alphabet[index]
    return output

print(rotn_v2('hello world!', 13))


# convert each char to its ASCII numeric value using ord()
# add offset to normalized ASCII value and wrap around when out of bounds
# convert char back to character using chr()
def rotn_v3(text, offset):
    output = ''
    for char in text:
        index = ord(char)
        if ord('a') <= index <= ord('z'):
            index -= ord('a')
            index += offset
            index %= ord('z') - ord('a') + 1
            output += chr(ord('a')+index)
        elif ord('A') <= index <= ord('Z'):
            index -= ord('A')
            index += offset
            index %= ord('Z') - ord('A') + 1
            output += chr(ord('A') + index)
        else:
            output += char

    print(output)
