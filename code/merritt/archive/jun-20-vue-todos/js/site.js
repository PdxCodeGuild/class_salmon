Vue.component('todo-item', {
    props: ['todo'],
    data: function() {
        return {
            editing: false
        }
    },
    template: `
    <li>
        <template v-if="editing"><input type="text" v-model="todo.text">  -- {{ todo.completed ? "done" : "not done" }}</template>
        <template v-else>{{ todo.text }} -- {{ todo.completed ? "done" : "not done" }}</template>
        <input type="checkbox" v-model="todo.completed">
        <button @click="toggleEdit">Edit</button>
        <button @click="$emit('remove', todo)">Remove</button>
    </li>`,
    methods: {
        toggleEdit: function() {
            this.editing = this.editing ? false : true;
        }
    }
});

Vue.component('add-todo', {
    data: function() {
        return {
            text: "",
            id: 4 
        }
    },
    template: `
    <div>
        <input type="text" v-model="text" placeholder="what do you need to do?">
        <button @click="add">Add to list</button>
    </div>`,
    methods: {
        add: function (event) {
            this.$emit('add', { text: this.text, completed: false, id: this.id });
            this.newTodo = "";
            this.newTodoId++;
        }
    }
});

let vm = new Vue({
    el: '#app',
    data: {
        todos: [
            { text: "Walk the dog", completed: false, id: 1 },
            { text: "Groceries", completed: true, id: 2 },
            { text: "Laundry", completed: false, id: 3 }
        ]
    },
    methods: {
        addTodo: function (todo) {
            this.todos.push(todo);
        },
        removeTodo: function (todo) {
            this.todos.splice(this.todos.indexOf(todo), 1);
        }
    },
    computed: {
        incompleteTodos: function () {
            return this.todos.filter(function(todo) {
                return todo.completed === false;
            });
        },
        completeTodos: function () {
            return this.todos.filter(function(todo) {
                return todo.completed === true;
            });
        }
    }
})