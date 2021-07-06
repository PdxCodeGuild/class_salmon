let submitButton = document.querySelector("#submit")
let taskList = document.getElementById("tasks")
let completed = document.getElementById("completed_tasks")

submitButton.addEventListener("click", function (event) {
    event.preventDefault()
    let newTask = document.getElementById("new_task").value
    newerTask = document.createElement("li")
    newerTask.innerText = newTask
    let removeBtn = document.createElement("button")
    removeBtn.innerText = "-"
    newerTask.appendChild(removeBtn)
    let checkBtn = document.createElement("button")
    checkBtn.innerText = "✓"
    newerTask.appendChild(checkBtn)
    taskList.appendChild(newerTask)
    
    checkBtn.addEventListener("click", function (event) {
        event.preventDefault()
        newerTask.classList.add("striketext")
    })
    removeBtn.addEventListener("click", function(event) {
        event.preventDefault()
        //taskList.removeChild(newerTask)
        this.previousSibling.remove()
        this.remove()
        checkBtn.remove()
    })
    

})


//Both buttons only work on the last item in the list or when there is only one item
/*let nums = document.getElementsByClassName("num")
let submitBtn = document.getElementById("submitBtn")
let results = document.getElementById("results")
let addNumBtn = document.getElementById("add-num")
let form = document.getElementById("form")

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
})*/