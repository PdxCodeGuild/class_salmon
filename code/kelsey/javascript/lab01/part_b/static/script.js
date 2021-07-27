// 1. queries - get pieces from html
// 2. input from user
// 3. formula => advice
// 4. return advice

let form = document.querySelector("#forms")
let firstCard = document.querySelector("#first")
let secondCard = document.querySelector("#second")
let thirdCard = document.querySelector("#third")
let btn = document.querySelector("#submit")
let advice = document.querySelector("#advice")

function totalPoints(firstCard, secondCard, thirdCard) {
    let total = parseInt(firstCard.value) + parseInt(secondCard.value) + parseInt(thirdCard.value)
    return total
}

btn.addEventListener("click", function(event) {
    event.preventDefault()
    let total = totalPoints(firstCard, secondCard, thirdCard)
    let newAdvice = document.createElement("li")
    let horizontalRule = document.createElement("hr")
    newAdvice.innerText = `Your total is: ${total}.`
    if (total < 17) {
        advice.prepend('Hit!')
    } else if (21 > total && total >= 17) {
        advice.prepend('Stay!')
    } else if (total === 21) {
        advice.prepend('Blackjack!')
    } else if (total > 21) {
        advice.prepend('Already Busted.')
    }
    advice.prepend(newAdvice)
    advice.prepend(horizontalRule)
})