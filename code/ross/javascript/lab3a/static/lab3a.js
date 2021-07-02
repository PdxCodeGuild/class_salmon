let number = prompt("Please input your credit card number: ")
number = Number(number)

let card_list = String(number).split("").map((number)=>{
    return Number(number)
})
console.log(card_list)

let check_digit = card_list.pop()
console.log(card_list)
console.log(check_digit)

let reversed_list = card_list.reverse()
console.log(reversed_list)

let doubled_list = []

for (let i = 0; i<reversed_list.length; i++) {
    if (i % 2 == 0) {
        doubled_list[i] = reversed_list[i] * 2
    } else {
        doubled_list[i] = reversed_list[i]
    }
}
console.log("doubled list: " + doubled_list)

let sub_nine = []

for (let i = 0; i<doubled_list.length; i++) {
    if (doubled_list[i] > 9) {
        sub_nine[i] = doubled_list[i] - 9
    } else {
        sub_nine[i] = doubled_list[i]
    }
}
console.log("sub nine " + sub_nine)

let total = 0
for (let i = 0; i<sub_nine.length; i++) {
    total += sub_nine[i]
}
console.log(total)

let second_dig = total % 10
console.log(second_dig)

let match = (check_digit == second_dig)
console.log(match)

if (match) {
    alert("That is a valid card number.")
} else {
    alert("Sorry, that number is not valid. Refresh and try again.")
}