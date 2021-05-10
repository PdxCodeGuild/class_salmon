# grading.py - Grading

def letter_grade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

def plus_or_minus(number):
    digit = number % 10
    if digit < 3:
        return '-'
    elif digit > 7:
        return '+'
    else:
        return ''

def final_grade(number):
    letter = letter_grade(number)
    if letter == 'F':
        return letter
    modifier = plus_or_minus(number)
    return letter + modifier

def main():
    grade = int(input('Enter your score to calculate your letter grade: ').strip().lower())
    print(final_grade(grade))

main()
