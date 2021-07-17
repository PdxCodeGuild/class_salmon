let app = new Vue({
    el: '#app',

    data: {
        phrase: '',
        mph: '',
        missDistance: '',
        date: '',
        name: '',
        hazardous: '',
        quantity: '',
        test: false,
        assList: [],
        day: [],
        starterObject: [],
        starterDistance: '',
        inputDate: '',
        minDiam: '',
        maxDiam: '',
        avgDiam: '',
    },

    methods: {
        loadPhrase: function () {
            axios({
                method: 'GET',
                // key = 't716nP3WfjaqK7mcEso1cz6iJHMbBgslpA8rAM0K',
                url: `https://api.nasa.gov/neo/rest/v1/feed?start_date=${this.inputDate}`,
                params: {
                    api_key: 't716nP3WfjaqK7mcEso1cz6iJHMbBgslpA8rAM0K'
                }
            }).then(response => {
                this.test = true
                this.inputDate = document.getElementById('inputDate').value.toString()
                // console.log(this.inputDate)
                this.mph = Math.round(response.data.near_earth_objects[this.inputDate][1]['close_approach_data'][0]["relative_velocity"]["miles_per_hour"])
                this.missDistance = Math.round(response.data.near_earth_objects[this.inputDate][1]['close_approach_data'][0]['miss_distance']['miles'])
                this.date = response.data.near_earth_objects[this.inputDate][1]['close_approach_data'][0]['close_approach_date']
                this.name = response.data.near_earth_objects[this.inputDate][1]['name']
                this.hazardous = response.data.near_earth_objects[this.inputDate][1]["is_potentially_hazardous_asteroid"]
                this.quantity = response.data.near_earth_objects[this.inputDate].length

                this.day = response.data.near_earth_objects[this.inputDate]

                this.starterObject = this.day[0]
                this.starterDistance = this.starterObject['close_approach_data'][0]['miss_distance']['miles']
                // console.log(this.starterObject)
                // console.log(this.starterDistance)
                console.log(this.day)
                this.day.forEach(ass => {
                    if (ass['close_approach_data'][0]['miss_distance']['miles'] < this.starterDistance) {
                        this.starterDistance = ass['close_approach_data'][0]['miss_distance']['miles']
                        this.starterObject = ass
                    }
                })

                this.avgDiam = Math.round(((this.starterObject['estimated_diameter']['meters']['estimated_diameter_max']) + (this.starterObject['estimated_diameter']['meters']['estimated_diameter_min'])) / 2)
                console.log(this.starterObject['estimated_diameter']['meters']['estimated_diameter_max'])
                console.log(this.starterObject['estimated_diameter']['meters']['estimated_diameter_min'])
                console.log(this.avgDiam)
                // console.log(this.starterDistance)





            })
        }
    }
})
