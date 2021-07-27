let submitButton = document.querySelector("#submit")
let taskList = document.querySelector("#tasks")
let completed = document.querySelector("#completed_tasks")
let newTask = document.querySelector("#new_task")

submitButton.addEventListener("click", function (event) {
    event.preventDefault()
    let newerTask = document.createElement("li")
    newerTask.innerText = newTask.value
    newTask.value = ""
    newerTask.setAttribute('id', 'taskItem')
    let removeBtn = document.createElement("button")
    removeBtn.innerText = "-"
    newerTask.appendChild(removeBtn)
    let checkBtn = document.createElement("button")
    checkBtn.innerText = "✓"
    newerTask.appendChild(checkBtn)
    taskList.appendChild(newerTask)
    checkBtn.addEventListener("click", function (event) {
        event.preventDefault()
        taskList.removeChild(newerTask)
        completed.appendChild(newerTask)
        event.target.parentNode.classList.add('striketext')
    })
    removeBtn.addEventListener("click", function(event) {
        event.preventDefault()
        event.target.parentNode.remove(newerTask)
    })
})