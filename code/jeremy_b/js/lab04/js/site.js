const vm = new Vue({
    el: '#app',
    data:{
        todos:[],
        todo: "",
        nextID: 4
    },
    methods: {
        addTodo: function(){
            this.todos.push({id: this.nextID, todo: this.todo, complete: false});
            this.todo = "";
            this.nextID++;
        },
        clearTodo: function (){
            this.todo = "";
        },
        markComplete: function(todo){
            this.todos[this.todos.indexOf(todo)].complete = true;
        },
        markIncomplete: function(todo){
            this.todos[this.todos.indexOf(todo)].complete = false;
        },
        deleteComplete: function(){
            for (let todo of this.todos){
                if (todo.complete === true){
                    console.log(this.todos.indexOf(todo));
                    this.todos.splice(this.todos.indexOf(todo), 1);
                    console.log(this.todos)
                }
            }
        }
    },
    computed: {}
})

