// Here I comment out quote of the day and move it to the component in the application
Vue.component('qotd', {
    data: function() {
        return {quoteResponse:{}}
    },
    template: `
        <div>
        <button v-on:click="loadQuote">Quote of the Day</button>
        <p v-if="quoteResponse.quote">{{ quoteResponse.quote.body }}</p>
        <p v-if="quoteResponse.quote"><i><a v-bind:href="quoteResponse.quote.url">{{ quoteResponse.quote.author }}</a></i></p>
        </div>
    `,
    methods: {
        loadQuote: function() {
            axios({
                method: "get",
                url: "https://favqs.com/api/qotd",
            }).then(response => {
                this.quoteResponse = response.data;
                console.log(response.data)
            })
        },
    },
})
let vm = new Vue({
    el: '#app',
    data: {
        // quoteResponse: {},
        authorResponse: [],
        filterInput: "",
        typeInput: "",
        pageInput: 1,
    },
    methods: {
        // loadQuote: function() {
        //     axios({
        //         method: "get",
        //         url: "https://favqs.com/api/qotd",
        //     }).then(response => {
        //         this.quoteResponse = response.data;
        //         console.log(response.data)
        //     })
        // },
        loadAuthor: function() {
            axios({
                method: "get",
                url: 'https://favqs.com/api/quotes/',
                headers: {
                    "Authorization": `Token token="${apiKey}"`,
                },
                params: {
                    type: this.typeInput,
                    filter: this.filterInput,
                    page: this.pageInput,
                },
                // url: `https://favqs.com/api/quotes/?filter=${filter}&type=${type}`,
            }).then(response => this.authorResponse = response.data
            )
        },
        nextPage: function() {
            this.pageInput++,
            this.loadAuthor()
        },
        previousPage: function() {
            if (this.pageInput >= 2) {
                this.pageInput--
            }
            this.loadAuthor()
        },
    },
});