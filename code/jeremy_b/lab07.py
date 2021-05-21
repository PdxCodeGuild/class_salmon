"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 07
Version: 1
Date: 5/21/2021

"""


# Define encryption function.
def encrypt(text):

    # Make sure all letters are lower case.
    text = text.lower()

    # turn string into list of corresponding ASCII values
    text = list(ord(x) for x in text)

    # Perform encryption
    encrypted_text = list((chr(((x + 13) % 122) + 96) if x + 13 > 122 else chr(x + 13)) for x in text)

    # Reconstruct from list into string.
    final_str = "".join(["" + letter for letter in encrypted_text])

    return final_str


str_to_encrypt = input("Enter text to encrypt: ")
print(f"Encrypted string: {encrypt(str_to_encrypt)}")

"""
Notes:

1) Since integers are easier to work with that strings, I used 'chr' and 'ord' to convert the string to ASCII dec values
   and dec values to characters respectfully.  This seems to have the advantage of using built in functions and not 
   having to deal with list searching.
2) Doing it this way also makes it easier to extrapolate to include capital letters, punctuation, etc.
3) I think it would be easier to decrypt this way as well.

"""
