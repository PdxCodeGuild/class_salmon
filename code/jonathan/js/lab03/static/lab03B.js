function greaterThanNine(num) {
    if (num > 9) {
        num -= 9
    }
    else {   
        num -= 0
    }
    return num
}

let runButton = document.querySelector("#run-button")

runButton.addEventListener("click", function(event) {
    event.preventDefault()
    let userCC = document.getElementById("textarea")
    let newUserCC = parseFloat(userCC.value)
    console.log(newUserCC)
    let userCCList = newUserCC.split("")
    let checkDigit = newUserCC.pop()
    let reverseUserCCList = userCCList.reverse()
    for (let i = 0; i < reverseUserCCList.length; i += 2) {
    reverseUserCCList[i] *= 2;}
    let doubleList = reverseUserCCList
    let newList = doubleList.map(greaterThanNine)
    let sumNum = newList.reduce(function(a, b){
        return a + b;
    }, 0)
    let lastCheck = sumNum % 10
    if (lastCheck == checkDigit) {
        alert("Valid.")
    } 
    else {
        alert("Sorry, that is not valid.")
    }
})