let vm = new Vue({
    el: '#app',
    data: {
        quotes: {},
        searchTerm: "",

    },
    methods: {
        loadQuote: function () {
            axios({
                method: "get",
                url: "https://favqs.com/api/quotes/",
                params: {
                    filter: this.searchTerm,
                    type: "author",
                    page: 2
                },
                headers: {
                    Authorization: `Token token="${favQsKey}"`
                }
            }).then(response => {
                this.quotes = response.data.quotes;
            });
        }
    }
});