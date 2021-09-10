# Import random
import random

# Import the characters to use
import string

letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation

all_characters = letters + digits + punctuation

# Start with empty password
final_password = ""

# Prompt from user to specify length
max_pw_length = int(input("How long would you like your password to be?: "))

# Build new string of random characters
# Do until length is equal to max length
while len(final_password) < max_pw_length:

    # Pick a random character from all available choices
    # Add the new character to the final password string
    final_password += random.choice(all_characters)

# Display output
print(f"""
Your password: {final_password}
""")