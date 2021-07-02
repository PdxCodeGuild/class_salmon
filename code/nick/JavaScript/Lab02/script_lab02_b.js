let card_selection1 = prompt('Pick 1 card: (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)')
let card_selection2 = prompt('Pick 1 card: (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)')
let card_selection3 = prompt('Pick 1 card: (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)')
// determine point value
if (card_selection1 === 'J' || card_selection1 === 'Q' || card_selection1 === 'K') {
    card_selection1 = 10
} else if (card_selection1 === 'A') {
    card_selection1 = 1    
} else {
    card_selection1 = parseInt(card_selection1)
}
    // console.log(card_selection1) //confirmed working
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
    alert('You are advised to HIT. Your current point total is: ' + String(total_pts))
}
else if (total_pts >= 17 && total_pts < 21) {
    alert('You are advised to STAY. Your current point total is: '+ String(total_pts))
}
else if (total_pts == 21) {
    alert('BLACKJACK - give me your money.')
} 
else {
    alert('Already busted. Play again.')
}