# program will break if user inputs any value outside of the dictionary

playing_cards_A1 = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}
playing_cards_A11 = {
    "A": 11,
}

# asking the user for their first card
first_card = input("\nWhat's your first card? ")
# asking the user for their second card
second_card = input("\nWhat's your second card? ")
# asking the user for their third card
third_card = input("\nWhat's your third card? ")

# starting hand total
hand_total = 0

# if the first car is an Ace
if first_card == "A":
    first = playing_cards_A11[first_card]
    hand_total += first
    # if the second card is also an Ace
    if second_card == "A":
        second = playing_cards_A1[second_card]
        hand_total += second
        # if the third card is also an Ace
        if third_card == "A":
            third = playing_cards_A1[third_card]
            hand_total += third
        # if the first two cards were Aces but the third is not
        else:
            third = playing_cards_A1[third_card]
            hand_total += third
            # if the sum of these three cards is above 21 change one of the Ace's to 1
            if hand_total > 21:
                hand_total -= 10
            # when the first two cards are Aces and the third card is 10 or a face card
            # change both Ace's to 1's to avoid a bust
            if hand_total == 32:
                hand_total -= 20
    # if the first card is an Ace and the second card is not
    else: 
        second = playing_cards_A1[second_card]
        hand_total += second
        # if the second card is a 10 or a face card
        # change the Ace to 1 to avoid a bust
        if hand_total >= 21:
            hand_total -= 10
            third = playing_cards_A1[third_card]
            hand_total += third
        # if the third card is an ace it will be 1 to avoid a bust   
        else:
            third = playing_cards_A1[third_card]
            hand_total += third
            # if the total is over 21 change the first Ace to 1 
            if hand_total > 21:
                hand_total -= 10
# if the first card is not an Ace                
else:
    first = playing_cards_A1[first_card]
    hand_total += first
    # if the second card is an Ace
    if second_card == "A":
        second = playing_cards_A11[second_card]
        hand_total += second
        # if the first card + the Ace at 11 is greater than or equal to 21
        # change the Ace to 1
        if hand_total >= 21:
            hand_total -= 10
        # if the first card + the Ace at 11 is not greater than or equal to 21    
        else:
            # if the final card is also an Ace
            if third_card == "A":
                third = playing_cards_A11[third_card]
                hand_total += third
                # if the first card and the two Aces at 11 are greater than 21
                # change one of the Aces to 1
                if hand_total > 21:
                    hand_total -= 10
    # if the second card is not an Ace                
    else:
        second = playing_cards_A1[second_card]
        hand_total += second
        # if the third card is an Ace
        if third_card == "A":
            third = playing_cards_A11[third_card]
            hand_total += third
            # if the total is greater than 21 change the value of the Ace to 1
            if hand_total > 21:
                hand_total -= 10
        # if all three cards are not Aces
        else:
            third = playing_cards_A1[third_card]
            hand_total += third

# if total is a blackjack
if hand_total == 21:
    print(f"\n{hand_total} is blackjack!")
# if total is between 17 and 20 will advise the user to stay
elif hand_total >= 17 and hand_total <= 20:
    print(f"\n{hand_total} stay.")
# if total is below 17 will advice the user to hit
elif hand_total <= 16:
    print(f"\n{hand_total} hit.")
# everything else would be above 21 and it is a bust
else: 
    print(f"\n{hand_total} bust!")