function validator() {
    let number = save_num()
    let card_list = cardtolist(number)
    console.log("card list: " + card_list)
    let match = parse(card_list)
    results(match)
}

function save_num() {
    let number = document.getElementById("cardnum")
    number = number.value
    let form = document.getElementById('cardnum')
    form.setAttribute('hidden', '')
    console.log("num: " + number)
    const sub_btn = document.getElementById("validate")
    sub_btn.setAttribute('hidden', '')
    return number
}


function cardtolist(number){
    var card_list = String(number).split("").map((number)=>{
        return Number(number)
    })
    return card_list
}

function parse(card_list) {
    let check_digit = card_list.pop()
    console.log(card_list)
    console.log("check dig: " + check_digit)

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
    return match
}

function results(match) {
    let results = document.querySelector("#results")
    if (match) {
        results.innerHTML = '<p>Thank you. Your credit card has been successfully validated.</p>'
    } else {
        results.innerHTML = '<p>Sorry. We could not validate your credit card. Please refresh and try again.</p>'
    }
}