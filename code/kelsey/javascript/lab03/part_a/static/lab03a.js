//lab 01 Unit Converter

// # Version 1
// # Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.
// foot = {'meters': 0.3048}
// number_of_feet = int(input(f'what is the distance in feet? '))
// print(f"{foot['meters'] * number_of_feet:.4f}")

// # Version 2

// # Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.
// convert_to_meters = {
//     'ft': 0.3048,
//     'mi': 1609.35,
//     'm': 1,
//     'km': 1000,

// #  Version 3
// # Add support for yards, and inches.
//     'yd': 0.9144,
//     'in': 0.0254
// }

// # Version 4
// # Now we'll ask the user for the distance, the starting units, and the units to convert to.

// distance = input("what is the distance? ")
// input_units = input("what are the input units? ")
// output_units = input("what are the output units? ")
// total_meters = int(distance) * convert_to_meters[input_units]
// final_conversion = total_meters / convert_to_meters[output_units]
// print(f'{distance} {input_units} is {final_conversion:.4f} {output_units}')

let numFeet = prompt("Enter number of feet: ")

let toMeters = function (numFeet) {
    return parseInt(numFeet) * 0.3048
}

alert(`${numFeet} ft = ${toMeters(numFeet)} m`)

// version2 & version3

let units = prompt("Enter unit of measurement (ft, mi, m, km, yd, in) to convert to meters: ").toLowerCase()

let convertedUnits = {
    'ft': 0.3048,
    'mi': 1609.35,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254
}

let userChoice = prompt(`Number of ${units}:`)

let conversion = convertedUnits[units] * parseFloat(userChoice)

alert(`${userChoice} ${units} = ${conversion} m`)

// version4

let distance = prompt("What is the distance? Enter number:")
let inputUnits = prompt("What are the input units (ft, mi, m, km, yd, in)?").toLowerCase()
let outputUnits = prompt("What are the output units (ft, mi, m, km, yd, in)?").toLowerCase()

let totalMeters = parseFloat(distance) * convertedUnits[inputUnits]
let finalConversion = totalMeters / convertedUnits[outputUnits]

alert(`${distance} ${inputUnits} = ${finalConversion} ${outputUnits}`)
