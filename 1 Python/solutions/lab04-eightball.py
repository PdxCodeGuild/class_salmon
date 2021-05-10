"""
Lab 4: Magic 8-Ball
"""
import random

predictions = ["It is certain","It is decidedly so","Without a doubt","Yes definitely","You may rely on it","As I see it, yes","Most likely","Outlook good","Yes","Signs point to yes","Reply hazy try again","Ask again later","Better not tell you now","Cannot predict now","Concentrate and ask again","Don't count on it","My reply is no","My sources say no","Outlook not so good","Very doubtful"]

# input validation
while True:
	# new user input at the beginning of each loop
	user_in = input('Welcome! Ask me a question: ').lower().strip() 
	if user_in == 'done': # exit condition
		break
	print(random.choice(predictions))
