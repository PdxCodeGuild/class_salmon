const values = {
    A:1,
    2:2,
    3:3,
    4:4,
    5:5,
    6:6,
    7:7,
    8:8,
    9:9,
    10:10,
    J:10,
    Q:10,
    K:10,
}


class Advice {
    // constructor(){
    // }

    total(first_card, second_card, third_card) {
        return (first_card + second_card + third_card)
    }

    advice(total_value) {
        if (total_value < 17) {
            advice_div.innerText = "Hit"
        } else if (total_value >= 17 && total_value < 21) {
            advice_div.innerText = "Stay"
        } else if (total_value == 21) {
            advice_div.innerText = "Blackjack!"
        } else {
            advice_div.innerText = "Already Busted!"
        }
    }
}

let play = new Advice

let btn = document.querySelector('#submit_btn')

btn.onclick = function() {
    let first_card = document.querySelector('#first_card')
    console.log("first card: " + values[first_card.value])
    first_card = values[first_card.value]
    let second_card = document.querySelector('#second_card')
    console.log("second card: " + values[second_card.value])
    second_card = values[second_card.value]
    let third_card = document.querySelector('#third_card')
    console.log("third card: " + values[third_card.value])
    third_card = values[third_card.value]
    console.log("total = " + (first_card + second_card + third_card))
    total = play.total(first_card, second_card, third_card)
    play.advice(total)
}