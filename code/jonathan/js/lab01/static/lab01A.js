let unitConverter = {
    'in': 0.0254,
    'ft': 0.3048,
    'yd': 0.9144,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
}

let userValue = parseFloat(prompt("Enter a distance please:"))
let userUnits = prompt("And they are which units? (in, ft, yd, mi, m, km):")
let answerUnits = prompt("And you would like the output in what unit? (in, ft, yd, mi, m, km):")

let userTotal = userValue * unitConverter[userUnits]
let rawAnswer = userTotal / unitConverter[answerUnits]
let answer = rawAnswer.toFixed(2)
alert(`${userValue}${userUnits} comes out to ${answer}${answerUnits}.`)