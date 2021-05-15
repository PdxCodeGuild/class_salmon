

# V1
# generate random number between a,b
# secret_num = random.randint(1,5)

guess_count = 0

# game loop
while guess_count < 10:
    print(guess_count)

    # prompt user for number guess
    guess = int(input('Guess a Number: '))

    # win condition
    if(secret_num == guess):
        print('WIN')
        print(f'You guess it in {guess_count + 1} tries!! CONGRATZ')
        break
    else:
        # increment guess count every iteration
        guess_count += 1
        print(f'Wrong number! {10 - guess_count} guesses remaining')


if(guess_count == 10):
    print('FAIL')
# Do you want to play again
