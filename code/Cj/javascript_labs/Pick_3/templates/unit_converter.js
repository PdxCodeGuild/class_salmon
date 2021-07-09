
// conversion_table = {
//     'mm': .001,
//     'cm': .01,
//     'm': 1,
//     'km': 1000,
//     'in': 0.0254 , 
//     'inch': 0.0254, 
//     'inches': 0.0254, 
//     'ft': 0.3048, 
//     'feet': 0.3048,
//     'miles': 1609.34,
//     'mi':  1609.34,
//     }

// UI = input('Enter number of units: ')
// UI1 = UI.isnumeric()
// while UI1 is False:
//     UI = input('Error: Please input a number: ')
//     UI1 = UI.isnumeric()
// UI = float(UI)
// UI2 = input('What are the input units?: ').lower()
// while UI2 not in conversion_table:
//     UI2 = input('Error! Please enter a valid unit type: ')
// UI3 = input('What is the output units?: ')
// while UI3 == UI2:
//     UI3 = input('Please enter a different valid unit type than the one previously entered: ')
// while UI3 not in conversion_table:
//     UI3 = input('Please enter a valid unit type: ')
// output = UI * conversion_table[UI2] / conversion_table[UI3]
// print(f'{UI} {UI2} converted to {UI3} is {output} {UI3}! ')

function isNumeric(n) {
    return !isNaN(parseFloat(n)) && isFinite(n);
  }

let conversion_table = {
    mm: .001,
    cm: .01,
    m: 1,
    km: 1000,
    in: 0.0254,
    ft: 0.3048,
    miles: 1609.34
}

let ui = prompt("Enter number of units:");
let ui1 = isNumeric(ui);
// console.log(ui1);
while (!ui1) {
    ui = prompt("Enter a NUMBER of units please:");
    ui1 = isNumeric(ui);
}
ui = parseFloat(ui);
// console.log(ui);
let ui2 = prompt("What is the input unit type?");
ui2 = ui2.toLowerCase();
// console.log(ui2);
while (!conversion_table.hasOwnProperty(ui2)) {
    ui2 = prompt("Invalid entry! Enter unit input type: ");
    ui2 = ui2.toLowerCase();
}
let ui3 = prompt("Enter output unit: ")
while (ui3 === ui2) {
    alert("Enter a different unit type than the first.")
    ui3 = prompt("Enter output unit: ")
}
while (!conversion_table.hasOwnProperty(ui3)) {
    ui3 = prompt("Invalid entry! Enter unit input type: ");
    ui3 = ui3.toLowerCase();
}
let output = ui * conversion_table[ui2] / conversion_table[ui3]
console.log(output)
alert(`${ui}${ui2} converted to ${ui3} is ${output}`)
