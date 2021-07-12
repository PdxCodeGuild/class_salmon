Vue.component('author-quotes', {
    template: '\
      <li>\
        {{ quote }}\
        <button v-on:click="$emit(\'remove\')">Remove</button>\
      </li>\
    ',
    props: ['title']
  })

let vm = new Vue({
    el: '#app',
    data: {
        quoteResponse: {}
    },
    methods: {
        loadQuote: function() {
            axios({
                method: "get",
                url: "https://favqs.com/api/qotd",
            }).then(response => {
                this.quoteResponse = response.data;
            })
        },
        loadAuthor: function(counter, command) {
            axios({
                method: "get",
                headers={'Content-Type': 'application/json', 'Authorization': `Token token="${apiKey}"`},
                url: `https://favqs.com/api/quotes?page=${counter}&filter=${command}`,
            }).then(response => {
                this.quoteResponse = response.data;
            })
        }
    },
});