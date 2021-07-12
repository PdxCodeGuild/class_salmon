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
let submitBtn = document.getElementById("submitBtn")
let results = document.getElementById("results")
submitBtn.addEventListener("click", function(event) {
    event.preventDefault()
    let card = document.getElementsByClassName("card")
    console.log(card)
    var cardTotal = 0
    for (let i=0; i<card.length; i++) {
        cardTotal += parseFloat(card[i].value)
        console.log(card[i])
    }
    if (cardTotal < 17) {
        //used var so i wouldnt have to duplicate creating results in each if statement
        var advice = `${cardTotal} Hit`
    } else if (cardTotal <21) {
        var advice = `${cardTotal} Stay`
    } else if (cardTotal === 21) {
        var advice = `${cardTotal} Blackjack`
    } else {
        var advice = `${cardTotal} Bust`
    }
    let result = document.createElement("li")
        result.innerText = advice
        results.prepend(result)
})