const cityGen = new Vue({
    el: '#vue-app',
    data: {
        // cities: ['seattle', 'oslo', 'paris'],
        city_one: '',
        city_two: '',
        city_three: '',
        data: {},
        summary: '',
        show: false,
        message: 'Data coming soon!',
        image: ''
    },
    methods: {
        add_to_list: function() {
            this.cities.push(this.city_one)
            // this.cities.push(this.city_two)
            // this.cities.push(this.city_three)
        },
        get_data: function() {
                axios.get(`https://api.teleport.org/api/urban_areas/slug:${encodeURIComponent(this.city_one)}/scores/`)
                .then(response => {
                    this.data = response.data,
                    this.show = true
                })
        },
        get_photo: function() {
            axios.get(`https://api.teleport.org/api/urban_areas/slug:${encodeURIComponent(this.city_one)}/images`)
            .then(response => {
                this.image = response.data.photos[0].image.web
                this.image = '<img width="95%" src="' + this.image + '">'
            })
        },
        hide: function() {
            this.show = false,
            this.message = 'Return to the search bar above to look up data for another city.'
        }
    }
})