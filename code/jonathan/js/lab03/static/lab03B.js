let userInput = document.querySelector("#user-input")
let runButton = document.querySelector("#run-btn")

runButton.addEventListener("click", function(event) {
    event.preventDefault()
    let ccF = userInput.value
    let ccS = ccF.split("")
    console.log(ccS)
})