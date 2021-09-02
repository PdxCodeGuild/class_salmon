Vue.component('random-quote', {
    data: function () {
        return {
            quote: '',
            author:'',

        }
    },
    template: `<div><p>{{quote}}</p><p>-- {{author}}</p></div>`,
    mounted(){
        axios.get('https://favqs.com/api/qotd', this.headers).then(response => {
            this.quote = response.data.quote.body;
            this.author = response.data.quote.author;
        })
    }

})
// do quote in quotes list


let app = new Vue({
    el: '#app',
    data: {
        results: [],
        searchInput: '',
        searchBy: '',
        page: 1,
        lastPage: false,
    },
    methods: {
        loadQuotes: function () {
            console.log("In loadQuotes")
            axios({
                url: 'https://favqs.com/api/quotes/',
                method: 'get',
                headers: {'Authorization': 'Token token="03e6a398349bfe897cdbfb4ea03fb3f8"'},
                params: {
                    type: this.searchBy,
                    filter: this.searchInput,
                    page: this.page
                },
            }).then(response => {
                this.results = response.data.quotes,
                this.page = response.data.page,
                this.lastPage = response.data.last_page
            });
        },
        nextPage: function () {
            this.page += 1,
            this.loadQuotes()
        },
        previousPage: function () {
            this.page -= 1,
            this.loadQuotes()
        },
    }
})
