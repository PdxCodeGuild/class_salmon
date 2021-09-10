// Card picks object
const card_picks = []

// document selectors
let advice = document.querySelector("#advice")
let cardTotal = document.querySelector("#displayTotal")
let showCards = document.querySelector("#displayCards")

// Function to total all cards in card_picks
function addCards(){
    let card_total = 0

    for(let i = 0; i < card_picks.length; i++){
        card_total += card_picks[i]
    }

    console.log(card_total)
    displayTotal.innerHTML = card_total
    showCards.innerHTML = card_picks
    
    if(card_total > 21){
        advice.innerHTML = '<span class="tag is-danger is-large">Busted!</span>';
    } else if(card_total === 21){
        advice.innerHTML = '<span class="tag is-success is-large">BLACKJACK!</span>';
    } else if(card_total < 21 && card_total > 16){
        advice.innerHTML = '<span class="tag is-warning is-large">Stay!</span>'
    } else if(card_total === 0){
        advice.innerHTML = "Pick a card to start."
    } else{
        advice.innerHTML = '<span class="tag is-info is-large">Hit</span>'
    }

}

// Function to add each card to card_picks 
function addAce(){
    card_picks.push(1)
    addCards()
}

function add2(){
    card_picks.push(2)
    addCards()
}

function add3(){
    card_picks.push(3)
    addCards()
}

function add4(){
    card_picks.push(4)
    addCards()
}
function add5(){
    card_picks.push(5)
    addCards()
}

function add6(){
    card_picks.push(6)
    addCards()
}
function add7(){
    card_picks.push(7)
    addCards()
}

function add8(){
    card_picks.push(8)
    addCards()
}
function add9(){
    card_picks.push(9)
    addCards()
}

function add10(){
    card_picks.push(10)
    addCards()
}

function addJack(){
    card_picks.push(10)
    addCards()
}

function addQueen(){
    card_picks.push(10)
    addCards()
}

function addKing(){
    card_picks.push(10)
    addCards()
}


addCards()
