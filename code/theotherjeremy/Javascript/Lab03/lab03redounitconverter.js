let userUnit = prompt(
    'What is your starting unit? \nChoose "ft", "mi", "m", "km", "yard", or "inch"\n  ')
let userDist = prompt('What is the distance?')
let convUnit = prompt('What is the final unit? \nChoose "ft", "mi", "m", "km", "yard", or "inch"')
let meters
const convDict = {'m': 1,
             'ft': .3048,
             'mi': 1609.34,
             'km': 1000,
             'inch': .0254,
             'yard': .9144}

if (userUnit in convDict) {
    meters = parseFloat(userDist) * (convDict[userUnit])
}

let finalDict = {'m': 1,
            'ft': 1/.3048,
            'mi': 1/1609.34,
            'km': 1/1000,
            'inch': 1/.0254,
            'yard': 1/.9144}

let result = meters * (finalDict[convUnit])

alert(`${userDist} ${userUnit} is ${result} ${convUnit}`)
alert('The metric system is superior!!')
