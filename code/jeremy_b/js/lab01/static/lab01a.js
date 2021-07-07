/**************************************************************
 * Author: Jeremy Bush
 * Project: Programming Bootcamp, JavaScript Lab 1a
 * Version: 1
 * Date: 6/29/2021
 *************************************************************/

// Units for conversion
let units = {
    ft:.3048,
    m:1,
    mi:1609.34,
    km:1000,
    yd:.9144,
    in:.0254
};

let original_len = prompt("Enter original length: ");
console.log(original_len);

let original_units = prompt("Enter original units: ");
console.log(original_units);

let output_units = prompt("Enter output units: ");
console.log(output_units);

if (original_units in units && output_units in units) {
    // convert to meters first.
    let len_meters = parseInt(original_len) * units[original_units]
    console.log(original_len + original_units + " equals " + len_meters + "m")
    // convert to output length.
    let converted_len = len_meters * (1 / units[output_units])
    alert(original_len + original_units + " equals " + converted_len + output_units)
} else {
        alert("Please check your input and output units and try again.")
}