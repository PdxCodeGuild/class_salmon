import string

class RotCipher:

    def __init__(self, rot_amount):
        self.rot_amount = rot_amount
    
    def encrypt(self, text):
        # start with the alphabet and input string
        alphabet = string.ascii_lowercase
        text = list(text)
        message = ''
        # loop over the characters of the input string
        for i in range(len(text)):
            # find the index of the character in the alphabet
            x = alphabet.index(text[i])
            # add the rot amount to that index
            x += self.rot_amount
            # make sure the new index is still in a valid range (modulus or subtraction)
            # while x > len(alphabet):
            #     x -= len(alphabet)
            x %= len(alphabet)
            # take the character from the alphabet at that new index
            # add the new character to the output
            message += alphabet[x]
        
        return message
    
    def decrypt(self, text):

        # self.rot_amount = -self.rot_amount
        # text = self.encrypt(text)
        # self.rot_amount = -self.rot_amount
        # return text

        # r = RotCipher(-self.rot_amount)
        # return r.encrypt(text)

        # start with the alphabet and input string
        alphabet = string.ascii_lowercase
        text = list(text)
        message = ''
        # loop over the characters of the input string
        for i in range(len(text)):
            # find the index of the character in the alphabet
            x = alphabet.index(text[i])
            # add the rot amount to that index
            x -= self.rot_amount
            # make sure the new index is still in a valid range (modulus or subtraction)
            # while x > len(alphabet):
            #     x -= len(alphabet)
            x %= len(alphabet)
            # take the character from the alphabet at that new index
            # add the new character to the output
            message += alphabet[x]
        
        return message
    
    def __str__(self):
        return f'Rot{self.rot_amount}'

