const app = new Vue({
    el: '#app',
    data: {
        title: 'To-Do List',
        newTodo: '',
        todos: []
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
            this.todos.splice(index, 1)
        },
        clear() {
            this.todos = []
        }
    }
})