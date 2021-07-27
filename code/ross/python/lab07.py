# take user's input
# store input as a list of characters
user_input = list(input("Please type in a phrase to be ciphered: "))

cipher_input = []
cipher = {' ':' ', 'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f':'s', 'g': 't', 'h': 'u', "i": 'v', "j": 'w', "k": "x", 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', "z":'m'}

for i in range(len(user_input)):
    cipher_input.append(user_input[i])

output_string = []

for i in range(len(cipher_input)):
    output_string.append(cipher[cipher_input[i]])

# output ciphered list
print(''.join(output_string))