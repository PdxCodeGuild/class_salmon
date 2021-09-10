
function pic6() {
    let numbers = []
    for (let i=0; i<6; i++) {
        let number = Math.floor(Math.random() * 100)
        numbers.push(number)
    }return numbers
}


function numMatches(){
    let winningNums = pic6();
    let balance = 0
    let prizes = {
        0:0,
        1:4,
        2:7,
        3:100,
        4:50000,
        5:1000000,
        6:25000000
    }
    for (let i=0; i<100000; i++){
        let entryNums =  pic6();
        let matches = 0;
        for (let i=0; i<6; i++){
            if (winningNums[i] === entryNums[i]){
                matches++
            }
        }
        balance = balance + prizes[matches] - 2
        console.log(balance)

    }
    return balance
}
let play = document.getElementById("play")

play.addEventListener("click", function(event) {
    event.preventDefault()
    let endbalance = numMatches()
    let results = document.getElementById("results")
    results.innerText = "Your ending balance after 100,000 tickest is $" + endbalance + " and your roi is " + ( endbalance + 200000 -200000 ) / 2000 + "%."
})