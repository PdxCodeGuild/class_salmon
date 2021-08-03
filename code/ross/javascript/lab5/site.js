const randQuote = new Vue({
    el: '#randQuotes',
    data () {
        return {
            quote: null,
            author: null,
            number: 1,
        }
    },
    methods: {
        randQ: function() {
            // console.log("sel: " + sel)
            // console.log("search: " + search)
            axios({
                method: 'get',
                url: 'https://favqs.com/api/qotd',
            }).then(response => {
                this.quote = response.data.quote.body,
                this.author = response.data.quote.author
            })
        }
    }
    // mounted () {
    //     axios 
    //         .get('https://favqs.com/api/qotd')
    //         .then(response => {
    //             this.quote = response.data.quote.body,
    //             this.author = response.data.quote.author
    //         })
    // }
})

const searchQuote = new Vue({
    el: '#searchQuotes',
    data: {
        quote: [],
        sel: '',
        search: '',
        current_page: '1',
    },
    methods: {
        findQ: function() {
            // console.log("sel: " + sel)
            // console.log("search: " + search)
            document.querySelector('#disp').removeAttribute('hidden')
            document.querySelector('#page').removeAttribute('hidden')
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                headers: {
                    "Authorization": 'Token token="cd3953dfc13f9a48a5f8987432e057b1"'
                },
                params: {
                    type: this.sel,
                    // filter: 'benjamin franklin'
                    filter: this.search,
                    page: this.current_page
                }
            }).then(response => this.quote = response.data)
        },
        pagenext: function() {
           this.current_page++,
           this.findQ()
        },
        pageprev: function() {
            if (this.current_page < 1) {
                alert("You are already on the first page.")
            } else {
                this.current_page--
            }
            this.findQ()
         },
    }
})