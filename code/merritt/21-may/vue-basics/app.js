let vm = new Vue({
    el: '#app-5',
    data: {
      message: 'Hello Vue.js!',
      futurePreference: false
    },
    methods: {
      reverseMessage: function () {
        this.message = this.message.split('').reverse().join('')
      }
    },
    computed: {
      reversedMessage: function() {
        return this.message.split('').reverse().join('')
      }
    },
    mounted: function() {
      console.log("Hello world!")
    },
    updated: function() {
      console.log("you changed the page!")
    }
  })