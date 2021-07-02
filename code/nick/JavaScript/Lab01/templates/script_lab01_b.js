let nums = document.getElementsByClassName("num")
let addNumBtn = document.getElementById("add-num")
let submitBtn = document.getElementById("submitBtn")
let results = document.getElementById("results")

console.log(nums)
function isNumeric(nums) {
    return !isNaN(parseFloat(nums))
}
addNumBtn.addEventListener("click", function(event) {
    event.preventDefault() //This should replace the boolean while loop, I think. 
    let list_nums = []
    if (isNumeric(nums) === true) {  //This is supposed to mean is not not a number for the parsefloat of the input https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN
        list_nums.push(parseFloat(nums)) //needs type conversion for the string inputs
        console.log(list_nums)
    } else {
        break
    }
let sum = list_nums.reduce(function (a, b) {
    return a + b
  }, 0)
console.log(sum)
let len = list_nums.length
console.log(len)
//Need to make a calculate average function when the user decides they are done adding all numbers
addNumBtn.addEventListener("click", function(event) {
    event.preventDefault()
    let average = sum / len
    results.append(average)

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