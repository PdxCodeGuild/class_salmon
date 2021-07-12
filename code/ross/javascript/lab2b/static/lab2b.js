function pick6() {
    let ticket = ['','','','','','']
    let i = 0
    while (i < 6) {
        let num = Math.floor(Math.random()*99)

        // console.log("num: " + num)
        ticket[i] = num
        // console.log("ticket: " + ticket)
        // console.log("i:" + i)
        i++
    }
    // console.log(ticket)
    return ticket
}

function num_matches(winning_tick) {
    // console.log("win: " + winning_tick)
    let player_tick = pick6()
    // console.log("player: " + player_tick)
    let matches = 0
    let x = 0
    while (x < 6) {
        if (winning_tick[x] == player_tick[x]) {
            matches++
            // console.log("matches: " + matches)
            x++
        } else {
            x++
        }
    }
    // console.log("win: " + winning_tick)
    // console.log("player: " + player_tick)
    // console.log("matches: " + matches)
    return matches
}

function money_won(matches) {
    if (matches == 0) {
        return 0
    } else if (matches == 1) {
        return 4
    } else if (matches == 2) {
        return 7
    } else if (matches == 3) {
        return 100
    } else if (matches == 4) {
        return 50000
    } else if (matches == 5) {
        return 1000000
    } else if (matches == 6) {
        return 25000000
    }
}

const winning_tick = pick6()
// console.log("winning tick: " + winning_tick)

let yes = document.querySelector('#yes_btn')
// console.log("yes: " + yes)
let no = document.querySelector('#no_btn')


//  Proceed option pops up after game is explained
let proceed = document.querySelector('#proceed')
proceed.style.display = 'none'

// Option to submit the desired number of rounds
let submit = document.querySelector("#submit")
submit.style.display = 'none'

yes.onclick = function() {
    yes.style.visibility = "hidden"
    no.style.visibility = "hidden"
    document.getElementById("chose_to_play1").innerHTML = "<p>Thanks for choosing to play. This will be fun!</p>"
    document.getElementById("chose_to_play2").innerText = "A winning ticket has been chosen."    
    document.getElementById("chose_to_play3").innerHTML = "<p>Winning ticket:</p>"   
    document.getElementById("win_tik").innerText = winning_tick 
    proceed.style.display = 'block' 
}

// Puts the round choice form into hiding until called
var user_rounds = document.querySelector('#user_rounds')
// console.log("user rounds: " + user_rounds)
user_rounds.style.display = 'none'
// console.log("user rounds: " + user_rounds.value)

proceed.onclick = function(){
    proceed.style.display = "none"
    document.querySelector("#user_rounds").innerHTML = 'type="text" placeholder="How many rounds would you like to play?'
    user_rounds.style.display = 'block'
    user_rounds = user_rounds.value
    // console.log("user rds: " + user_rounds)
    submit.style.display = 'block'
}

submit.onclick = function() {
    user_rounds = document.querySelector('#user_rounds')
    user_rounds = user_rounds.value
    let bal = 0
    // console.log(user_rounds)    
    let rounds = 0
    while (rounds < user_rounds) {
        rounds++
        bal -= 2
        let matches = num_matches(winning_tick)
        bal += money_won(matches)
        // console.log("bal: " + bal)
    }
    var str_rounds = user_rounds.toString()
    var str_bal = bal.toLocaleString()
    // console.log(bal)
    const ROI = bal / 200000
    document.getElementById("results1").innerText = "Your final balance after " + str_rounds + " rounds is $" + str_bal + "."
    document.getElementById("results2").innerText = "That means you earned $" + (bal + (user_rounds * 2)).toLocaleString() + "."    
    document.getElementById("results3").innerHTML = "And you spent $" + (2 * user_rounds) + "."
    document.getElementById("results4").innerText = "Your ROI was " + `${Math.round((ROI) * 100)}` + "%."
}

no.onclick = function() {
    alert("Okay, you don't want to play. If you change your mind, simply go back and click the 'Yes' button.")
}
