Vue.component('individual', {
    data: function () {
        return {
            fartscroll(50);
        }
    },

})
// do quote in quotes list


let app = new Vue({
    el: '#app',


    data: {
        results: [],
        searchInput: '',
        qotd: '',
        author: ''

    },
    methods: {
        loadQuotes: function () {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/qotd',
                headers: {
                    'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'
                },

            }).then(response => {
                this.qotd = response.data.quote.body
                this.author = response.data.quote.author

                console.log(this.qotd)
            })
        }
    },

    // searchKEY: function () {
    //     axios({
    //         method: 'get',
    //         url: 'https://favqs.com/api/quotes',
    //         headers: {
    //             'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'
    //         },
    //         // params: {
    //         //     type: 'author',
    //         //     filter: 'mark twain'
    //         // }

    //     }).then(response => {
    //         this.qotd = response.data.quote.body
    //         this.author = response.data.quote.author

    //         console.log(this.qotd)
    //     })
    // }
    searchAuthor: function () {
        axios({
            method: 'get',
            url: 'https://favqs.com/api/quotes',
            headers: {
                'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'
            },
            params: {
                type: 'author',
                filter: 'searchInput'
            }

        }).then(searchResponse => {
            this.results = searchResponse.data.quote.body
            this.author = searchResponse.data.quote.author

        })
    },
    //     searchTag: function () {
    //         axios({
    //             method: 'get',
    //             url: 'https://favqs.com/api/qotd',
    //             headers: {
    //                 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'
    //             },
    //             // params: {
    //             //     type: 'author',
    //             //     filter: 'mark twain'
    //             // }

    //         }).then(response => {
    //             this.qotd = response.data.quote.body
    //             this.author = response.data.quote.author

    //             console.log(this.qotd)
    //         })
    //     }
    //     // function for choosing each button

    // },
    created: function () {
        this.loadQuotes()


    }






})
