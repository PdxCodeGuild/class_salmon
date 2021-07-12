let app = new Vue({
    el: '#app',

    data: {
        qotd{}
    }
    methods: {
        loadQuotes: function() {
            axios({
                method: 'get', 
                url: 'https//favqs.com/api/quotd'
            }).then((response) => {
                console.log(response.data)
            })
                // params: {
                    
                }
                // headers: {
                    // 'x-api-key': 'api-key'
                }

        }
    }