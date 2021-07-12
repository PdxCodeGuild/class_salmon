// # Lab 4: Blackjack Advice

// # Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). 
// first_card = input("What's your first card? ")
// second_card = input("What's your second card? ")
// third_card = input("What's your third card? ")

// # Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1.
// point_value = {
//     'A': 1,
//     '2': 2,
//     '3': 3,
//     '4': 4,
//     '5': 5,
//     '6': 6,
//     '7': 7,
//     '8': 8,
//     '9': 9,
//     '10': 10,
//     'J': 10,
//     'Q': 10,
//     'K': 10
// }

// first_card = point_value[first_card]
// second_card = point_value[second_card]
// third_card = point_value[third_card]

// def sum_value(card_1, card_2, card_3):
//     total_points = card_1 + card_2 + card_3
//     return total_points

// total_points = sum_value(first_card, second_card, third_card)

// # Use the following rules to determine the advice:
// if total_points < 17:
//     print(f'{total_points} Hit')
// elif 21 > total_points >= 17:
//     print(f'{total_points} Stay')
// elif total_points == 21:
//     print(f'{total_points} Blackjack!')
// elif total_points > 21:
//     print(f'{total_points} Already Busted')


let firstCard = prompt("What's your first card? ").toUpperCase()
let secondCard = prompt("What's your second card? ").toUpperCase()  
let thirdCard = prompt("What's your third card? ").toUpperCase()

const pointValue = {
    A: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    J: 10,
    Q: 10,
    K: 10
}

let cardOne = parseInt(pointValue[firstCard])
// console.log(cardOne)
let cardTwo = parseInt(pointValue[secondCard])
// console.log(cardTwo)
let cardThree = parseInt(pointValue[thirdCard])
// console.log(cardThree)

let totalPoints = parseInt(cardOne + cardTwo + cardThree)

// console.log(totalPoints)

if (totalPoints < 17) {
    alert(`${totalPoints} Hit`)
} else if (21 > totalPoints >= 17) {
    alert(`${totalPoints} Stay`)
} else if (totalPoints === 21) {
    alert(`${totalPoints} Blackjack!`)
} else if (totalPoints > 21) {
    alert(`${totalPoints} Already Busted`)
}