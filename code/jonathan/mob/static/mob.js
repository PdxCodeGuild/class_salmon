let submitButton = document.querySelector("#submit")
let taskList = document.querySelector("#tasks")
let completed = document.querySelector("#completed_tasks")
let newTask = document.querySelector("#new_task")


submitButton.addEventListener("click", function (event) {
    event.preventDefault()
    newerTask = document.createElement("li")
    newerTask.innerText = newTask.value
    newerTask.setAttribute('id', 'taskItem')
    // let currentTask = document.querySelector('#taskItem')
    let removeBtn = document.createElement("button")
    removeBtn.innerText = "-"
    newerTask.appendChild(removeBtn)
    let checkBtn = document.createElement("button")
    checkBtn.innerText = "✓"
    newerTask.appendChild(checkBtn)
    taskList.appendChild(newerTask)
    checkBtn.addEventListener("click", function (event) {
        event.preventDefault()
        // newerTask.classList.add("striketext")
        // let completedTask = document.createElement("li") 
        event.target.parentNode.classList.add('striketext')
        // event.target.parentNode.completed.appendChild(newerTask)
        // completedTask.appendChild(newerTask)
        // console.log(event.target.parentNode('#text'))
    })
    removeBtn.addEventListener("click", function(event) {
        event.preventDefault()
        event.target.parentNode.remove(newerTask)
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