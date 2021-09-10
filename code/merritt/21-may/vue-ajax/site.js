const vm = new Vue({
    el: '#app',
    data: {
        results: [],
        qotd: {}
    },
    methods: {
        loadQotd: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/qotd/'
            }).then(response => this.qotd = response.data).catch(console.log("error!"))
        },
        loadQuotes: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                headers: {
                    "Authorization": `Token token="${apiKey}"`
                },
                params: {
                    type: 'author',
                    filter: 'abraham lincoln'
                }
            }).then(response => this.results = response.data)
        }
    },
    created: function() {
        this.loadQotd()
    }
})