let conversion_table = {
    mm: .001,
    cm: .01,
    m: 1,
    km: 1000,
    in: 0.0254,
    ft: 0.3048,
    miles: 1609.34
};

let div_container = document.createElement("div");

let body = document.getElementById("body");

let form = document.createElement("form");
form.action = '';
form.method = "post";

body.appendChild(form);

let input_units = document.createElement('select');
    input_units.id = "input-unit"
for (key in conversion_table) {
    let option = document.createElement('option');
    option.value = key;
    option.innerText = key
    input_units.appendChild(option);
}
form.appendChild(input_units)
// let input_units = document.createElement('input')
// input_units.type = "select"

let total_units = document.createElement("input");
total_units.type = "number";
total_units.name = "total-units";
total_units.id = "total-units";
total_units.placeholder = "Enter number of units";

form.appendChild(total_units);

let output_units = document.createElement('select');
    output_units.id = "output-unit"
for (key in conversion_table) {
    let option = document.createElement('option');
    option.value = key;
    option.innerText = key
    output_units.appendChild(option);
}
form.appendChild(output_units);

let submit_btn= document.createElement('input');
    submit_btn.type = "submit";
    submit_btn.value = "Convert";

form.appendChild(submit_btn);

let retsult_container = document.createElement('h4');
    retsult_container.innerText = "";
    body.appendChild(retsult_container)

submit_btn.addEventListener("click", function(event) {
    event.preventDefault();
    let num1 = document.getElementById("input-unit")
    let input_unit = num1.value
    let num2 = document.getElementById("output-unit")
    let output_unit = num2.value
    // console.log(output_unit)
    // console.log(conversion_table[input_unit])
    // console.log(total_units.value)
    let output = total_units.value * conversion_table[input_unit] / conversion_table[output_unit];
    console.log(output)
    retsult_container.innerText = output
})
    // console.log(input_unit)
    


// console.log(output)





