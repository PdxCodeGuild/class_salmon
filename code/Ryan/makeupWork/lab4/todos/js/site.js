new Vue({
    el: '#app',
    data: {
        newItem: '',

        // Store an array of objects (the todos themselves)
        items: [{
                id: 1,
                name: "clean car",
                completed: false,
            },
            {
                id: 2,
                name: "wash clothes",
                completed: true,
            },
        ]
    },
    // List each todo
    computed: {
        reversedItems() {
            return this.items.slice(0).reverse()
        }
    },
    // Allow the user to add and remove todos
    methods: {
        addItem: function () {
            this.items.push({
                // Increment the id
                id: this.items.length + 1,
                // take in the new item name
                name: this.newItem,
                // default to false completion
                completed: false,
            });
            // reset the add item input
            this.newItem = "";
        },
        // Allow a user to toggle if a task is complete or not
        toggleComplete: function (item) {
            item.completed = !item.completed;
        },
        removeItem: function (item) {
            this.items = this.items.filter((newItem) => newItem.name !== item.name)
        }
    }
})