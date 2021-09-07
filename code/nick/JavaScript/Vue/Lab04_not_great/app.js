let vm = new Vue({
    el: '#app',
    data: {
            completed_tasklist: [],
            input_task: '',
            selected_task: '',
            incomplete_tasklist: [],
    },
    methods: {
        addToList: function() {
            let input = this.input_task
            console.log(input)
            this.incomplete_tasklist.push(input)
            console.log(this.incomplete_tasklist, "incomplete_tasklist")
        },
        addToCompleted: function() {
            console.log(this.selected_task, "selected_task")
            let li = this.selected_task
            console.log(li)
            this.completed_tasklist.push(li)
            console.log(this.completed_tasklist, "completed tasklist")
            this.incomplete_tasklist.remove(selected_task)
        }
    }        
})