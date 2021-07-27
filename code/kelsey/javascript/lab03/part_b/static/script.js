let form = document.querySelector("#form")
let distance = document.querySelector("#distance")
let unitsIn = document.querySelector("#input_units")
let unitsOut = document.querySelector("#output_units")
let btn = document.querySelector("#submit")
let final = document.querySelector("#final")

const toMeters = {
    ft: 0.3048,
    mi: 1609.35,
    m: 1,
    km: 1000,
    yd: 0.9144,
    in: 0.0254
}

btn.addEventListener("click", function(event) {
    event.preventDefault()
    let startingUnits = unitsIn.value
    let calc = parseInt(distance.value) * toMeters[startingUnits] / toMeters[unitsOut.value]
    final.innerText = `${distance.value} ${unitsIn.value} = ${calc} ${unitsOut.value}`
})