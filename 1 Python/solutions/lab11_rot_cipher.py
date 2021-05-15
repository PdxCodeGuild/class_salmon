



def rot13(text):
    ...

    # method 1
    # have two strings - the original and rotated alphabet
    # start output as a blank string
    # iterate over the characters in the input string
        # find the index of the character in the alphabet
        # https://github.com/PdxCodeGuild/class_eagle/blob/main/1%20Python/docs/08%20Strings.md#find-afindb
        # use that index to find the corresponding character in the rotated alphabet
        # add the rotated character to your output
    # return your output

    # method 2
    # have one string - the alphabet
    # start output as a blank string
    # iterate over the characters in the input string
        # find the index of the character in the alphabet
        # https://github.com/PdxCodeGuild/class_eagle/blob/main/1%20Python/docs/08%20Strings.md#find-afindb
        # add 13 to the index
        # use subtraction or modulus to keep the index in a valid range
        # get the letter in the alphabet at that new index
    # add the rotated character to your output
    # return your output

    # method 3
    # make a dictionary where the keys are the original letters
    # and the values are the rotated letters

    # method 4
    # use ord to find the ascii code of a letter
    # add 13 to the ascii code
    # do some arithmetic to put the ascii code in a valid range
    # use chr to turn the ascii code into a character
    # https://github.com/PdxCodeGuild/class_eagle/blob/main/1%20Python/docs/08%20Strings.md#ascii-codes-ord-and-chr



print(rot13('hello')) # uryyb





import string

def rotn(text, rot_amount):
    alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + string.whitespace
    output = ''
    for char in text:
        index = alphabet.find(char)
        if index == -1:
            output += char
        else:
            index += rot_amount
            index %= len(alphabet)
            output += alphabet[index]
    return output
        
print(rotn('Hello World!', 13))
print(rotn(rotn('Hello World!', 13), -13))




encrypted_text = 'UryyBh9BEyq.'
for i in range(26):
    decrypted_text = rotn(encrypted_text, -i)
    if 'Hello' in decrypted_text:
        print('The decrypted text is: ' + decrypted_text)
        print('The rotation amount was ' + str(i))


