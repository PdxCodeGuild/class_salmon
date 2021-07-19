Vue.component('qotd', {
    data: function() {
        return {
            results: [],
            qotd: {}
        }
    },
    template: `
    <span>
        <div>
            <button @click="loadQuoteOfDay">Get Qotd</button>
        </div>

        <div>
            <h3>Quote of the Day:</h3>
        </div>

        <div>
            <q v-if='qotd.quote'>{{ qotd.quote.body }}</q>
            <h5 v-if='qotd.quote'>{{ qotd.quote.author }}</h5>
        </div>
    </span>
    
    `,
    methods: {
        loadQuoteOfDay: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/qotd',
            }).then(response => this.qotd = response.data).catch(console.log("error!"))
            .then(response => console.log(response))
        },
    }
})  


var app = new Vue({
    el: '#app',
    data: {
        message: 'Search for quotes',
        results: [],
        qotd: {},
        tagFilter: '',
        keywordFilter: '',
        authorFilter: '',
        counter: 1,
        page: 1,
        author: '',
        result: '',
        keyword: '',
        tag: '',
        apikey: apiKey,
    },
    methods: {
        byAuthor: function() {
            search = this.authorFilter
            this.author = this.authorFilter
            this.keyword = ''
            this.tag = ''
            this.authorFilter = ''
            this.page = 1
            this.result='byAuthor'
            axios({
              method: 'get',
              url: 'https://favqs.com/api/quotes',
              headers: {
                  "Authorization": `Token token="${apiKey}"`
              },
              params: {
                  type: 'author',
                  filter: this.author,
                  page: this.page
              }
            }).then(response => {
                // console.log(response)
                this.results = response.data

            })
        },
        byKeyword: function() {
            search = this.keywordFilter
            this.keyword = this.keywordFilter
            this.tag = ''
            this.author =''
            this.keywordFilter = ''
            this.page = 1
            this.result='byKeyword'
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: {
                    'Authorization': `Token token="${apiKey}"`
                },
                params: {
                    filter: search,
                    page: this.page
                }
            }).then(response => {
                this.results = response.data
            })
        },
        byTag: function() {
            search = this.tagFilter
            this.tag = this.tagFilter
            this.keyword = ''
            this.author = ''
            this.tagFilter = ''
            this.result='byTag'
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: {
                    'Authorization': `Token token="${apiKey}"`
                },
                params: {
                    type: 'tag',
                    filter: search
                }
            }).then(response => {
                this.results = response.data
            })
        },
        incermentCounter: function() {
            this.counter++
        },
        nextPage: function() {
            if (this.result === 'byAuthor') { 
                if (this.results.last_page === true) {
                    
                }
                else {
                    this.page++ 
                    // this.byAuthor()
                    axios({
                        method: 'get',
                        url: 'https://favqs.com/api/quotes',
                        headers: {
                            "Authorization": `Token token="${apiKey}"`
                        },
                        params: {
                            type: 'author',
                            filter: this.author,
                            page: this.page
                        }
                    }).then(response => {
                        this.results = response.data
                        console.log(this.results.page)
                        console.log(this.results.last_page)
                    }) 
                }
            }
            if (this.result === 'byKeyword') {
                if (this.results.last_page === true) {

                }
                else {
                    this.page++
                    axios({
                        method: 'get',
                        url: 'https://favqs.com/api/quotes',
                        headers: {
                            'Authorization': `Token token="${apiKey}"`
                        },
                        params: {
                            filter: search,
                            page: this.page,
                        }
                    }).then(response => {
                        this.results = response.data
                    }) 
                }
            }
            if (this.result === 'byTag') {
                if (this.result.last_page === true) {

                }
                else {
                    this.page++
                    axios({
                        method: 'get',
                        url: 'https://favqs.com/api/quotes',
                        headers: {
                            'Authorization': `Token token="${apiKey}"`
                        },
                        params: {
                            type: 'tag',
                            filter: search,
                            page: this.page
                        }
                    }).then(response => {
                        this.results = response.data
                    })
                }
            }
        },
        previousPage: function() {
            if (this.result === 'byAuthor') {
                if (this.results.page === 1) {

                }
                else {
                    this.page--
                axios({
                    method: 'get',
                    url: 'https://favqs.com/api/quotes',
                    headers: {
                        "Authorization": `Token token="${apiKey}"`
                    },
                    params: {
                        type: 'author',
                        filter: this.author,
                        page: this.page
                    }
                }).then(response => {
                    this.results = response.data
                    console.log(this.results.page)
                    console.log(this.results.last_page)
                }) }
            }
            if (this.result === 'byKeyword') {
                if (this.results.page === 1) {

                }
                else {
                    this.page--
                    axios({
                        method: 'get',
                        url: 'https://favqs.com/api/quotes',
                        headers: {
                            'Authorization': `Token token="${apiKey}"`
                        },
                        params: {
                            filter: search,
                            page: this.page,
                        }
                    }).then(response => {
                        this.results = response.data
                    }) 
                }
            }
            if (this.result === 'byTag') {
                if (this.results.page ===1) {

                }
                else {
                    this.page--
                    axios({
                        method: 'get',
                        url: 'https://favqs.com/api/quotes',
                        headers: {
                            'Authorization': `Token token="${apiKey}"`
                        },
                        params: {
                            type: 'tag',
                            filter: search,
                            page: this.page
                        }
                    }).then(response => {
                        this.results = response.data
                    })
                }
            }
        },
    },
    created: function () {
        console.log(this.apikey)
        axios({
            method: 'get',
            url: 'https://favqs.com/api/quotes/',
            headers: {
                Authorization: `Token token="${this.apikey}"`
            },
            params: {

            }
        }).then(response => {
            this.results = response.data
        })

    }  

})