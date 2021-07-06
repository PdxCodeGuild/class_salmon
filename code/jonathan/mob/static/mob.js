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
    document.body.appendChild(removeBtn)
    taskList.append(newerTask)
    
    // removeBtn.addEventListener("click", function (event) {
    //     event.preventDefault()
    //     this.previousSibling.remove()
    //     this.remove()
    // })
})

// function myFunction() {
//     var str = "Hello World!";
//     var result = str.strike();
//     document.getElementById("demo").innerHTML = result;
//   }