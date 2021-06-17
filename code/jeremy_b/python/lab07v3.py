"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 07
Version: 2
Date: 5/21/2021

"""
from random import randint


# Define encryption function.
def encrypt(text, offset):

    # Make sure all letters are lower case.
    text = text.lower()

    # turn string into list of corresponding ASCII values
    text = list(ord(x) for x in text)

    # Perform encryption
    encrypted_text = list((chr(((x + offset) % 122) + 96) if x + offset > 122 else chr(x + offset)) for x in text)

    # encrypt offset and add to string
    encrypted_text.append(chr(offset + 96))

    # Reconstruct from list into string.
    final_str = "".join(["" + letter for letter in encrypted_text])

    return final_str


# define decryption function
def decrypt(text):
    print(f"String to decrypt: {text}")
    # Get offset and remove from string
    text = list(ord(x) for x in text)
    print(f"List to decrypt: {text}")
    offset = text.pop(-1) - 96
    print(f"Offset: {offset}")
    # decrypted_text = list((chr(((x - offset) % 122) - 96) if x - offset < 122 else chr(x - offset)) for x in text)
    decrypted_text = []
    for letter in text:
        if (letter - offset) < 122:
            decrypted_text.append(chr(letter - offset))
        elif (letter - offset) > 122:
            decrypted_text.append(chr(((letter - offset) % 122) - 96))

    print(f"Decrypted text: ")

    original_str = "".join(["" + letter for letter in decrypted_text])

    return original_str


# Ask user whether to encrypt, decrypt or exit
print(" String Encryption Tool ".center(36, "*"))

while True:
    print("(1) Encrypt")
    print("(2) Decrypt")
    print("(3) Exit\n")
    choice = input("Choose an option: ")
    try:
        if int(choice) == 1:
            str_to_encrypt = input("Enter text to encrypt: ")
            offset = randint(1, 25)
            print(offset)
            print(f"Encrypted string: {encrypt(str_to_encrypt, offset)}")
        elif int(choice) == 2:
            str_to_decrypt = input("Enter text to decrypt: ")
            print(f"Decrypted string: {decrypt(str_to_decrypt)}")
        elif int(choice) == 3:
            break
        else:
            raise ValueError
    except ValueError:
        print("Please enter a valid option from the menu!")

print("\nThank you for using this tool!")

"""
Notes:

1) Added decryption option.  Basically, the final string returned has the offset as the last list element.
   It is also encrypted along with the original string.
2) Took away user ability to input the offset.  It's now done randomly at runtime.  This also removes the need for 
   the try/except loop to catch invalid input.

"""