let unitConverter = {
    'in': 0.0254,
    'ft': 0.3048,
    'yd': 0.9144,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
}

let userValue = document.querySelector('#user_value');
value_button.onclick = function() {
    let newUserValue = userValue.value;
    let newNumValue = parseFloat(newUserValue)
    console.log(newNumValue)
    return newNumValue
}
let userUnits = document.querySelector('#user_units');
unit_button.onclick = function() {
    let newUserUnits = userUnits.value;
    console.log(newUserUnits)
    return newUserUnits
}
let answerUnits = document.querySelector('#answer_units');
answer_button.onclick = function() {
    let newAnswerUnits = answerUnits.value;
    console.log(newAnswerUnits)
    return newAnswerUnits
}
let run_button = document.querySelector('#run_button')
run_button.onclick = function(unitConverter, newUserUnits) {
    console.log(unitConverter[newUserUnits])

    //let userTotal = newNumValue * unitConverter[newUserUnits]
    //let rawAnswer = userTotal / unitConverter[newAnswerUnits]
    //let answer = rawAnswer.toFixed(2)
    //console.log(answer)
    //alert(`${userValue}${userUnits} comes out to ${answer}${answerUnits}.`)
}