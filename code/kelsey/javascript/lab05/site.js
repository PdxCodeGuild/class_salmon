Vue.component('show-results', {
    props: ["results"],
    data: function () {
        return {
            results: this.results
        }
    },
    template: `<div v-for="result in results">{{ result.body }}</div>`
})

const vm = new Vue({
    el: '#app',
    data: {
        results: null,
        searchSelect: '',
        searchInput: ''
    },
    methods: {
        loadQuotes() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                headers: {
                    "Authorization": `Token token=${apiKey}`
                }
            }).then(response => {
                console.log(response)
                this.results = response.data.quotes
            })
        },
        search() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                headers: {
                    "Authorization": `Token token=${apiKey}`
                },
                params: {
                    filter: this.searchInput,
                    type: this.searchSelect
                }
            }).then(response => {
                console.log(response)
                this.results = response.data.quotes
            })
        },
        created() {
            this.loadQuotes()
        },
        nextPg() {

        },
        previousPg() {

        }

    }

})