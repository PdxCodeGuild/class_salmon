alert("Please choose three cards.")
let first_card = prompt("Pick your first card (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K): ")
console.log("first card: " + first_card)
let second_card = prompt("Pick your second card (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K): ")
console.log("second card: " + second_card)
let third_card = prompt("Pick your third card (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K): ")
console.log("third card: " + third_card)
console.log("total = " + (parseInt(first_card) + parseInt(second_card) + parseInt(third_card)))

let values = {
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


console.log("first card: " + values[first_card])
let total_value = (parseInt(values[first_card]) + parseInt(values[second_card]) + parseInt(values[third_card]))
console.log("total val variable = " + total_value)

function advice() {
    if (total_value < 17) {
        alert("Hit")
    } else if (total_value >= 17 && total_value < 21) {
        alert("Stay")
    } else if (total_value == 21) {
        alert("Blackjack!")
    } else {
        alert("Already Busted!")
    }
}

alert(advice())