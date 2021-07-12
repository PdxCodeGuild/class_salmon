const randQuote = new Vue({
    el: '#randQuotes',
    data () {
        return {
            quote: null
        }
        return {
            author: null
        }
    },
    methods: {
        findQ: function() {
            document.querySelector('#random').removeAttribute('hidden')
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
        search: null
    },
    

})