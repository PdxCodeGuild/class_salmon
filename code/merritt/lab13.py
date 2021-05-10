import string

def rot_x(input_string, rotation_amount):
    output_string = ""
    for letter in input_string:
        if letter in string.ascii_lowercase:
            output_string += string.ascii_lowercase[(string.ascii_lowercase.index(letter) + int(rotation_amount)) % 26]
        elif letter in string.ascii_uppercase:
            output_string += string.ascii_uppercase[(string.ascii_uppercase.index(letter) + int(rotation_amount)) % 26]
        else:
            output_string += letter
    return output_string

print(rot_x(input("enter a string: "), input("enter rotation: ")))