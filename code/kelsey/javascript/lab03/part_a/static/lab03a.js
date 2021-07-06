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