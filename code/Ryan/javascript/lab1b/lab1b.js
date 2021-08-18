console.log("pageload")
const conversion_table = {
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000,
    "yd": 0.9144,
    "in": 0.0254
};

// vv Use this to get the value of the input field vv
const userInput = document.querySelector("#input-distance");

// const units = "(ft/mi/m/km/yd/in)";
// let user_input_distance = userInput.value // Number(prompt("What is the distance?"));
// const user_input_unit = "mi" // prompt(`Convert from unit: ${units}`);
// const user_output_unit = "ft" // prompt(`Convert to unit: ${units}`);
// const converted_distance = (user_input_distance * conversion_table[user_input_unit]) / conversion_table[user_output_unit];
// const output = `${user_input_distance} ${user_input_unit} is ${converted_distance} ${user_output_unit}.`;

document.querySelector("#main-form").onsubmit = function(e){e.preventDefault()};

function converter(inputUnit){

    let userInputDistance = userInput.value
    inputDistance = Number(userInputDistance);
    console.log(conversion_table[inputUnit], "line 25 -> conversion table")
    // inputUnit = inputUnit;
    
    let base_measure = (conversion_table[inputUnit] * inputDistance) / conversion_table["m"];
    console.log(inputDistance, inputUnit,base_measure);

    document.querySelector("#feet").innerHTML = base_measure*conversion_table["ft"];
    document.querySelector("#miles").innerHTML = base_measure*conversion_table["mi"];
    document.querySelector("#meters").innerHTML = base_measure*conversion_table["m"];
    document.querySelector("#kilometers").innerHTML = base_measure*conversion_table["km"];
    document.querySelector("#yards").innerHTML = base_measure*conversion_table["yd"];
    document.querySelector("#inches").innerHTML = base_measure*conversion_table["in"];
    

    // var sleep = function(ms) {
    // let now = Date.now(), end = now + ms;
    // while (now < end) { now = Date.now();}
    // }

    // console.log("foo");
    // sleep(5000);
    // console.log("bar");
}

// console.log(converter("ft", 1))
