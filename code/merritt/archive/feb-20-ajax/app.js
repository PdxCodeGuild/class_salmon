let vm = new Vue({
    el: '#app',
    data: {
        quoteResponse: {}
    },
    methods: {
        loadQuote: function() {
            axios({
                method: "get",
                url: "https://favqs.com/api/qotd",
            }).then(response => {
                this.quoteResponse = response.data;
            })
        }
    },
});