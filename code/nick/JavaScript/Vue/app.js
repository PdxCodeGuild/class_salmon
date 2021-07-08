let vm = new Vue({
    el: '#app',
    data: {
        tasklist: []
    },
    methods: {
        task: function() {
            console.log(this.tasklist);
        }

    }
})