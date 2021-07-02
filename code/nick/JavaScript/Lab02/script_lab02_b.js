// let card_selection1 = document.getElementById("card1")
// let card_selection2 = document.getElementById("card2")
// let card_selection3 = document.getElementById("card3")
let addCardsBtn = document.getElementById("add_cards")
// determine point value
addCardsBtn.addEventListener("click", function(event) {
    event.preventDefault()
    let card_selection1 = document.getElementById("card1").value
    let card_selection2 = document.getElementById("card2").value
    let card_selection3 = document.getElementById("card3").value
    console.log(card_selection1)
    if (card_selection1 === 'J' || card_selection1 === 'Q' || card_selection1 === 'K') {
        card_selection1 = 10
    } else if (card_selection1 === 'A') {
        card_selection1 = 1    
    } else {
        card_selection1 = parseInt(card_selection1)
    }
    console.log(card_selection1) //
    if (card_selection2 === 'J' || card_selection2 === 'Q' || card_selection2 === 'K') {
        card_selection2 = 10
    } else if (card_selection2 === 'A') {
        card_selection2 = 1    
    } else {
        card_selection2 = parseInt(card_selection2)
    }

    if (card_selection3 === 'J' || card_selection3 === 'Q' || card_selection3 === 'K') {
        card_selection3 = 10
    } else if (card_selection3 === 'A') {
        card_selection3 = 1    
    } else {
        card_selection3 = parseInt(card_selection3)
    }

    let total_pts = [card_selection1, card_selection2, card_selection3].reduce(function (a, b) {
        return a + b
    }, 0)
    console.log(total_pts);// confirmed working
    if (total_pts < 17) {
        let advice = document.createElement("p")
        console.log(advice)
        results.append(advice, String("You are advised to HIT. Your current point total is: " + String(total_pts)))
    }
    else if (total_pts >= 17 && total_pts < 21) {
        let advice = document.createElement("p")
        results.append(advice, String("You are advised to STAY. Your current point total is: " + String(total_pts)))
        // alert('You are advised to STAY. Your current point total is: '+ String(total_pts))
    }
    else if (total_pts == 21) {
        let advice = document.createElement("p")
        results.append(advice, String("BLACKJACK - give me your money. Your current point total is: " + String(total_pts)))
        // alert('BLACKJACK - give me your money.')
    } 
    else {
        let advice = document.createElement("p")
        results.append(advice, String("Already busted. Refresh to get advice on your next game."))
        // alert('Already busted. Play again.')
    }
})