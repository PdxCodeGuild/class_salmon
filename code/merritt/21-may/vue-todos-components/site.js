Vue.component('add-todo', {
    data: function() {
        return {
            id: 4,
            text: ""
        }
    },
    template: `
    <div>
        <input type="text" placeholder="What do you want to do?" v-model="text" @keydown.enter="addTodo">
        <button @click="addTodo">Add to List</button>
    </div>
    `,
    methods: {
        addTodo: function() {
            this.$emit('add', {text: this.text, completed: false, id: this.id})
            this.text = ""
            this.id++
        },
    }
})

Vue.component('todo-item', {
    data: function() {
        return {
            editMode: false
        }
    },
    props: ['todo'],
    template: `
    <p>
        <input v-if="editMode" type="text" v-model="todo.text">
        <template v-else>{{ todo.text }}</template>
        <input type="checkbox" v-model="todo.completed">
        <button @click="toggleEdit">{{ editMode ? "Done" : "Edit" }}</button>
        <button @click="$emit('remove', todo)">-</button>
    </p>
    `,
    methods: {
        toggleEdit: function() {
            this.editMode = this.editMode ? false : true
        }
    },
    mounted: function() {
        console.log(`mounted ${this.todo.text}`)
    },
    destroyed: function() {
        console.log(`removed ${this.todo.text}`)
    }
})

const vm = new Vue({
    el: '#app',
    data: {
        todos: [
            {id: 1, text: "Wag the dog", completed: false},
            {id: 2, text: "Buy more milk", completed: false},
            {id: 3, text: "Stare at the sky", completed: false}
        ],
    },
    methods: {
        addTodo: function(payload) {
            this.todos.push(payload)
        },
        removeTodo: function(payload) {
            this.todos.splice(this.todos.indexOf(payload), 1)
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