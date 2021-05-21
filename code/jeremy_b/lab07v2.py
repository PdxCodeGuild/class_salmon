"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 07
Version: 2
Date: 5/21/2021

"""


# Define encryption function.
def encrypt(text, offset):

    # Make sure all letters are lower case.
    text = text.lower()

    # turn string into list of corresponding ASCII values
    text = list(ord(x) for x in text)

    # Perform encryption
    encrypted_text = list((chr(((x + offset) % 122) + 96) if x + offset > 122 else chr(x + offset)) for x in text)

    # Reconstruct from list into string.
    final_str = "".join(["" + letter for letter in encrypted_text])

    return final_str


str_to_encrypt = input("Enter text to encrypt: ")

while True:
    try:
        offset = int(input('Enter integer between 1 and 25: '))
        if offset not in range(1, 25):
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid integer that is between 1 and 25")

print(f"Encrypted string: {encrypt(str_to_encrypt, offset)}")

"""
Notes:

1) Added ability to specify the encryption key offset.
2) Offset has error checking.

"""
