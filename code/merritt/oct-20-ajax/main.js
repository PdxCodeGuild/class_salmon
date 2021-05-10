var vm = new Vue({
    el: '#app',
    data: {
      quotes: [],
      searchTerm: ""
    },
    methods: {
      loadQuote: function() {
        axios({
          url: "https://favqs.com/api/quotes",
          method: "get",
          headers: {
            "Authorization": `Token token="${apiKey}"`
          },
          params: {
            filter: this.searchTerm
          }
        }).then(response => {
          this.quotes = response.data.quotes
        })
      }
    }
  })