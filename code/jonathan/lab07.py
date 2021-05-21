import string

raw_list = []

# takes the input and converts to lowercase
raw_message = input("Enter a message to encode: ").lower() 

# if punctuation in raw_list 
for x in raw_message: 
# checking message for punctuation
    if x in string.punctuation: 
    # replace punctuation with blank strings
        raw_message = raw_message.replace(x, "") 
# if numbers in user raw_list             
for z in raw_message:  
# checking message for numbers
    if z in string.digits: 
    # replace numbers with blank strings
        raw_message = raw_message.replace(z, "") 

raw_list = list(raw_message)

print(raw_list)

rot_letters = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26
<<<<<<< HEAD
}
=======
}

# take the letter and find the number value from the rot_letters dictionary
# add 13 to each number and IF the (number is > 26) - 26 
# # find the new value from the same dictionary 


>>>>>>> f27848dcf0c6bb1791555a036794346a611f48bc
