# Mad Lib Exercise

# Text to act as the Mad Lib
'''

BOY1 and GIRL1 were walking down the street when a SCARYTHING jumped out at them suddenly.
"EXCLAMATION!" they screamed.
Even though they kicked and shouted the SCARYTHING carrried on and hurtled down the street.
Their friend, BOY2, happened to see them and he ran and got help.
Now the two children are sitting by the blazing fire telling their stories.

'''

# Gather user input

boy_1 = input("Enter a boy name: ")
girl = input("Enter a girl name: ")
boy_2 = input("Enter another boy name: ")
scary_thing = input("Name something scary: ")
exclamation = input("What's something embarrassing to yell in public?: ")

# Format name inputs
boy_1 = (boy_1).capitalize()
girl = (girl).capitalize()
boy_2 = (boy_2).capitalize()
exclamation = (exclamation).upper()

# Test user inputs
# print(boy_1 , girl , boy_2 , scary_thing , exclamation)

# Format the Mad Lib
print(f"""

Unit 2 Mad Lib
--------------

{boy_1} and {girl} were walking down the street when a {scary_thing} jumped out at them suddenly.
\"{exclamation}!\" they screamed.
Even though they kicked and shouted the {scary_thing} carrried on and hurtled down the street.
Their friend, {boy_2}, happened to see them and he ran and got help.
Now the two children are sitting by the blazing fire telling their stories.

""")