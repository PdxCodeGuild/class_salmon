// var todos = []

var app = new Vue({
    el: '#app',
    data: {
        message: 'Welcome to the To-Do List App'
    }
})

var list = new Vue({
    el: '#list',
    data: {
        newItem: '',
        markComplete: '',
        markRemove: '',
        todos: [
            {id: 1, todo: "Pet the bed", completed: false}, 
            {id: 2, todo: "Make the dog", completed: false}, 
            {id: 3, todo: "Mow the dishes", completed: false}, 
            {id: 4, todo: "Wash the lawn", completed: false}, 
            {id: 5, todo: "Take out the furniture", completed: false}, 
            {id: 6, todo: "Dust the trash", completed: false}
        ],
        nextID: 7
    },
    methods: {
        add: function() {
            this.todos.push({id: this.nextID, todo: this.newItem, completed: false})
            this.nextID++
        },
        removeItem: function() {
            console.log("markRemove: " + this.markRemove)
            this.todos.splice((this.markRemove - 1), 1)
        },
        completeItem: function(markComplete) {
            console.log("comp: " + this.todos[(markComplete - 1)]['todo'])
            this.todos[(markComplete - 1)]['completed'] = true
            this.todos[(markComplete - 1)]['todo'].addClass(".strikethrough")
        },
        incompleteItem: function(index) {
            this.todos[index] = this.todos[index]
        }
    }
  })