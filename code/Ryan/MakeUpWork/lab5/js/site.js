const vm = new Vue({
    el: '#app',
    data: {
        results: {},
        currentPage: 1,
        searchType: ""
      },
    methods: {
        incrementPage: function() {
            
            if(this.searchType === "random") {
                this.loadRandomQuotes(this.currentPage+1)
            } else if(this.searchType === "keyword") {
                this.loadQuoteByKeyword(this.currentPage+1)
            } else if(this.searchType === "author") {
                this.loadQuoteByAuthor(this.currentPage+1)
            } else if(this.searchType === "tag") {
                this.loadQuoteByTag(this.currentPage+1)
            };
            this.currentPage += 1;
        },

        decrementPage: function() {
            
            if(this.searchType === "random") {
                this.loadRandomQuotes(this.currentPage-1)
            } else if(this.searchType === "keyword") {
                this.loadQuoteByKeyword(this.currentPage-1)
            } else if(this.searchType === "author") {
                this.loadQuoteByAuthor(this.currentPage-1)
            } else if(this.searchType === "tag") {
                this.loadQuoteByTag(this.currentPage-1)
            };
            this.currentPage -= 1;
        },

        loadRandomQuotes: function(pageCount){
            this.searchType = "random"
            pageCount = this.pageCount
            axios
                .get('https://favqs.com/api/quotes/', {
                    headers: {
                    "Authorization": 'Token token="b7647848255789e53bbff6835cb6119c"'
                    },
                    params: {
                        page: `${this.currentPage}`
                    }
                }).then(res => this.results = res.data) 
        },
        loadQuoteByKeyword: function(pageCount){
            this.searchType = "keyword"
            pageCount = this.pageCount
            query = document.getElementById("searchQuery").value
            axios
                .get('https://favqs.com/api/quotes/', {
                    headers: {
                    "Authorization": 'Token token="b7647848255789e53bbff6835cb6119c"'
                    },
                    params: {
                        type: "keyword",
                        filter: `${query}`,
                        page: `${this.currentPage}`
                    }
                }).then(res => this.results = res.data)
            
        },
        loadQuoteByAuthor: function(pageCount){
            this.searchType = "author"
            pageCount = this.pageCount
            query = document.getElementById("searchQuery").value
            axios
                .get('https://favqs.com/api/quotes/', {
                    headers: {
                    "Authorization": 'Token token="b7647848255789e53bbff6835cb6119c"'
                    },
                    params: {
                        type: "author",
                        filter: `${query}`,
                        page: `${this.currentPage}`
                    }
                }).then(res => this.results = res.data)
            
        },
        loadQuoteByTag: function(pageCount){
            this.searchType = "tag"
            pageCount = this.pageCount
            query = document.getElementById("searchQuery").value
            axios
                .get('https://favqs.com/api/quotes/', {
                    headers: {
                    "Authorization": 'Token token="b7647848255789e53bbff6835cb6119c"'
                    },
                    params: {
                        type: "tag",
                        filter: `${query}`,
                        page: `${this.currentPage}`
                    }
                }).then(res => this.results = res.data)
            
        },
        testClick: function(){
            console.log(this.results, "results")
            console.log(this.results.quotes, "quotes")
            console.log(this.results.page, "page")
            console.log(this.results.quotes[0], "quote")
            console.log(document.getElementById("searchQuery").value)
            console.log(this.searchType)
        }
    },

    created: function() {
        this.loadRandomQuotes()
     },
})
