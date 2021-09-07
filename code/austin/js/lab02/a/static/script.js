/*def valid_card(card):
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
print(blackjack_advice())*/
function validCard(cardNumber){
    let cards = {
        "1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"j":10,"q":10,"k":10,"a":1
    } 
    while(true){
        let card = (prompt(`What is your ${cardNumber} card? \n choices: 1,2,3,4,5,6,7,8,9,10,j,q,k,a`)).toLowerCase()
        for(key in cards){
            if(key === card){
                return cards[key]
            }
        }
    }
}
function blackjackAdvice(){
    let card1 = validCard("first")
    let card2 = validCard("second")
    let card3 = validCard("third")
    let cardTotal = card1 + card2 + card3
    if (cardTotal < 17) {
        alert(`${cardTotal} Hit`)
    } else if (cardTotal <21) {
        alert(`${cardTotal} Stay`)
    } else if (cardTotal === 21) {
        alert(`${cardTotal} Blackjack`)
    } else {
        alert(`${cardTotal} Bust`)
    }
}
while(true){
    blackjackAdvice()
}