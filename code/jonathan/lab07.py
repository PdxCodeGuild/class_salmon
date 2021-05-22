import string

def caesar_encrypt(unencrypted_message):   
    global encrypted_message
    '''
    Takes the unencrypted message and finds each character in the string "alphabet" 
    and adds the user inputted shift to determine their new position. 
    For numbers greater than 25 the (% 26) will get their value under 25
    or back within the alphabet and joins them together in the encrypted message string
    '''
    encrypted_message = "".join([alphabet[(alphabet.find(c) + encrypt_shift) % 26] for c in unencrypted_message])
    return encrypted_message

def caesar_decrypt(encrypted_message):   
    decrypted_message = ""
    '''
    Takes the encrypted message and finds each character in the string "alphabet" 
    and subtracts the user inputted shift to determine their new(original) position. 
    For numbers greater than 25 the (% 26) will get their value under 25
    or back within the alphabet and joins them together in the encrypted message string
    '''
    decrypted_message = "".join([alphabet[(alphabet.find(c) - encrypt_shift) % 26] for c in encrypted_message])
    return decrypted_message

# list of letters we're working with
alphabet = "abcdefghijklmnopqrstuvwxyz"

# user inputs their unencrypted message and 
unencrypted_message = input("Enter a message to be encrypted: ").lower()

# asks the user for their desired shift
encrypt_shift = input("Enter the shift: ")
# cast to integer
encrypt_shift = int(encrypt_shift)

# removes any spaces in the unencrypted message
unencrypted_message = unencrypted_message.replace(" ", "")
# removes any symbols in the unencrypted message

for p in unencrypted_message: # if punctuation in user word1
    if p in string.punctuation: # checking word for punctuation
        # replace punctuation with blank strings
        unencrypted_message = unencrypted_message.replace(p, "") 

# removes any numbers in the unencrypted message
for n in unencrypted_message: # if numbers in user word1       
    if n in string.digits: # checking word1 for numbers
        # replace numbers with blank strings
        unencrypted_message = unencrypted_message.replace(n, "") 

# print the encrypted message
print(caesar_encrypt(unencrypted_message))
# print the decrypted message
print(caesar_decrypt(encrypted_message))