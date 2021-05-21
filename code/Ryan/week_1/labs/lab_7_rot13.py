# Prompt the user to enter a string
input_string = input("Enter a word: ")
print(input_string)

# Separate each letter
input_string = (list(map(str,input_string)))

output_string = ""

# Check the dictionary for the corresponding key
cipher = {
"a": "n",
"b": "o",
"c": "p",
"d": "q",
"e": "r",
"f": "s",
"g": "t",
"h": "u",
"i": "v",
"j": "w",
"k": "x",
"l": "y",
"m": "z",
"n": "a",
"o": "b",
"p": "c",
"q": "d",
"r": "e",
"s": "f",
"t": "g",
"u": "h",
"v": "i",
"w": "j",
"x": "k",
"y": "l",
"z": "m",
}

# For each letter in the string
for each_letter in input_string:

    # Change the variable name to check_letter
    check_letter = each_letter

    # For each letter in the cipher
    for each_cipher_letter in cipher:

        # If the check_letter is equal to the cipher letter
        if check_letter == each_cipher_letter:

            # Get the value of the cipher letter
            cipher_letter_value = cipher[each_cipher_letter] 

            # Add to output
            output_string += cipher_letter_value

# Output the string
print(output_string)
