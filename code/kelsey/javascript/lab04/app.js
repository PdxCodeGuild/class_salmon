
const app = new Vue({
    el: '#app',
    data: {
        title: 'To-Do List',
        newTodo: '',
        todos: [],
        completed: []
    },
    methods: {
        addTodo() {
            this.todos.push({
                task: this.newTodo,
                done: false
            })
            this.newTodo = ''
        },
        removeTodo(todo) {
            const index = this.todos.indexOf(todo)
            this.completed.splice(index, 1)
        },
       
        completedTodo(todo) {
            const index = this.todos.indexOf(todo)
            this.todos.splice(index, 1)
            this.completed.push(todo)
        },
        clear() {
            this.completed = []
        },
    }
})