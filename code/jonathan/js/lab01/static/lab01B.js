let unitConverter = {
    'in': 0.0254,
    'ft': 0.3048,
    'yd': 0.9144,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
}



let userValue = document.querySelector("#user-value")
let startingUnits = document.querySelector("#starting-units")
let endingUnits = document.querySelector("#ending-units")
let runButton = document.querySelector("#run-button")

runButton.addEventListener("click", function(event) {
    event.preventDefault()
    console.log(userValue.value)
    function runButton() {
        if (document.getElementById("in").checked) {
            return ("in")
        }
        else if (document.getElementById("ft").checked) {
            return ("ft")
        }
        else if (document.getElementById("yd").checked) {
            return ("yd")
        }
        else if (document.getElementById("mi").checked) {
            return ("mi")
        }
        else if (document.getElementById("m").checked) {
            return ("m")
        }
        else if (document.getElementById("km").checked) {
            return ("km")
        }
    }
})
