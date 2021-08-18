const conversion_table = {
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000,
    "yd": 0.9144,
    "in": 0.0254
};

const units = "(ft/mi/m/km/yd/in)";

const user_input_distance = Number(prompt("What is the distance?"));

const user_input_unit = prompt(`Convert from unit: ${units}`);

const user_output_unit = prompt(`Convert to unit: ${units}`);

const converted_distance = (user_input_distance * conversion_table[user_input_unit]) / conversion_table[user_output_unit];

const output = alert(`${user_input_distance} ${user_input_unit} is ${converted_distance} ${user_output_unit}.`);