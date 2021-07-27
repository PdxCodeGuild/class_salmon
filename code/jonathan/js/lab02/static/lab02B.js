playingCardsA1 = {
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
playingCardsA11 = {
    "A": 11,
}
firstCard = document.getElementsByName("first-card")
secondCard = document.getElementsByName("second-card")
thirdCard = document.getElementsByName("third-card")
runButton = document.querySelector("#run-button")
results = document.getElementById("results")
let linebreak = document.createElement("br")

runButton.addEventListener("click", function(event) {
    event.preventDefault()
    for (var i = 0, length = firstCard.length; i < length; i++) {
        if (firstCard[i].checked) {
            let firstNewCard = firstCard[i].value
            console.log(firstNewCard)
            for (var i = 0, length = secondCard.length; i < length; i++) {
            if (secondCard[i].checked) {
                let secondNewCard = secondCard[i].value
                console.log(secondNewCard)
                for (var i = 0, length = thirdCard.length; i < length; i++) {
                if (thirdCard[i].checked) {
                    let thirdNewCard = thirdCard[i].value
                    console.log(thirdNewCard)
                    handTotal = 0

                    if (firstNewCard == "A") {
                        first = playingCardsA11[firstNewCard]
                        handTotal += first
                        if (secondNewCard == "A") {
                            second = playingCardsA1[secondNewCard]
                            handTotal += second
                            if (thirdNewCard == "A") {
                                third = playingCardsA1[thirdNewCard]
                                handTotal += third
                            }
                            else {
                                third = playingCardsA1[thirdNewCard]
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
                            second = playingCardsA1[secondNewCard]
                            handTotal += second
                            if (handTotal >= 21) {
                                handTotal -= 10
                                third = playingCardsA1[thirdNewCard]
                                handTotal += third
                            }
                            else {
                                third = playingCardsA1[thirdNewCard]
                                handTotal += third
                                if (handTotal > 21) {
                                    handTotal -= 10
                                }

                            }
                        }
                    }
                    else {
                        first = playingCardsA1[firstNewCard]
                        handTotal += first
                        if (secondNewCard == "A") {
                            secpmd = playingCardsA11[secondNewCard]
                            handTotal += secondNewCard
                            if (handTotal >= 21) {
                                handTotal -= 10
                            }
                            else {
                                if (thirdNewCard == "A") {
                                    third = playingCardsA11[thirdNewCard]
                                    handTotal += third
                                    if (handTotal > 21) {
                                        handTotal -= 10
                                    }
                                }
                            }
                        }
                        else {
                            second = playingCardsA1[secondNewCard]
                            handTotal += second
                            if (thirdNewCard == "A") {
                                third = playingCardsA11[thirdNewCard]
                                handTotal += third
                                if (handTotal > 21) {
                                    handTotal -= 10
                                }
                            }
                            else {
                                third = playingCardsA1[thirdNewCard]
                                handTotal += third
                            }
                        }
                    }

                    if (handTotal == 21) {
                        results.append(linebreak)
                        results.append(`${handTotal} is blackjack!`)
                    }
                    else if (handTotal >= 17 && handTotal <= 20) {
                        results.append(linebreak)
                        results.append(`${handTotal} stay!`)
                    }
                    else if (handTotal <= 16) {
                        results.append(linebreak)
                        results.append(`${handTotal} hit!`)
                    }
                    else {
                        results.append(linebreak)
                        results.append(`${handTotal} bust!`)
                    }
        }
    }
        }
    }
        }
    }
    
    
})
