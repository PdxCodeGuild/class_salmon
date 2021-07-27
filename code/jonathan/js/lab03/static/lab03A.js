function greaterThanNine(num) {
    if (num > 9) {
        num -= 9
    }
    else {   
        num -= 0
    }
    return num
}

let userCC = prompt("Please enter your credit card number")

let userCCList = userCC.split("")
//console.log(userCCList)

let checkDigit = userCCList.pop()
//console.log(checkDigit)

let reverseUserCCList = userCCList.reverse()
//console.log(reverseUserCCList)

for (let i = 0; i < reverseUserCCList.length; i += 2) {
    reverseUserCCList[i] *= 2;}

let doubleList = reverseUserCCList
//console.log(doubleList)

let newList = doubleList.map(greaterThanNine)
//console.log(newList)

let sumNum = newList.reduce(function(a, b){
    return a + b;
}, 0)
//console.log(sumNum)

let lastCheck = sumNum % 10
//console.log(lastCheck)

if (lastCheck == checkDigit) {
    alert("Valid.")
} 
else {
    alert("Sorry, that is not valid.")
}