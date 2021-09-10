# Import modules
import random

# Input the user score
user_score = input("Enter the score you received: ")

# Convert user score to integer
user_score = int(user_score)

# Generate the rival score
rival_score = random.randint(0, 100)

# Use modulus to determine the appendage for the + or -
user_letter_append = user_score % 10

if user_letter_append >= 7:
    user_letter_append = "+"

elif user_letter_append <= 3:
    user_letter_append = "-"

else:
    user_letter_append = ""

rival_letter_append = rival_score % 10

if rival_letter_append >= 7:
    rival_letter_append = "+"

elif rival_letter_append <= 3:
    rival_letter_append = "-"

else:
    rival_letter_append = ""

# Convert the grades to letters
# Validation check if score is greater than 100
if user_score > 100:
    print(f"{user_score} is higher than the max of 100. Please enter an appropriate score.")
    exit()

# Assign the user grade to the number range
if 100 == user_score:
    user_grade = f"A++. Perfect Score"
elif 100 >= user_score >= 90:
    user_grade = f"A{user_letter_append}"
elif 89 >= user_score >= 80:
    user_grade = f"B{user_letter_append}"
elif 79 >= user_score >= 70:
    user_grade = f"C{user_letter_append}"
elif 69 >= user_score >= 60:
    user_grade = f"D{user_letter_append}"
else:
    user_grade = f"F"

# Assign the rival grade to the number range
if 100 == rival_score:
    rival_grade = f"A++. Perfect Score"
elif 100 >= rival_score >= 90:
    rival_grade = f"A{rival_letter_append}"
elif 89 >= rival_score >= 80:
    rival_grade = f"B{rival_letter_append}"
elif 79 >= rival_score >= 70:
    rival_grade = f"C{rival_letter_append}"
elif 69 >= rival_score >= 60:
    rival_grade = f"D{rival_letter_append}"
else:
    rival_grade = f"F"

# Compare user to rival
if user_score > rival_score:
    compare_result = "YES!"
elif user_score < rival_score:
    compare_result = "Unfortunately no..."
else:
    compare_result = "Woah! You tied. What a coincidence."

final_output = f"""
Your grade is a {user_grade}, with a score of {user_score}.
But did you beat your rival?
{compare_result}
Rival's grade is {rival_grade}, with a score of {rival_score}.
"""
print(final_output)
