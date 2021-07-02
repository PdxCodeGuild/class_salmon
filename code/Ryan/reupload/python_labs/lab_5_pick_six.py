"""
import random
number_generator = random.randint(1, 99)
def pick_6():
    pick_6 = []
    while len(pick_6) < 7:
        pick_6.append(random.randint(1, 99))
    return pick_6
# winning_numbers = pick_6()
winning_numbers = [23, 25, 30, 50, 70, 89, 98]
winning_numbers.sort()
print(winning_numbers)
# player_numbers = pick_6()
player_numbers = [2, 12, 23, 50, 93, 95, 99]
player_numbers.sort()
print(player_numbers)
def num_matches():
    output = []
    i = 0
    for each_number in player_numbers:
        # Does this number match the winning number at the same index?
        if each_number == winning_numbers[i]:
            output.append("w")
            continue
        else:
            output.append("l")
            continue
    i += 1
    return output.count("w")
def pnl():
    player_numbers.count()
def play(plays):
    plays = int(plays)
    while p < plays:
        pick_6
        num_matches
    
    return 
p = 0
plays = 5
while p < plays:
        print(pick_6())
        print(num_matches())
        p += 1
  
loss = plays * -2
print(loss)
"""
import random

# Player ticket
test_player_ticket = []

while len(test_player_ticket) < 6:
    test_player_ticket.append(random.randint(1, 99))

test_player_ticket.sort()

total_tickets = 1000

# Pick6 tickets
test_pick6_tickets =  []

total_ticket_winnings = 0

while len(test_pick6_tickets) != total_tickets:
    # Generate a ticket
    add_pick6_ticket = []

    while len(add_pick6_ticket) < 6:
        add_pick6_ticket.append(random.randint(1, 99))


    add_pick6_ticket.sort()
    #print(add_pick6_ticket)
    #print(test_player_ticket)
    # Add the ticket to the list of tickets
    test_pick6_tickets.append(add_pick6_ticket)

    #print(test_pick6_tickets)

    # Foreach ticket in the list of tickets
    for ticket in test_pick6_tickets:

    # Running count of winners
        matching_numbers = 0

    # Separate each ticket number 
    # Check if the ticket matches the player numbers
        #print(ticket)
        #print(test_player_ticket)
        if ticket[0] == test_player_ticket[0]:
            matching_numbers += 1
        if ticket[1] == test_player_ticket[1]:
            matching_numbers += 1
        if ticket[2] == test_player_ticket[2]:
            matching_numbers += 1
        if ticket[3] == test_player_ticket[3]:
            matching_numbers += 1
        if ticket[4] == test_player_ticket[4]:
            matching_numbers += 1
        if ticket[5] == test_player_ticket[5]:
            matching_numbers += 1

    # If the ticket is a winner, how many numbers match
    #print(matching_numbers)
    
    if matching_numbers == 1:
        total_ticket_winnings += 4
    if matching_numbers == 2:
        total_ticket_winnings += 7
    if matching_numbers == 3:
        total_ticket_winnings += 100
    if matching_numbers == 4:
        total_ticket_winnings += 50000
    if matching_numbers == 5:
        total_ticket_winnings += 1000000
    if matching_numbers == 6:
        total_ticket_winnings += 25000000

    current_tickets = int(len(test_pick6_tickets))
    remaining_tickets = total_tickets - current_tickets
    print(remaining_tickets)

ticket_cost = len(test_pick6_tickets) * 2
roi = ((total_ticket_winnings - ticket_cost)/ticket_cost)*100
print(f"Spent ${ticket_cost}. Won ${total_ticket_winnings} with an ROI of {roi}%")