"""
Lab 3: convert a number grade into a letter grade
"""

grade = int(input('what is the number grade? '))
ones_digit = grade % 10

if grade >= 90:
    letter_grade = 'A'
elif grade >= 80:
    letter_grade = 'B'
elif grade >= 70:
    letter_grade = 'C'
elif grade >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'


if letter_grade != 'F': # because there is no F+ or F-
	if ones_digit > 7:
		letter_grade += '+'
	elif ones_digit < 3:
		letter_grade += '-'

print(letter_grade)