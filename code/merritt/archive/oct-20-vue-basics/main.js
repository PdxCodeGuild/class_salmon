var vm = new Vue({
    el: '#app-5',
    data: {
      message: 'Hello Vue.js!',
      newMessage: "",
      newTodo: {},
      completed: false
    },
    methods: {
      reverseMessage: function () {
        this.message = this.message.split('').reverse().join('')
      }
    },
    computed: {
        reverse: function() {
            return this.message.split('').reverse().join('')
        }
    },
    mounted: function() {
        console.log("Hello!")
        this.reverseMessage()
    },
    updated: function() {
        console.log("You updated the page!")
    }
  })