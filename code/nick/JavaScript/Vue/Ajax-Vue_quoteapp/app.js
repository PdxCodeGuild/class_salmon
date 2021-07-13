// Vue.component('author-quotes', {
//     template: '\
//       <li>\
//         {{ quote }}\
//         <button v-on:click="$emit(\'remove\')">Remove</button>\
//       </li>\
//     ',
//     props: ['title']
//   })

let vm = new Vue({
    el: '#app',
    data: {
        quoteResponse: {},
        authorResponse: {}
    },
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
        loadAuthor: function() {
            axios({
                method: "get",
                headers: {
                    "Authorization": `Token token="${apiKey}"`,
                },
                params: {
                    type: 'author',
                    filter: 'mark twain'
                },
                url: `https://favqs.com/api/quotes/?filter=${filter}&type=${type}`,
            }).then(response => {
                this.authorResponse = response.data;
                console.log(response.data)
            })
        }
    },
});