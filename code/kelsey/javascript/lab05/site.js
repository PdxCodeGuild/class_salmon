// Requirements:

// Your app must use Vue to fetch data and interact with the results.
// Let the user enter a search term and select whether to search by keyword, author, or tag.
// Implement pagination buttons when the search returns more than 25 quotes.
// When the page first loads, show the user a set of completely random quotes.
// You must have at least one Vue component in your app.

Vue.component('', {
    data: function() {
        return
    }, 
    template: ''
})
const vm = new Vue({
    el: '#app',
    data: {
        results: ''
    },
    search() {
        axios({
            method: 'get',
            url: 'https://favqs.com/api/quotes/',
            headers: {
                "Authorization": `Token token="75781e1e8edbf2eb68848384abbbd2bb"`
            }.then(response => {
                console.log(response)
            })
        })
    }
})