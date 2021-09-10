const vm = new Vue({
    el: '#app',
    data: {
        todos: [
            {id: 1, text: "Wag the dog", completed: false},
            {id: 2, text: "Buy more milk", completed: false},
            {id: 3, text: "Stare at the sky", completed: false}
        ],
        newTodo: {id: 4, text: "", completed: false}
    },
    methods: {
        addTodo: function() {
            this.todos.push({
                id: this.newTodo.id,
                text: this.newTodo.text,
                completed: this.newTodo.completed
            })
            this.newTodo.text = ""
            this.newTodo.id++
        },
        removeTodo: function(todo) {
            this.todos.splice(this.todos.indexOf(todo), 1)
        }
    },
    computed: {
        incompleteTodos: function() {
            // let incompleteTodos = []
            // for (let i=0; i<this.todos.length; i++) {
            //     if (this.todos[i].completed === false) {
            //         incompleteTodos.push(this.todos[i])
            //     }
            // }
            // return incompleteTodos
            return this.todos.filter(function(todo) {
                return todo.completed === false
            })
        },
        completeTodos: function() {
            return this.todos.filter(function(todo) {
                return todo.completed === true
            })
        }
    }
})