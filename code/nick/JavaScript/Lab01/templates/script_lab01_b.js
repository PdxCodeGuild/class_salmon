let nums = [5, 0, 8, 3, 4, 1, 6]
let list_nums = []
let boolean = true
console.log(nums)
function isNumeric(num_or_done) {
    return !isNaN(parseFloat(num_or_done))
}
while (boolean === true) {
    let num_or_done = prompt("Enter a number or 'done'")
    if (isNumeric(num_or_done) === true) {  //This is supposed to mean is not not a number for the parsefloat of the input https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN
        list_nums.push(parseFloat(num_or_done)) //needs type conversion for the string inputs
        console.log(list_nums)
        // return list_nums //cannot return unless this is a function
    } else {
        break
        }
}

let sum = list_nums.reduce(function (a, b) {
    return a + b
  }, 0)
console.log(sum);
let len = list_nums.length
console.log(len)
alert(`The average of your list values are ${sum/len}`)