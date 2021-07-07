/**************************************************************
 * Author: Jeremy Bush
 * Project: Programming Bootcamp, JavaScript Lab 2a
 * Version: 1
 * Date: 6/29/2021
 *************************************************************/

// hundreds digit function
function hundreds(number){
    hundreds = {
        1: "one hundred",
        2: "two hundred",
        3: "three Hundred",
        4: "four hundred",
        5: "five hundred",
        6: "six hundred",
        7: "seven hundred",
        8: "eight hundred",
        9: "nine hundred"
    };

    return hundreds[number];
}

// Tens digit
function tens(number){
    tens = {
        1: "teen",  // Only for numbers 14 & 16 - 19
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety",
        0: ""
    };

    return tens[number];
}

// ones digit
function ones(number){
    ones = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        0: "zero"
    };

    return ones[number];
}

// Handle special 10s numbers 10 - 13, 15
function special_tens(number) {
    let tens_digit = ''
    // get rid of hundreds digit if it exists
    if (number.length === 3) {
        number.shift();
    }

    //calculate 10s digit
    if (number[0] === 1 && number[1] === 0){
        tens_digit = 'ten';
    } else if (number[0] === 1 && number[0] in [1, 2, 3, 5]) {
        if (number[1] === 1){
            tens_digit = 'eleven';
        } else if (number[1] === 2) {
            tens_digit = 'twelve';
        } else if (number[1] === 3) {
            tens_digit = 'thirteen';
        } else if (number[1] === 5) {
            tens_digit = 'fifteen';
        }
    } else {
        tens_digit = tens(number[0])
    }

    return tens_digit;
}


// get number to input
let num_to_translate = prompt("Enter an integer between 1 and 999: ").split("");
console.log(num_to_translate)

// Translate the number to phrase
if (num_to_translate.length === 1){
    console.log("In if")
    alert(ones(parseInt(num_to_translate[0])));
} else if (num_to_translate.length === 2 && parseInt(num_to_translate[0]) === 1 && (parseInt(num_to_translate[1]) in [0, 1, 2, 3, 5])){
    console.log("In first if else")
    alert(ones(num_to_translate[1]) + special_tens(num_to_translate));
} else if (num_to_translate.length === 2 && parseInt(num_to_translate[0]) === 1 && (parseInt(num_to_translate[1]) in [4, 6, 7, 8, 9])){
    console.log("in second if else")
    alert(ones(num_to_translate[1]) + special_tens(num_to_translate));
} else if (num_to_translate.length === 3 && parseInt(num_to_translate[1]) === 1 && parseInt(num_to_translate[2] in [0, 1, 2, 3, 5])){
    console.log("in third if else")
    alert(hundreds(num_to_translate[0] + " " + special_tens(num_to_translate)));
} else if (num_to_translate.length === 3 && parseInt(num_to_translate[1]) === 1 && parseInt(num_to_translate[2]) in [4, 6, 7, 8, 9]){
    console.log("in fourth if else")
    alert(hundreds(num_to_translate[0]) + " " + ones(num_to_translate[2]) + tens(num_to_translate[1]));
} else{
    console.log("in else")
    alert(hundreds(num_to_translate[0]) + " " + tens(num_to_translate[1]) + "-" + ones(num_to_translate[2]));
}

