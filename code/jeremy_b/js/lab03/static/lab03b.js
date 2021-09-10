/**************************************************************
 * Author: Jeremy Bush
 * Project: JS Lab 3b
 * Version: 1
 * Date: 8/27/2021
 *************************************************************/

function calcAvg() {
// Get numbers to average
    let user_input = document.getElementById('numsToAvg').value.split(",")
    console.log(user_input)
    let num_list = user_input.map(function (item) {
        return parseInt(item, 10);
    });
    console.log(num_list)
    let num_total = 0;
    let i = 0;
    do {
        num_total += num_list[i];
        i++
    } while (i < num_list.length);

//  Get average
    let num_avg = num_total / num_list.length;

// Print data to console.
    console.log("You entered " + num_list.length.toString() + " numbers.")
    console.log("The total sum of numbers entered is " + num_total.toString() + ".")
    document.getElementById("prtAvg").innerText = "You entered " + num_list.length.toString() + " numbers.  The total sum of numbers entered is " + num_total.toString() + ". The average of numbers entered is " + num_avg.toFixed(2).toString() + ".";
}