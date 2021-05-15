




def number_grade_to_letter_grade(number_grade):

    plus_minus = ''
    ones_digit = number_grade % 10
    if ones_digit > 5:
        plus_minus = '+'
    elif ones_digit < 5:
        plus_minus = '-'
    
    letter_grade = ''
    if number_grade >= 90:
        letter_grade = 'A' + plus_minus
    elif number_grade >= 80:
        letter_grade = 'B' + plus_minus
    elif number_grade >= 70:
        letter_grade = 'C' + plus_minus
    elif number_grade >= 60:
        letter_grade = 'D' + plus_minus
    else:
        letter_grade = 'F'
    
    return letter_grade




# only run this code if the user runs the module directly
# and not if they import it
if __name__ == '__main__':

    # REPL - read evaluate print loop
    while True:

        while True:
            number_grade = input('What is the number? ') # get the number from the user
            if number_grade.isdigit(): # isdigit() returns true if the string only contains numbers
                break
            else:
                print('enter a number!')

        number_grade = int(number_grade) # convert the number to an integer
        letter_grade = number_grade_to_letter_grade(number_grade)
        print(letter_grade)

        run_again = input('would you like to enter another grade? ').lower()
        if run_again != 'yes':
            print('Goodbye!')
            break



