var summary = ""

var city_s = "Seattle"

var cities = document.querySelector('#numcomparisons')
console.log(cities)

Vue.component('add-city', {
    data: function() {
        return {
            id: 1,
            city: []
        }
    },
    template: `
    <div>
    <label for="cityName">Input a city name here:</label>
    <input type="text" id="cityName" v-model="search">
    <button @click="add_city">Add City</button>
    <br>
    </div>
    `,
    methods: {
        add_city: function() {
            this.$emit('add', [this.city])
            this.city = ""
            // this.id++
        }
    }
})

const cityGen = new Vue({
    el: '#cityGen',
    data: {
        city: {},
        search: '',
        overall: 0,
        trait_one: "Cost of Living",
        trait_two: "Commute",
        trait_three: "Safety",
        traits: {
            traits1: 'housing',
            traits2: 'cola',
            traits3: 'housing',
            traits4: 'housing',
            traits5: 'housing',
            traits6: 'housing',
            traits7: 'housing',
            traits8: 'housing',
            traits9: 'housing',
            traits10: 'housing',
            traits11: 'housing',
            traits12: 'housing',
            traits13: 'housing',
            traits14: 'housing',
            traits15: 'housing',
            traits16: 'housing',
            traits17: 'housing',
        }
    },
    // methods: {      
    //     // addCity: function() {
    //     //     axios({
    //     //         method: 'get',
    //     //         url: 'https://api.teleport.org/api/',
    //     //         headers: {
    //     //             "Accept": "application/vnd.teleport.v1+json",
    //     //             "cache-control": "public, max-age=300",
    //     //             "content-length": "388",
    //     //             "content-type": "application/vnd.teleport.v1+json; charset=utf-8"
    //     //         },
    //     //         parameters: {
    //     //             search: 'Shanghai'
    //     //         }
    //     //     }).then(response => this.city = response)
    //     // }
    //     citySearch: function() {
    //         axios({
    //             method: 'get',
    //             url: 'https://api.teleport.org/api/urban_areas/seattle/scores/',
    //             headers: {
    //                 "content-length": "80",
    //                 "content-type": "text/html; charset=utf-8"
    //               },
    //             parameters: {
    //                 search: 'Seattle'
    //             }
    //         }).then(response => this.city = response)
    //     }
    // }
    mounted () {
        axios 
            // .get(`https://api.teleport.org/api/cities/?${search}`)
            .get('https://api.teleport.org/api/urban_areas/slug:seattle/scores/')
            // .get('https://api.teleport.org/api/urban_areas/slug:${this.search}/scores/')
            .then(response => {
                this.overall = Math.round(response.data["teleport_city_score"])
                console.log(this.overall)
                console.log(this.search)
                this.city = response
                this.search = add-city
            })
    }
})

cityGen.search = add-city
console.log(cityGen.search)

// document.querySelector('summary').innerHTML = city.data["summary"]