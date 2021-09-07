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
            console.log("matches: " + matches)
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

let bal = 0

let rounds = 0
while (rounds < 100000) {
    rounds++
    bal -= 2
    let matches = num_matches(winning_tick)
    bal += money_won(matches)
}

// console.log("bal: " + bal)

if (play == true) {
    alert("Thanks for choosing to play.") 
    const winning_tick = pick6()
    alert(`A winning ticket has been chosen.
    
    Winning ticket: ${winning_tick}`)
    console.log("winning tick: " + winning_tick)
    
    let bal = 0
    
    let rounds = 0
    while (rounds < 100000) {
        rounds++
        bal -= 2
        let matches = num_matches(winning_tick)
        bal += money_won(matches)
    }
    
    console.log("bal: " + bal)
    const ROI = bal / 200000
    // console.log("roi: " + ROI)
    alert(`Your final balance after 100,000 rounds is $${bal.toLocaleString()}.`)
    alert(`That means you earned $${(bal + 200000).toLocaleString()}.`)
    alert("And you spent $200,000.")
    alert(`Your ROI was ${Math.round((ROI) * 100)}%.`)
    alert("I recommend you not quit your day job. And don't go to Vegas.")
} else {
    alert("Okay, you don't want to play. If you change your mind, simply refresh the page.")
}
