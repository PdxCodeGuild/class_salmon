import random

# your starting balance
balance = 0

def takara(takarakuji, ticket):
    '''
    Function to take the lottery numbers and compare them to each lottery ticket
    and keep a running total of winnings and mostly losings. 
    '''

    lotto_message = ""

    global balance

    if len(matching_numbers) == 1:
        balance += 4
        lotto_message = (f"Matched one number! You win $4 and your new balance is ${balance}")
        return lotto_message
    if len(matching_numbers) == 2:
        balance += 7
        lotto_message = (f"Matched two numbers! You win $7 and your new balance is ${balance}")
        return lotto_message
    if len(matching_numbers) == 3:
        balance += 100
        lotto_message = (f"Matched three numbers! You win $100 and your new balance is ${balance}")    
        return lotto_message
    if len(matching_numbers) == 4:
        balance += 50000
        lotto_message = (f"Matched four numbers! You win $50,000 and your new balance is ${balance}")
        return lotto_message
    if len(matching_numbers) == 5:
        balance += 1000000
        lotto_message = (f"Matched five numbers! You win $1,000,000 and your new balance is ${balance}")
        return lotto_message
    if len(matching_numbers) == 6:
        balance += 25000000
        lotto_message = (f"Matched them all! You win $25,000,000 and your new balance is ${balance}")
        return lotto_message
    else:
        lotto_message = f"You matched no numbers and wasted $2"
        return lotto_message

# drawing the six lotto numbers from 1 to 100
# outside the loop because the lotto numbers won't change
takarakuji = random.sample(range(1, 100), 6)

# to play the lotto 100,000 times
for x in range(1, 100001):

    # subtract the cost of each ticket from your balance every loop
    balance -= 2

    # your ticket drawing six numbers from 1 to 100
    # this changes every loop so it is inside unlike the lotto numbers
    ticket = random.sample(range(1, 100), 6)

    # comparing each number between the ticket and the lotto
    matching_numbers = [t1 for t1, t2 in zip(takarakuji, ticket) if t1 == t2]

    # print(takarakuji) # if you want to print out the lottery ticket
    # print(ticket) # if you want to print out each of your tickets

    print(takara(takarakuji, ticket))

# adding commas to ending balance
balance_commas = "{:,}".format(balance)
# adding the $ to ending balance
new_balance = "${:,.2f}".format(balance)

roi = (balance - 200000)/200000 
# adding two decimal places to roi
number_two_decimal = "{:.2f}".format(roi)
# adding commas to roi
balance_commas = "{:,}".format(roi)
# adding the % to roi
new_roi = "{:,.2f}%".format(roi)

expenses = x*2
# adding commas to ending balance
expenses_commas = "{:,}".format(expenses)
# adding the $ to ending balance
expenses_balance = "${:,.2f}".format(expenses)

print(f"Your ending balance after {x} tries is {new_balance}")
print(f"Your earnings were {new_balance} and your expenses were {expenses_balance} and your ROI over {x} tries is {new_roi}.")
print("Lottery games are based on chance, should be played for entertainment only and should not be played for investment purposes.")