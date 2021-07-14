const vm = new Vue({
    el: '#app',
    data: {
        results: [],
        qotd: {},
        picked: "",
        message:"",
        page: 1
    },
    methods: {
        loadRandom: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                headers: {
                    "Authorization": `Token token="${apiKey}"`
                },
            }).then(response => this.results = response.data).catch(console.log("error!"))
        },
        loadQuotes: function(searchBy,searchFor) {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                headers: {
                    "Authorization": `Token token="${apiKey}"`
                },
                params: {
                    type: searchBy,
                    filter: searchFor,
                    
                },
            }).then(response => this.results = response.data)
        },
        pages: function(){
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                headers: {
                    "Authorization": `Token token="${apiKey}"`
                },
            }).then(response => this.results = response.data)
        }
    },
    mounted: function() {
        this.loadRandom()
    }
})