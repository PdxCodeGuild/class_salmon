// let nums = document.getElementById("num").value
// console.log(nums)
let addNumBtn = document.getElementById("add-num")
let submitBtn = document.getElementById("submitBtn")
let results = document.getElementById("results")

// console.log(nums)
// function isNumeric(nums) {
//     return !isNaN(parseFloat(nums))
// }
var list_nums = []
addNumBtn.addEventListener("click", function(event) {
    event.preventDefault() //This should replace the boolean while loop, I think. 
    let nums = document.getElementById("num").value
    console.log(nums)
    function isNumeric(nums) {
        return !isNaN(parseFloat(nums))
    }    
    console.log(isNumeric(nums))
    if (isNumeric(nums) === true) {  //This is supposed to mean is not not a number for the parsefloat of the input https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN
        list_nums.push(parseFloat(nums)) //needs type conversion for the string inputs
        console.log(list_nums)
        let advice = document.createElement("p")
        results.append(advice, String("The number " + String(list_nums) + " has been added to the list."))
        console.log(list_nums)
        // return list_nums
    } else {
        let advice = document.createElement("p")
        results.append(advice, String("This is not a number: " + String(nums)))
        return list_nums
    }
    }
)
console.log(list_nums)
// var sum = list_nums.reduce(function (a, b) {
//     return a + b
//   }, 0)
// console.log(sum)
// var len = list_nums.length
// console.log(len)
//Need to make a calculate average function when the user decides they are done adding all numbers
submitBtn.addEventListener("click", function(event) {
    let sum = list_nums.reduce(function (a, b) {
        return a + b
      }, 0)
    console.log(sum)
    let len = list_nums.length
    console.log(len)
    event.preventDefault()
    let average = sum / len
    let advice = document.createElement("p")
    results.append(advice, String("The average of your list is: " + String(average)))
})
// while (boolean === true) {
//     let num_or_done = prompt("Enter a number or 'done'")
//     if (isNumeric(num_or_done) === true) {  //This is supposed to mean is not not a number for the parsefloat of the input https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN
//         list_nums.push(parseFloat(num_or_done)) //needs type conversion for the string inputs
//         console.log(list_nums)
//         // return list_nums //cannot return unless this is a function
//     } else {
//         break
//         }
// }


// console.log(sum)
// let len = list_nums.length
// console.log(len)
// alert(`The average of your list values are ${sum/len}`)