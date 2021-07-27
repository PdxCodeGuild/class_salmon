const vm = new Vue({
    el: '#app',
    data:{
        todos:[],
        todo: "",
        toDelete: [],
        nextID: 0
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
            // Get index of elements to delete
            for (let i = 0; i < this.todos.length;) {
                if (this.todos[i].complete === true) {
                    this.toDelete.push(i);
                    i++;
                } else {
                    i++;
                }
            }
            this.toDelete.sort();
            console.log(this.toDelete);
            for(let i = this.toDelete.length - 1; i > -1;){
                this.todos.splice(this.toDelete[i], 1);
                i--;
            }
        }

    },
    computed: {}
})

