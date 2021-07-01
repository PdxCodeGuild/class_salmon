//This is a JS version of lab2 python; Average numbers
// nums = [5, 0, 8, 3, 4, 1, 6]
// list = []
// boolean = True
// while boolean == True:
//     num_or_done = input("Enter a number or 'done'")
//     if num_or_done.isnumeric():
//         list.append(float(num_or_done))
//     elif num_or_done == 'done':
//         boolean = False
//         break

// average_from_user = sum(list)/len(list)
// print(f'The average of your list values are {average_from_user}.')

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
    return a + b;
  }, 0);
console.log(sum);
let len = list_nums.length
console.log(len)
alert(`The average of your list values are ${sum/len}`)