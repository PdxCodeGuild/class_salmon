# Import module
import random

# Intro
print(f"""
------------------------------------------
Welcome to the rock, paper, scissors game!
Today it's Man vs Machine. 
Who will come out victorious?
""")
# List possible choices
rps_list = ["Rock", "Paper", "Scissors"]

# User picks choice with list menu
counter = 0
for item in rps_list:
    print(f'{counter} {item}')
    counter += 1

# User prompt for choice
user_choice = int(input(f"""
Pick a number and hit Enter: """))

# Computer picks random choice
comp_choice = random.randint(0, 2)

# Compare the results
# Catch ties
if comp_choice == user_choice:
    decision = "tied"

# Win Conditions or else loss
elif user_choice == 0 and comp_choice == 2:
    decision = "win"
elif user_choice == 1 and comp_choice == 0:
    decision = "win"
elif user_choice == 2 and comp_choice == 1:
    decision = "win"
else:
    decision = "lose"

# Validation check
if user_choice >= 3:
    print("Incorrect choice. Please restart.")
    exit()

# Change integers to string for evaluation
user_choice = str(user_choice)
comp_choice = str(comp_choice)

# Display output
print(f"""
------------------------------------------
That was a close match!!!
You chose: {rps_list[(eval(user_choice))]}.

But did you beat your opponent?
------------------------------------------
""")
wait = input("Press Enter to see the result.")

print(f"""
------------------------------------------
You {decision}!

The Computer chose {rps_list[(eval(comp_choice))]}.
See you next time!
------------------------------------------
""")

wait = input()