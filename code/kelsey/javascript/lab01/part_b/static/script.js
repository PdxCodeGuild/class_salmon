let firstCard = document.getElementById("first")
let secondCard = document.getElementById("second")
let thirdCard = document.getElementById("third")

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
let cardTwo = parseInt(pointValue[secondCard])
let cardThree = parseInt(pointValue[thirdCard])

let totalPoints = parseInt(cardOne + cardTwo + cardThree)

onsubmit