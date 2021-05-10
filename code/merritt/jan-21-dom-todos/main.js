const newTodoInput = document.getElementById('new-todo-text')
const addTodoBtn = document.getElementById('add-todo')
const incomplete = document.getElementById('incomplete')
const complete = document.getElementById('complete')

function addTodo() {
    const todoText = newTodoInput.value

    const removeBtn = document.createElement('button')
    removeBtn.innerText = "-"
    removeBtn.addEventListener('click', function() {
        this.parentElement.remove()
    })

    const completeBtn = document.createElement('button')
    completeBtn.innerText = "✓"
    completeBtn.addEventListener('click', function() {
        complete.appendChild(this.parentElement)
        this.parentElement.style.textDecoration = 'line-through'
        this.remove()
    })

    const li = document.createElement('li')
    li.innerText = todoText
    li.appendChild(completeBtn)
    li.appendChild(removeBtn)
    incomplete.appendChild(li)
}

addTodoBtn.addEventListener('click', addTodo)
newTodoInput.addEventListener('keyup', function(e) {
    if (e.key === "Enter") {
        addTodo()
    }
})