// const items = []


// items.push("Item 1")
// items.push("Item 2")
// items.push("Item 3")
// items.push("Item 4")

const app = Vue.createApp({

    data: function() {
        return{
            items: [
                {id: 1, text: "Text One", completed: false},
                {id: 2, text: "Text Two", completed: true},
                {id: 3, text: "Text Three", completed: true}
            ]
        }
    },

    methods: {
        strikeThrough: function(item) {
            let currentIndex = this.items.indexOf(item);
            console.log(currentIndex);
            console.log(this.items[currentIndex].completed);
            this.items[currentIndex].completed = !this.items[currentIndex].completed;
            console.log(this.items[currentIndex].completed);
        }
    },

})

app.mount("#app") 



// data: {
//     items: [
//       {id: 1, text: "Text One", completed: false},
//       {id: 2, text: "Text Two", completed: true},
//       {id: 3, text: "Text Three", completed: true}
//     ]
//   }
  
  
  
  
//   <---------------HTML--------------->
  
//   <ul v-for="item in items">
//     <li v-if="item.completed"><s>{{item.text}}</s>
//     <li v-else>{{item.text}}
//   </ul>