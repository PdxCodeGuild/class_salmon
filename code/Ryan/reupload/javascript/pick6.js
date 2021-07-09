// Pick 6 random numbers between 1 - 99.
const ticketGen = (numOfTix = prompt("How many tickets would you like to generate?")) => {
    const randNum = (min = 1, max = 99) => Math.floor(Math.random() * (max-min + 1) + min);

    const ticket = () => {
        let ticket = []
        for(let numInTicket = 0; numInTicket < 6; numInTicket++){
            ticket.push(randNum())
        } return ticket
    };

    let tickets = []
    for(i = 0; i < numOfTix; i++){ 
        tickets.push(ticket())
    }
    
    return tickets
}

const masterTicket = [1,2,3,4,5,6];
const playerTickets = [
    [1,99,98,97,96,95], 
    [1,2,99,98,97,96], 
    [1,2,3,99,98,97], 
    [1,2,3,4,99,98],
    [1,2,3,4,5,99],
    [1,2,3,4,5,6]
];


console.log(masterTicket[0]);
console.log(playerTickets[0][0]);

// Player picks their own number
const playerTicketGen = () => {
    let playerTicket = [];
    for(i = 0; i < 6; i ++){
        let playerPick = prompt("Pick a number between 1-99")
        playerTicket.push(playerPick)
    }
    return playerTicket;
}

// let isEqual = masterTicket.every((value, index) => value === playerTickets[5][index]);
// console.log(isEqual);

// const playerTicket = playerTicketGen()

// let counter = 0
// for(i = 0; i < 6; i ++){
//     let isEqual = masterTicket.length === playerTickets.length && masterTicket.every((value, index) => value === playerTickets[index]);
//     console.log(isEqual);
    
//     if(isEqual === true){
//         counter ++
//     }console.log(counter)
// }

    // for(i = 0; i < 6; i ++){
    //     console.log(playerTickets[i])
    //     // const matching_nums = playerTickets[i].filter(num => {
    //     //         return num[i] === masterTicket[i]
    //     //     }
    //     // )
    // }

const payout = (match_results) => {
    switch(match_results.length){
    case 1:
        console.log("1 match")
    case 2:
        console.log("2 match")
    case 3:
        console.log("3 match")
    case 4:
        console.log("4 match")
    case 5:
        console.log("5 match")
    case 6:
        console.log("6 match")
    case 0:
        console.log("No matches")
    }
    match_results = []
} 

const match_results = []
let counter = 0
while(counter < playerTickets.length){

    // console.log(playerTickets[counter])

    // var matching_nums = 0

    playerTickets[counter].forEach(num => {
        // console.log(num)
        for(i = 0; i < 6; i ++){
                if(num === masterTicket[i]) {
                    // matching_nums += 1
                    match_results.push(num)
                }
            // console.log(matching_nums)
        }
        // console.log(matching_nums)
        
    })
    payout(match_results)

    // console.log(matching_nums)

    counter++
}

console.log(payout())
