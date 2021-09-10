# Import modules
import random

# Input the user score
user_score = input("Enter the score you received: ")

# Convert user score to integer
user_score = int(user_score)

# Generate the rival score
rival_score = random.randint(0, 100)

# Use modulus to determine '+' or '-'
score_append = user_score % 10
rival_score_append = rival_score % 10

# Prevent score 100 = -
if user_score == 100:
    perfect = "+++"
    score_append = perfect

# '+' 9-7>=%
elif score_append == 9 or 8 or 7:
    score_append = "+"

# '-' = %>= 0-3
elif score_append == 3 or 2 or 1 or 0:
    score_append = "-"

# Neutral
else:
    print(".")

# Prevent score 100 = -
if rival_score == 100:
    perfect = "+++"
    rival_score_append = perfect

# '+' 9-7>=%
elif rival_score_append == 9 or 8 or 7:
    rival_score_append = "+"

# '-' = %>= 0-3
elif rival_score_append == 3 or 2 or 1 or 0:
    rival_score_append = "-"

# Neutral
else:
    print(".")

# Convert score to letter grade using if/elif/else

# If user_score > 100
if user_score > 100:
    print(f"You can't score a {user_score}! Enter your true score")

# If user_score <= 100 and >= 90
elif 100 >= user_score >= 90:
    print(f"With a score of {user_score} you have an A{score_append}. Fantastic!")

# If user_score <= 89 and >= 80
elif 89 >= user_score >= 80:
    print(f"With a score of {user_score} you have an B{score_append}. You're doing great.")

# If user_score <= 79 and >= 70
elif 79 >= user_score >= 70:
    print(f"With a score of {user_score} you have an C{score_append}. There's room for improvement.")

# If user_score <= 69 and >= 60
elif 69 >= user_score >= 60:
    print(f"With a score of {user_score} you have an D{score_append}. That's close to failure.")

# If user_score <= 59 and >= 0
else:
    print(f"With a score of {user_score} you have an F{score_append}. At least your a nice person...")

# Compare to the rival

# Greater than the rival
if user_score > rival_score:
    print(f"Congrats! Your score of {user_score} is higher than your rival's {rival_score}.\nYou have an ")
# Equal to the rival

# Less than the rival