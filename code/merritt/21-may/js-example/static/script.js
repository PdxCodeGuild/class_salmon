// let titleElement = document.getElementById("title")
// let listItems = document.getElementsByClassName("red")
// let titleElement = document.querySelector("#title")
// let listItems = document.querySelectorAll("li.red")
// let inputElement = document.getElementById("text")
// let btn = document.getElementById("btn")

// titleElement.innerHTML = "<em>Emphasized Title!</em>"
// titleElement.style.border = "1px solid red"

// titleElement.style.backgroundColor = "green"

// titleElement.setAttribute("what-this-does", "i-am-a-title")

// inputElement.name = "more-text"
// inputElement.type = "file"

// for (let i=0; i<listItems.length; i++) {
//     listItems[i].style.backgroundColor = "red"
//     listItems[i].classList.add("classy")
// }
// // listItems[0].style.backgroundColor = "red"

// // console.log(titleElement)
// // console.log(listItems)
// // console.log(inputElement)

// console.log(listItems[0].getAttribute("style"))

// let form = document.createElement("form")
// form.action = ""
// form.method = "post"

// let formInput = document.createElement("input")
// formInput.type = "text"
// formInput.name = "key"
// formInput.placeholder = "enter value here"

// let submitBtn = document.createElement("input")
// submitBtn.type = "submit"
// submitBtn.value = "Submit Form"

// form.appendChild(formInput)
// form.appendChild(submitBtn)

// console.log(form)
// console.log(formInput)

// document.body.appendChild(form)

let nums = document.getElementsByClassName("num")
let submitBtn = document.getElementById("submitBtn")
let results = document.getElementById("results")
let addNumBtn = document.getElementById("add-num")
let form = document.getElementById("form")

console.log(nums)

submitBtn.addEventListener("click", function(event) {
    event.preventDefault()
    let total = 0
    for (let i=0; i<nums.length; i++) {
        total += parseFloat(nums[i].value)
    }
    let average = total / nums.length
    let newTotal = document.createElement("li")
    newTotal.innerText = average
    results.prepend(newTotal)
})

addNumBtn.addEventListener("click", function(event) {
    event.preventDefault()
    let newNum = document.createElement("input")
    newNum.type = "number"
    newNum.classList.add("num")
    let removeBtn = document.createElement("button")
    removeBtn.innerText = "-"
    removeBtn.addEventListener("click", function(event) {
        event.preventDefault()
        this.previousSibling.remove()
        this.remove()
    })

    form.insertBefore(removeBtn, addNumBtn)
    form.insertBefore(newNum, removeBtn)
})