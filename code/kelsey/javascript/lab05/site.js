// Vue.component('display', {
//     props: ["quotes"],
//     data: function () {
//         return {
//             results: this.results
//         }
//     },
//     template: `<div>
//                 <div v-for="result in results">{{ result.body }}</div>
//                 </div>`
// })

const vm = new Vue({
    el: '#app',
    data: {
        results: [],
        searchSelect: '',
        searchInput: ''
    },
    methods: {
        loadQuotes() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                headers: {
                    "Authorization": `Token token="75781e1e8edbf2eb68848384abbbd2bb"`
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