const vm = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        nums: [
            {id: 1, number: "2"},
            {id: 2, number: "2"},
            {id: 3, number: "2"},
            {id: 4, number: "2"}
        ],
        nextID: 5
    },
    methods: {
        addNum: function() {
            this.nums.push({id: this.nextID, number: ""})
            this.nextID++
        },
        removeNum: function(num) {
            this.nums.splice(this.nums.indexOf(num),1)
        },
        clearNum: function() {
            this.nums = []
        }
    },
    computed: {
        average: function() {
            let total = 0
            for (let num of this.nums) {
                total += parseFloat(num.number)
            }
            return total / this.nums.length
        }
    }
})