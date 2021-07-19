// Requirements:

// Your app must use Vue to fetch data and interact with the results.
// Let the user enter a search term and select whether to search by keyword, author, or tag.
// Implement pagination buttons when the search returns more than 25 quotes.
// When the page first loads, show the user a set of completely random quotes.
// You must have at least one Vue component in your app.

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
        searchInput: '',

    },
    methods: {
        search() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                headers: {
                    "Authorization": `Token token="75781e1e8edbf2eb68848384abbbd2bb"`
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

    }

})