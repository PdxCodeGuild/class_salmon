


import string
import random

def random_characters(length, alphabet):
    # start with a blank string
    output = ''
    # loop 'length' number of times
    for i in range(length):
        # every iteration, choose a random character out of our alphabet
        char = random.choice(alphabet)
        # add the character to our output string
        output += char
    # return output string
    return output

# print(random_characters(5, string.ascii_lowercase)) # utecq


def random_password(n_lowercase, n_uppercase, n_digits, n_punctuation):
    
    # start with a blank string
    output = ''

    # call our random_characters function with different lengths and alphabets
    output += random_characters(n_lowercase, string.ascii_lowercase)
    output += random_characters(n_uppercase, string.ascii_uppercase)
    output += random_characters(n_digits, string.digits)
    output += random_characters(n_punctuation, string.punctuation)

    # shuffle our output
    output = list(output)
    random.shuffle(output)
    output = ''.join(output)

    # return our output
    return output


print(random_password(2, 2, 2, 2))









