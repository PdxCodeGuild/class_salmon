/**************************************************************
 * Author: Jeremy Bush
 * Project:
 * Version: 1
 * Date:
 *************************************************************/

// Build HTML form

let orgUnitsOptions = ["in", "ft", "m", "yd", "km", "mi"];

let br = document.createElement("br");

let form = document.createElement('form');

let orgLengthLabel = document.createElement('label');
orgLengthLabel.for = "numsToAvg";
orgLengthLabel.id = "orgLengthLabel";
orgLengthLabel.innerHTML = "Enter length: "

let orgLength = document.createElement("input");
orgLength.type = "number";
orgLength.id = "orgLength";
orgLength.name = "numsToAvg";

let orgUnitsLabel = document.createElement("label");
orgUnitsLabel.for = "orgUnits";
orgUnitsLabel.innerHTML = "From Units: ";

let orgUnits = document.createElement("select");
orgUnits.id = "orgUnits";
orgUnits.name = "orgUnits";

for (let unit of orgUnitsOptions){
    let option = document.createElement("option");
    option.value = unit;
    option.innerHTML = unit;
    orgUnits.appendChild(option);
}

let conUnitsLabel = document.createElement("label");
conUnitsLabel.for = "conUnits";
conUnitsLabel.innerHTML = "To Units: ";

let conUnits = document.createElement("select");
conUnits.id = "conUnits";
conUnits.name = "conUnits"

for (let unit of orgUnitsOptions){
    let option = document.createElement("option");
    option.value = unit;
    option.innerHTML = unit;
    conUnits.appendChild(option);
}

let button = document.createElement("button");
button.setAttribute("onClick", "unitConverter()");
button.type = "submit";
button.onClick = "unitConverter()";
button.innerHTML = "Convert";

// Append everything to form
form.appendChild(orgLengthLabel);
form.appendChild(orgLength);
form.appendChild(br);
form.appendChild(orgUnitsLabel);
form.appendChild(orgUnits);
form.appendChild(br);
form.appendChild(conUnitsLabel);
form.appendChild(conUnits);
form.appendChild(br);
form.appendChild(button);

// append to body
document.getElementsByTagName("body")[0].appendChild(form);

function unitConverter() {
    let units = {
        ft: .3048,
        m: 1,
        mi: 1609.34,
        km: 1000,
        yd: .9144,
        in: .0254
    };

    let original_len = document.getElementById("orgLength").value;
    console.log(original_len);

    let original_units = document.getElementById("orgUnits").value;
    console.log(original_units);

    let output_units = document.getElementById("conUnits").value;
    console.log(output_units);

    // convert to meters first.
    let len_meters = parseInt(original_len) * units[original_units];
    console.log(original_len + original_units + " equals " + len_meters + "m");
    // convert to output length.
    let converted_len = len_meters * (1 / units[output_units]);
    document.getElementById("convertedNum").innerHTML = original_len + original_units + " equals " + converted_len + output_units;
    console.log(original_len + original_units + " equals " + converted_len + output_units);
    event.preventDefault();
}