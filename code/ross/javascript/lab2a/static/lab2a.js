let ticket = ['','','','','','']

function pick6() {
    let i = 0
    while (i < 6) {
        let num = Math.round(Math.random()*99)
        // console.log("num: " + num)
        ticket[i] = num
        // console.log("ticket: " + ticket)
        // console.log("i:" + i)
        i++
    }
    // console.log(ticket)
    return ticket
}

function num_matches(winning_tick, player_tick=pick6()) {
    console.log("win: " + winning_tick)
    console.log("player: " + player_tick)
    let matches = 0
    let x = 6
    while (x < 6) {
        if (winning_tick[x] == player_tick[x]) {
            matches++
            console.log("matches: " + matches)
            x++
        } else {
            x++
        }
    }
    console.log("matches: " + matches)
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

var winning_tick = pick6()

let bal = 0

let rounds = 0
while (rounds < 100) {
    rounds++
    bal -= 2
    let matches = num_matches(winning_tick)
    bal += money_won(matches)
}

console.log("bal: " + bal)


const ROI = bal / 200000
console.log("roi: " + ROI)
// alert(`"Your final balance after 100,000 rounds is $${bal}."`)
// alert(`"That means you earned $${bal + 200000}"`)
// alert("And you spent $200,000.")
// alert(`"Your ROI was ${Math.round(ROI, 2) * 100}%."`)