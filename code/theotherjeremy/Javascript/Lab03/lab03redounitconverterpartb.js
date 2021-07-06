let userUnit = document.querySelector('#userUnit')
let convUnits = document.querySelector('#convUnits')
let userDist = document.querySelector('#userDist')



let ddl = document.querySelector('#ddl');
let units = ['feet', 'miles', 'meters', 'kilometers', 'yards', 'inches']
for (let i=0; i<units.length; ++i) {
    let option = document.createElement('option')
        option.innerText = units[i]
        option.value = units[i]
        ddl.appendChild(option)
    }

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

let result = meters * (finalDict[convUnits])

final.onclick = function(evt) {
    result.innerText = userDist + userUnit + "  =  "  + result + convUnits +
    ('The metric system is superior!!')
}



