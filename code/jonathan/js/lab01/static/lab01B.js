let unitConverter = {
    'in': 0.0254,
    'ft': 0.3048,
    'yd': 0.9144,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
}

let userValue = document.querySelector("#user-value")
let runButton = document.querySelector("#run-button")
let startingUnits = document.getElementsByName("starting-units")
let endingUnits = document.getElementsByName("ending-units")
let results = document.getElementById("results")

runButton.addEventListener("click", function(event) {
    event.preventDefault()
    let newUserValue = parseFloat(userValue.value)
    for (var i = 0, length = startingUnits.length; i < length; i++) {
    if (startingUnits[i].checked) {
        let userStartingUnits = startingUnits[i].value
        let userTotal = newUserValue * unitConverter[userStartingUnits]
        for (var i = 0, length = endingUnits.length; i < length; i++) {
        if (endingUnits[i].checked) {
            let userEndingUnits = endingUnits[i].value
            let rawAnswer = userTotal / unitConverter[userEndingUnits]
            let answer = rawAnswer.toFixed(2)
            newAnswer = document.createElement("li")
            newAnswer.innerText = answer
            results.prepend(newAnswer)
        }
    }
        }
    }    
    
    
})