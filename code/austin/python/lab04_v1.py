def valid_card(card):
    if card in ('1,2,3,4,5,6,7,8,9,10'):
        return int(card)
    elif card in ('Q,q,j,J,K,k'):
        return 10
    elif card in ('A,a'):
            return 1
def blackjack_advice():
    card1 = valid_card(input("What's your first card?"))
    card2 = valid_card(input("What's your second card?"))
    card3 = valid_card(input("What's your third card?"))
    cards_tot = (card1)+(card2)+(card3)
    if cards_tot < 17:
        return f"{cards_tot} Hit"
    elif cards_tot < 21:
        return f"{cards_tot} Stay"
    elif cards_tot == 21:
        return f"{cards_tot} Blackjack"
    else:
        return f"{cards_tot} Already busted"
print(blackjack_advice())
