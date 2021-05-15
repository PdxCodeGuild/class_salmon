# Using a while loop, allow the user to guess 10 times. If they fail to guess the number after 10 tries, the user is told they've lost. If the user guesses the number, the user is told they've won and the game exits. You can get a random number using random.randint:
import random




# PART 5
import random

# generate random number between a,b

guess_count = 0
game_loop = True
last_guess = 0
guess = ''
# prompt user for number guess
secret_num = int(input('Pick a Secret Number (1-5): '))

# game loop
while game_loop:
    print()
    guess = random.randint(1, 5)
    print(f'Computer Guessed: {guess}')
    # increment guess count every iteration
    guess_count += 1

    # win condition
    if secret_num == guess:
        print('WIN')
        print(f'You guessed it in {guess_count} tries!! CONGRATZ')
        game_loop = False
    else:
        if last_guess:
            if abs(last_guess-secret_num) > abs(guess-secret_num):
                print(f"You're getting Warmer!")
            elif abs(last_guess-secret_num) == abs(guess-secret_num):
                print("You are no Closer and Further than last time.")
            else:
                print("You're getting Colder!")
        print(f"Wrong number! You've guessed {guess_count} many times!")

        if guess < secret_num:
            print('Your guess is to Low!')
        else:
            print('Your guess is to High')

    last_guess = guess
