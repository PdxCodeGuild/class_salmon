var app = new Vue({
    el: '#app',
    data: {
        userInput: '',
        message: "Cj's To Do list",
        todos: []
    },  
    methods: {
        addTask: function() {

            app.todos.push({text:this.userInput, completed: false})
            this.userInput = ''
        },
        removeTask: function(thing) {
            this.todos.splice(this.todos.indexOf(thing),1)
        },
        clearTasks: function() {
            let i = 0
            for (this.todo of this.todos) {
                // console.log('hello')
                if (this.todo.completed === true) {
                    this.todos.splice(i,1)
                    // this.todos.splice(this.todos.indexOf(thing),1)
                    // console.log('yes')
                }
                i++
            }
        },
        strike: function() {
            for (todo of this.todos) {
                if (todo.completed === true) {
                    todo.text.classList.add('strike');
                }
            }
        }
        }
})
