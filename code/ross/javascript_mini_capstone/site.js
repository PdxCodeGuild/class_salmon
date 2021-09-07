Vue.component('add-traits', {
    data: function() {
        return {
            trait_one: "Cost of Living",
            trait_two: "Commute",
            trait_three: "Safety"
        }
    }, 
    methods: {
        addTraits: function() {
            trait_one = '',
            trait_two = '',
            trait_three = ''
        }
    }
})

Vue.component('add-city', {
    data: function() {
        return {
            id: 1,
            city_str: "",
            url: ""
        }
    },
    template: `
    <div>
        <label for="cityName">Input a city name here:</label>
        <input type="text" name="cityName" placeholder="Type city name" v-model="city_str" @keydown.enter="add_to_list"><br>
        <button @click='add_to_list'>Add City</button>
        <br>
    </div>
    `,
    methods: {
        add_to_list: function() {
            url = `https://api.teleport.org/api/urban_areas/slug:${this.city_str}/scores/`
            console.log(url)
            this.$emit('add', {id: this.id, city_str: this.city_str, url: url})
            console.log("id: " + this.id)
            console.log("city_str: " + this.city_str)
            this.id++
            this.city_str = ""
            console.log("num comp: " + city_data)
        }
    }
})

// Vue.component('dataPull', {
//     data: {
//         city: {}
//     },
//     mounted () {
//         axios
//             .get(`https://api.teleport.org/api/urban_areas/slug:${encodeURIComponent(this.search)}/scores/`)
//             .then(response => {
//                 this.city_data[0].data = response
//                 this.city_data[0].overall = Math.round(response.data["teleport_city_score"])
//                 this.city_data[0].summary = response.data["summary"]
//                 // this.overall = Math.round(response.data["teleport_city_score"])
//                 this.city = response
//             })
//     }
// })

const cityGen = new Vue({
    el: '#vue-app',
    data: {
        city_data: [
            {id: "1", city_str: "seattle", url: 'https://api.teleport.org/api/urban_areas/slug:seattle/scores/', overall: 0, summary: '', trait_one: "Cost of Living", trait_two: "commute", trait_three: "safety", data: ""},
            // {id: "1", city_str: "portland", url: 'https://api.teleport.org/api/urban_areas/slug:portland/scores/', overall: 1, summary: '', trait_one: "startups", trait_two: "women", trait_three: "dogs"},
            // {num: "1", city: "portland", trait_one: "", trait_two: "", trait_three: ""},
            // {id: "2", city_str: "vancouver"},
            // {id: "3", city_str: "portland"}
        ],
        num_comps: 1,
        city: {},
        search: 'seattle',
        overall: 0,
        trait_one: "Cost of Living",
        trait_two: "Commute",
        trait_three: "Safety",
        // trait_selection: {
        //     first: trait_one,
        //     second: trait_two,
        //     third: trait_three
        // },
        traits: {
            'startups': '3',
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
        // response: dataPull
    },
    methods: {
        add_to_list: function(payload) {
            this.city_data.push(payload)
            console.log("num com: " + city_data)
        }
    },
    mounted () {
        axios
            .get(`https://api.teleport.org/api/urban_areas/slug:${encodeURIComponent(this.search)}/scores/`)
            .then(response => {
                this.city_data[0].data = response.data
                this.city_data[0].overall = Math.round(response.data["teleport_city_score"])
                this.city_data[0].summary = response.data["summary"]
                // this.overall = Math.round(response.data["teleport_city_score"])
                this.city = response
            })
    }
})