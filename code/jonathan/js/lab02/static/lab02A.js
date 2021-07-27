let playingCardsA1 = {
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
let playingCardsA11 = {
    "A": 11,
}

let firstCard = prompt("What's your first card?")
let secondCard = prompt("What's your second card?")
let thirdCard = prompt("What's your third card?")

let handTotal = 0

if (firstCard == "A") {
    first = playingCardsA11[firstCard]
    handTotal += first
    if (secondCard == "A") {
        second = playingCardsA1[secondCard]
        handTotal += second
        if (thirdCard == "A") {
            third = playingCardsA1[thirdCard]
            handTotal += third
        }
        else {
            third = playingCardsA1[thirdCard]
            handTotal += third
            if (handTotal > 21) {
                handTotal -= 10
            if (handTotal == 32) {
                handTotal -= 20
            }
            }
        }
    }
    else {
        second = playingCardsA1[secondCard]
        handTotal += second
        if (handTotal >= 21) {
            handTotal -= 10
            third = playingCardsA1[thirdCard]
            handTotal += third
        }
        else {
            third = playingCardsA1[thirdCard]
            handTotal += third
            if (handTotal > 21) {
                handTotal -= 10
            }

        }
    }
}
else {
    first = playingCardsA1[firstCard]
    handTotal += first
    if (secondCard == "A") {
        secpmd = playingCardsA11[secondCard]
        handTotal += secondCard
        if (handTotal >= 21) {
            handTotal -= 10
        }
        else {
            if (thirdCard == "A") {
                third = playingCardsA11[thirdCard]
                handTotal += third
                if (handTotal > 21) {
                    handTotal -= 10
                }
            }
        }
    }
    else {
        second = playingCardsA1[secondCard]
        handTotal += second
        if (thirdCard == "A") {
            third = playingCardsA11[thirdCard]
            handTotal += third
            if (handTotal > 21) {
                handTotal -= 10
            }
        }
        else {
            third = playingCardsA1[thirdCard]
            handTotal += third
        }
    }
}

if (handTotal == 21) {
    alert(`${handTotal} is blackjack!`)
}
else if (handTotal >= 17 && handTotal <= 20) {
    alert(`${handTotal} stay`)
}
else if (handTotal <= 16) {
    alert(`${handTotal} hit`)
}
else {
    alert(`${handTotal} bust`)
}