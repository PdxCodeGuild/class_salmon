// const vm = new Vue({
//   el: '#app',
//   delimiters: ['[[', ']]'],
//   data: {
//       nums: [
//           {id: 1, number: "2"},
//           {id: 2, number: "2"},
//           {id: 3, number: "2"},
//           {id: 4, number: "2"}
//       ],
//       nextID: 5
//   },
//   methods: {
//       addNum: function() {
//           this.nums.push({id: this.nextID, number: ""})
//           this.nextID++
//       },
//       removeNum: function(num) {
//           this.nums.splice(this.nums.indexOf(num),1)
//       },
//       clearNum: function() {
//           this.nums = []
//       }
//   },
//   computed: {
//       average: function() {
//           let total = 0
//           for (let num of this.nums) {
//               total += parseFloat(num.number)
//           }
//           return total / this.nums.length
//       }
//   }
// })
const vm = new Vue({
  el: '#app',
  data: {
    newTodoText: '',
    todos: [],
    completeTodos:[],
    nextTodoId: 1
  },
  methods: {
    addNewTodo: function () {
      if(this.newTodoText != ""){
      this.todos.push({
        id: this.nextTodoId++,
        value: this.newTodoText,
        completed: false
      })
    }
      this.newTodoText = ''
    },
    toggleComplete: function (todo) {
      todo.completed = !todo.completed;
    },
    removeTodo: function(todo) {
      this.todos.splice(this.todos.indexOf(todo),1)
    }
  }
})