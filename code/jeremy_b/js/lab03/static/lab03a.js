/**************************************************************
 * Author: Jeremy Bush
 * Project: Programming Bootcamp, LS Lab 3a
 * Version: 1
 * Date: 7/1/2021
 *************************************************************/

/* Average numbers redo, python lab 2 */

// Get numbers to average
user_input = prompt("Enter numbers to average seperated by a comma.");


// Split into array and convert to integers and get sum of entered numbers.
user_input.split(",");
let num_list = user_input.split(',').map(function(item) {
    return parseInt(item, 10);
});

let num_total = 0;
let i = 0;
do{
    num_total += num_list[i];
    i++
} while (i < num_list.length);

//  Get average
let num_avg = num_total/num_list.length;

// Print data to console.
console.log("You entered " + num_list.length.toString() + " numbers.")
console.log("The total sum of numbers entered is " + num_total.toString() + ".")
alert("You entered " + num_list.length.toString() + " numbers.  The total sum of numbers entered is " + num_total.toString() + ". The average of numbers entered is " + num_avg.toFixed(2).toString() + ".")