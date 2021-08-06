Vue.component ('previous-page', {
    template: `<button @click="$emit('previouspage')" type='button' class='btn btn-dark ml-3 mr-3'>Previous</button>` 
})

Vue.component ('next-page', {
    template: `<button @click="$emit('nextpage')" type='button' class='btn btn-dark ml-3 mr-3'>Next</button>` 
})


new Vue ({
    el:'#app',
    data : {
        quotes: [],
        search: '',
        key: '',
        page: 1,
        last_page: false
    },
    methods : {
        loadQuotes: function () {
            axios({
                url: 'https://favqs.com/api/quotes',
                method: 'get',
                headers: {
                    "Authorization": `Token token="${apiKey}"`
                },
                params: {
                    type: this.key,
                    filter: this.search,
                    page: this.page
                }
            }).then(response => {
                this.quotes = response.data.quotes,
                this.page = response.data.page,
                this.last_page = response.data.last_page
            })
        },
        termSelect(event) {
            key = event.target.value
        },
        nextPage: function () {
            this.page += 1
            this.loadQuotes()
        },
        previousPage: function () {
            this.page -= 1
            this.loadQuotes(this.page)
        }
    },
    mounted: function () {
        axios({
            url: 'https://favqs.com/api/quotes',
                method: 'get',
                headers: {
                    "Authorization": `Token token="${apiKey}"`
                },
        })
        .then (response => {
            this.quotes = response.data.quotes
        })
    },
})
