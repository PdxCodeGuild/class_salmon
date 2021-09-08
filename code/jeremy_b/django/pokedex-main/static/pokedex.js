/**************************************************************
 * Author: Jeremy Bush
 * Project: Pokedex, Django Lab 7
 * Version: 1
 * Date: 9/7/2021
 * *************************************************************/

// Vue app

let app = new Vue({
    el: '#app',
    delimiters:['[[', ']]'],
    data:{
        user: '',
        pokemon: [],
        caught: [],
        csrf_token: document.querySelector("input[name=csrfmiddlewaretoken]").value,
    },
    methods:{
        loadPokemon: function() {
            axios.get({url: '/api/v1/pokemon'}).then(response => {
                this.pokemon = response.data;
                console.log(this.pokemon);
            })


        }
    },
    mounted: function() {
        this.$nextTick(function() {
            this.loadPokemon();
            axios.get({url: '/api/v1/current_user'}).then(response => {
                this.user = response.data;
                this.caught = this.user.caught;
            })
        })
    }
})

// Other JS.