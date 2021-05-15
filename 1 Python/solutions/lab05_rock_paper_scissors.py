



import random

# the key of the outer dictionary is the human's choice
# the key of the inner dictionary is the computer's choice
results = {
    'rock': {
        'rock': 'tie',
        'paper': 'computer wins',
        'scissors': 'human wins'
    },
    'paper': {
        'rock': 'human wins',
        'paper': 'tie',
        'scissors': 'computer wins'
    },
    'scissors': {
        'rock': 'computer wins',
        'paper': 'human wins',
        'scissors': 'tie'
    }
}

emojis = {
    'rock': '✊',
    'paper': '✋',
    'scissors': '✌'
}

choices = ['rock', 'paper', 'scissors']
while True:
    human_choice = input('Rock, paper, or scissors? ').lower().strip()
    if human_choice not in choices:
        print('invalid input')
        continue
    computer_choice = random.choice(choices)
    print(f'You chose {human_choice} {emojis[human_choice]}')
    print(f'The computer chose {computer_choice} {emojis[computer_choice]}')
    print('The result is: ' + results[human_choice][computer_choice])


