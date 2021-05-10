Vue.component('todo-item', {
  props: ['todo'],
  template:
    `<li>
      <p style="display: inline-block;" v-bind:class="{ completed: todo.isCompleted }" v-bind:style="{ color: todo.color }">{{ todo.text }}</p>
      <input type="checkbox" v-model="todo.isCompleted">
      <button @click="$emit('remove-todo', todo)">✕</button>
    </li>`,
    // <button @click="removeTodo(todo, $event)">✕</button>
  methods: {
    // removeTodo: function (todo, $event) {
    //   let index = this.todos.indexOf(todo);
    //   this.todos.splice(index , 1);

    //   // let index = this.$parent.todos.indexOf(todo);
    //   // this.$parent.todos.splice(index , 1);

    //   // this.$parent.todos = this.$parent.todos.filter(item => item !== todo)
    // }
  },
  mounted: function () {
    console.log(`You mounted the todo item ${this.todo.text}`)
  }
})

let app = new Vue({
  el: '#app',
  data: {
    message: 'Hello world!',
    titleMessage: 'I typed this',
    exists: true,
    todos: [
      { id: 1, text: 'Learn JavaScript', isCompleted: false , color: '#ff7f50' },
      { id: 2, text: 'Learn Vue', isCompleted: true, color: '#008080' },
      { id: 3, text: 'Build something awesome', isCompleted: false, color: '#8b0000' }
    ],
    newTodo: {
      text: '',
      isCompleted: false,
      color: '#000000',
      id: 4
    },
  },
  methods: {
    reverseMessage: function () {
      this.message = this.message.split('').reverse().join('');
    },
    addTodo: function () {
      this.todos.push({ id: this.newTodo.id, text: this.newTodo.text, isCompleted: this.newTodo.isCompleted, color: this.newTodo.color });
      this.newTodo.id++;
    },
    removeTodo: function (todo, $event) {
      let index = this.todos.indexOf(todo);
      this.todos.splice(index , 1);
    }
  },
  mounted: function () {
    console.log(this);
  },
  computed: {
    incompleteTodos: function () {
      return this.todos.filter(todo => !todo.isCompleted)
    },
    completeTodos: function () {
      return this.todos.filter(todo => todo.isCompleted)
    }
  },
  watch: {
    "newTodo.text": function (newValue, oldValue) {
      console.log(`You changed ${oldValue} to ${newValue}.`)
    }
  }
});