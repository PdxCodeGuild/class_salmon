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
    taskList.append(newerTask)
    
    checkBtn.addEventListener("click", function (event) {
        event.preventDefault()
              
        newerTask.classList.add("striketext")
    })



})
