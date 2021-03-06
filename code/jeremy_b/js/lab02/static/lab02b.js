/* JS for lab02b */

function get_number(){
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
        0: ""
    };

    return ones[number];
}

// Handle special 10s numbers 10 - 13, 15
function special_tens(number) {
    console.log('number is: ' + number)
    let tens_digit = ''
    // get rid of hundreds digit if it exists
    if (number.length === 3) {
        number.shift();
    }

    //calculate 10s digit
    if (parseInt(number[0]) === 1 && parseInt(number[1]) === 0){
        tens_digit = 'ten';
    } else if (parseInt(number[0]) === 1 && parseInt(number[1]) === 1) {
            tens_digit = 'eleven';
    } else if (parseInt(number[0]) === 1 && parseInt(number[1]) === 2) {
            tens_digit = 'twelve';
    } else if (parseInt(number[0]) === 1 && parseInt(number[1]) === 3) {
            tens_digit = 'thirteen';
    } else if (parseInt(number[0]) === 1 && parseInt(number[1]) === 5) {
            tens_digit = 'fifteen';
    } else if (parseInt(number[0]) === 1 && parseInt(number[1]) === 8) {
            tens_digit = 'eighteen'
    } else {
        tens_digit = tens(number[0])
    }

    return tens_digit;
}



    let x = [4, 6, 7, 9];
    let y = [0, 1, 2, 3, 5, 8];

    let num_to_translate = document.getElementById("number").value.split("");
    console.log(num_to_translate)

    // Translate the number to phrase
    if (num_to_translate.length === 1){
        console.log("In if")
        document.getElementById("translated_number").innerText = ones(parseInt(num_to_translate[0]))
    } else if (num_to_translate.length === 2 && parseInt(num_to_translate[0]) === 1 && y.includes(parseInt(num_to_translate[1]))){
        console.log("In first if else");
        document.getElementById("translated_number").innerText = special_tens(num_to_translate)
    } else if (num_to_translate.length === 2 && parseInt(num_to_translate[0]) === 1 && x.includes(parseInt(num_to_translate[1]))){
        console.log("in second if else")
        document.getElementById("translated_number").innerText = ones(parseInt(num_to_translate[1])) + special_tens(num_to_translate)
    } else if (num_to_translate.length === 2 && parseInt(num_to_translate[0]) !== 1){
        document.getElementById("translated_number").innerText = tens(num_to_translate[0]) + "-" + ones(num_to_translate[1])
    } else if (num_to_translate.length === 3 && parseInt(num_to_translate[1]) === 1 && y.includes(parseInt(num_to_translate[2]))){
        console.log("in third if else")
        document.getElementById("translated_number").innerText = hundreds(num_to_translate[0]) + " " + special_tens(num_to_translate);
    } else if (num_to_translate.length === 3 && parseInt(num_to_translate[1]) === 1 && x.includes(parseInt(num_to_translate[2]))){
        console.log("in fourth if else")
        document.getElementById("translated_number").innerText = hundreds(num_to_translate[0]) + " " + ones(num_to_translate[2]) + tens(num_to_translate[1]);
    } else{
        console.log("in else")
        document.getElementById("translated_number").innerText = hundreds(num_to_translate[0]) + " " + tens(num_to_translate[1]) + "-" + ones(num_to_translate[2]);
    }
}