Vue.component('todo-item', {
    props: ['todo'],
    data: function() {
        return {
            editing : false
        }
    },
    template:
    `<li>
        <template v-if="editing">
            <input type="number" v-model="todo.quantity">
            <input type="text" v-model="todo.text"> 
        </template>
        <template v-else>
            {{ todo.quantity }} -- {{ todo.text }} 
        </template>
        <input type="checkbox" v-model="todo.completed"> 
        <button @click="toggleEdit(todo)">{{ editing ? "Save" : "Edit" }}</button> 
        <button @click="$emit('delete', todo)">Delete</button>
    </li>`,
    methods: {
        toggleEdit: function() {
            this.editing = this.editing ? false : true;
        }
    },
    mounted: function() {
        console.log(`You just mounted a todo called ${this.todo.text}`);
    },
    beforeDestroy: function() {
        console.log(`Say goodbye to ${this.todo.text}`);
    }
})

Vue.component('add-todo', {
    data: function() {
        return {
            newTodo: { text: "", quantity: 1, completed: false, id: 4, editing: false }
        }
    },
    template:
    `<div>
        <h3><slot></slot></h3>
        <input type="number" v-model="newTodo.quantity">
        <input type="text" v-model="newTodo.text" @keyup.enter="add" />
        <button @click="add">add me</button>
    </div>`,
    methods: {
        add: function() {
            this.$emit('add',
                {
                    text: this.newTodo.text,
                    quantity: this.newTodo.quantity,
                    completed: this.newTodo.completed,
                    id: this.newTodo.id,
                    editing: this.newTodo.editing
                }
            );
            this.newTodo.text = "";
            this.newTodo.id++;
        }
    }
})

let vm = new Vue({
    el: '#app',
    data: function() {
        return {
            todos: [
                { text: "Learn Vue", quantity: 1, completed: true, id: 1 },
                { text: "Learn More Vue", quantity: 10, completed: false, id: 2 },
                { text: "Learn React???", quantity: 5, completed: false, id: 3 },
            ],
            message: "Here are some words for you."
        }
    },
    methods: {
        reverseMessage: function() {
            this.message = this.message.split("").reverse().join("");
        },
        addTodo: function(todo) {
            this.todos.push(todo);
        },
        removeTodo: function(todo) {
            this.todos.splice(this.todos.indexOf(todo), 1);
        }
    },
    computed: {
        todoCount: function() {
            return this.todos.length;
        },
        incompleteTodos: function() {
            // return this.todos.filter(function(todo) {
            //     return todo.completed === false;
            // })
            return this.todos.filter(todo => !todo.completed);
        },
        completeTodos: function() {
            return this.todos.filter(todo => todo.completed);
        }
    }
});