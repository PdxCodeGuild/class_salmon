let app = new Vue({
    el: '#app',

    data: {
        phrase: '',
    },

    methods: {
        loadPhrase: function () {
            axios({
                method: 'GET',
                // key = 't716nP3WfjaqK7mcEso1cz6iJHMbBgslpA8rAM0K',
                url: 'https://api.nasa.gov/neo/rest/v1/feed?start_date=2021-07-15',
                params: {
                    api_key: 't716nP3WfjaqK7mcEso1cz6iJHMbBgslpA8rAM0K'
                }
            }).then(response => {
                console.log(response)
                this.phrase = response.data,

                    console.log(this.phrase)

            })

        }
    }
})