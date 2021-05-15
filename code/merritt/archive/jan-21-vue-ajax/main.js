const vm = new Vue({
    el: '#app',
    data: {
        results: {}
    },
    methods: {
        loadQuotes: function() {
            axios({
                url: "https://favqs.com/api/quotes",
                method: "get",
                headers: {
                    "Authorization": `Token token="${apiKey}"`
                },
                params: {
                    filter: "steve jobs",
                    type: "author"
                }
            }).then(response => {
                this.results = response.data
            })
        }
    }
})