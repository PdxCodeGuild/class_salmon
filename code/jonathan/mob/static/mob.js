let submitButton = document.querySelector("#submit")
let taskList = document.getElementById("tasks")

submitButton.addEventListener("click", function(event) {
    event.preventDefault()
    let newTask = document.getElementById("new_task").value
    newerTask = document.createElement("li")
    newerTask.innerText = newTask
    tasks.prepend(newerTask)
})