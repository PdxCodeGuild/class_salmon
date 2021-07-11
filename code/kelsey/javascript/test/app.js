var todos = ["Pet the bed", "Make the dog", "Mow the dishes", "Wash the lawn", "Take out the furniture", "Dust the trash"]
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
      todos
    }
  })

var add = new Vue({
    el: '#add',
    data: {
        newItem: '',
        todos
    }
})

var removeI = new Vue({
    el: '#removeI',
    data: {
        todos
    }
})