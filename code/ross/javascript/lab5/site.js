const randQuote = new Vue({
    el: '#randQuotes',
    data () {
        return {
            quote: null,
            author: null
        }
    },
    methods: {
        randQ: function() {
            document.querySelector('#random').removeAttribute('hidden')
            document.querySelector('#randB').setAttribute('hidden', 'true')
            document.querySelector('#anotherrandB').setAttribute('hidden', 'false')

        },
        anotherE: function() {
            document.querySelector('#anotherrandB').setAttribute('hidden', 'false')
            document.querySelector('#random')
        }
    },
    mounted () {
        axios 
            .get('https://favqs.com/api/qotd')
            .then(response => {
                this.quote = response.data.quote.body,
                this.author = response.data.quote.author
            })
    }
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
        pagination: function() {
            let page_choice 
            let page_next = document.querySelector("#page-next")
            let page_prev = document.querySelector("#page-prev")
            page_next.addEventListener('click', console.log(page_next))
            // if (page_choice == true) {
            //     this.current_page++
            //     console.log(this.current_page)
            //     this.findQ()
            // } else {
            //     console.log(this.current_page)
            // }
        }
    }
})