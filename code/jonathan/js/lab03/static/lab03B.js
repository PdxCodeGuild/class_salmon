function greaterThanNine(num) {
    if (num > 9) {
        num -= 9
    }
    else {   
        num -= 0
    }
    return num
}

let userInput = document.querySelector("#user-input")
let runButton = document.querySelector("#run-btn")
let results = document.querySelector("#results")
let linebreak = document.createElement("br")

runButton.addEventListener("click", function(event) {
    event.preventDefault()
    let ccValue = userInput.value
    //console.log(ccValue)
    let ccSplit = ccValue.split("")
    //console.log(ccSplit)
    let checkDigit = ccSplit.pop()
    //console.log(checkDigit)
    let reverseUserCC = ccSplit.reverse()
    //console.log(reverseUserCC)
    for (let i = 0; i < reverseUserCC.length; i += 2) {
        reverseUserCC[i] *= 2;}
    let doubleCC = reverseUserCC
    //console.log(doubleCC)
    let nineList = doubleCC.map(greaterThanNine)
    //console.log(nineList)
    let sumList = nineList.reduce(function(a, b){
        return a + b;
    }, 0)
    console.log(sumList)
    let lastCheck = sumList % 10
    //console.log(lastCheck)
    if (lastCheck == checkDigit) {
        results.prepend(linebreak)
        results.prepend("Your credit card is valid.")
    } 
    else {
        results.prepend(linebreak)
        results.prepend("Sorry, that is not valid.")
    }
})