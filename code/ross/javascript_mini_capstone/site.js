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
    <input type="text" name="cityName" placeholder="Type city name" v-model="city_str"><br>
    <button @click='add_to_list'>Add City</button>
    <br>
    </div>
    `,
    methods: {
        add_to_list: function() {
            this.$emit('add', {id: this.id, city_str: this.city_str, url: 'https://api.teleport.org/api/urban_areas/slug:${city_str}/scores/'})
            console.log("id: " + this.id)
            console.log("city_str: " + this.city_str)
            this.id++
            this.city_str = ""
            console.log("num comp: " + num_comparisons)
        }
    }
})

const cityGen = new Vue({
    el: '#cityGen',
    data: {
        num_comparisons: [
            // {id: "1", city_str: "seattle", url: 'https://api.teleport.org/api/urban_areas/slug:seattle/scores/'},
            // {num: "1", city: "seattle", trait_one: "", trait_two: "", trait_three: ""},
            // {id: "2", city_str: "vancouver"},
            // {id: "3", city_str: "portland"}
        ],
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
    methods: {
        add_to_list: function(payload) {
            this.num_comparisons.push(payload)
            console.log(num_comparisons)
        }
    },
    mounted () {
        axios 
            // .get('https://api.teleport.org/api/urban_areas/slug:seattle/scores/')
            // for (i in num_comparisons) {
                // .get(`https://api.teleport.org/api/urban_areas/slug:${this.test.url}/scores/`)
                .get(`${this.num_comparisons[0].url}`)
                .then(response => {
                    this.overall = Math.round(response.data["teleport_city_score"])
                    console.log("overall: " + this.overall)
                    console.log("search: " + this.search)
                    console.log("num comp: " + this.num_comparisons)
                    this.city = response
                })
            // }
    }
})