import random

def get_grade(score):
    '''Return a letter grade based on the provided score'''
    # check the score
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    elif score >= 0:
        grade = 'F'

    return grade

def get_modifier(score):
    '''extra challenge...fill in this function to return a grade modifier +/- based on the score'''
    pass

# ask the user for their score
user_score = input("Please enter your score 0-100: ")

# convert score to integer
user_score = int(user_score)

# generate the rival's score
rival_score = random.randint(0, 100)


# get the user's grade by passing their score to the function
user_grade = get_grade(user_score)

# get the rival's grade by passing their score to the function
rival_grade = get_grade(rival_score)


print(f"score: {user_score}, grade: {user_grade}")
print(f"score: {rival_score}, grade: {rival_grade}")