# rps.py - Rock Paper Scissors
import random

# def calc_winner(user_choice, pc_choice):
	# # hard-coded solution
	# if user_choice == pc_choice:
	# 	print('Tie')
	# elif user_choice == 'rock':
	# 	if pc_choice == 'paper':
	# 		print('Computer wins')
	# 	else: # pc_choice == 'scissors'
	# 		print('Player wins')
	# elif user_choice == 'paper':
	# 	if pc_choice == 'scissors':
	# 		print('Computer wins')
	# 	else: # pc_choice == 'rock'
	# 		print('Player wins')
	# else: # user_choice == 'scissors'
	# 	if pc_choice == 'rock':
	# 		print('Computer wins')
	# 	else: # pc_choice == 'paper'
	# 		print('Player wins')			

def calc_winner(user_choice, pc_choice):
	# # dictionary solution	
	defeats = {'rock': 'scissors',
			   'paper': 'rock',
			   'scissors': 'paper'}

    # if user_choice = rock and pc_choice = paper 
    # then defeats[user_choice] == defeats['rock'] == scissors
    # then scissors != paper
    # then winner is computer
	if user_choice == pc_choice:
		print('Tie!')
	elif defeats[user_choice] == pc_choice:
		print('User wins!')
	else:
		print('Computer wins!')

# # tests
# calc_winner('rock', 'scissors')
# calc_winner('rock', 'rock')
# calc_winner('rock', 'paper')
# calc_winner('paper', 'scissors')
# calc_winner('paper', 'rock')

while True: # loop game until user says stop
	while True: # input validation
		user_choice = input('Rock, paper, scissors: ').strip().lower()
		if user_choice in ['rock', 'paper', 'scissors']:
			break

	# randomly select computer move
	pc_choice = random.choice(['rock', 'paper', 'scissors'])
	print(f'Computer chooses {pc_choice}')
	calc_winner(user_choice, pc_choice) # calculate winner

	while True: # input validation
		play_again = input('Do you want to play again: ')
		if play_again in ['yes', 'y', 'no', 'n']:
			break

	# exit program if user says 'no' or 'n'
	if play_again.startswith('n'):
		break
