let vm = new Vue({
    el: '#app',
    data: {
            completed_tasklist: [],
            input_task: '',
            incomplete_tasklist: [],
    },
    methods: {
        addToList: function() {
            let input = this.input_task
            console.log(input)
            this.incomplete_tasklist.push(input)
            console.log(this.incomplete_tasklist, "incomplete_tasklist")
        }
    }        
})