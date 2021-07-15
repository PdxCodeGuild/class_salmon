let app = new Vue({
    el: '#app',
    data: {itemText: '',
        incompleteTodos: [],
        completeTodos: []

    }, 


    methods: {
        addItem: function() {
            console.log(this.itemText)
            this.incompleteTodos.push(this.itemText)
        },
        deleteItem: function() {
            // this.nums.splice(this.nums.indexOf(num),1)      
                   
        },
        strikeItem: function() {



        }
   
   
   
   
   
                }





})
