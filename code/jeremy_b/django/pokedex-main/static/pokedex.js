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
        caughtList: [],
        csrf_token: document.querySelector("input[name=csrfmiddlewaretoken]").value,
    },
    methods:{
        loadPokemon: function() {
            axios({
                method: 'GET',
                url: '/api/v1/pokemon'
            }).then(response => {
                this.pokemon = response.data;
            })
        },
        catchPokemon: function(pokemon_id){
            console.log(pokemon_id);
            let new_list = [];
            for (i = 0; i < this.caught.length; i++){
                new_list.push(this.caught[i])
            }
            new_list.push(pokemon_id)
            axios({
                method: 'patch',
                url: `/api/v1/users/${this.user.id}/`,
                headers: {
                    'X-CSRFToken': this.csrf_token
                },
                data: {
                    'caught': new_list
                }
            }).then(response => {
                this.getUpdatedCaughtList();

                this.loadPokemon();
            });
        },
        releasePokemon: function(pokemon_id){
            let new_list = [];
            for (i = 0; i < this.caught.length; i++){
                new_list.push(this.caught[i])
            }
            let index = new_list.indexOf(pokemon_id)
            console.log(index)
            new_list.splice(index, 1)
            console.log(new_list)
            axios({
                method: 'patch',
                url: `/api/v1/users/${this.user.id}/`,
                headers: {
                    'X-CSRFToken': this.csrf_token
                },
                data: {
                    'caught': new_list
                }
            }).then(response => {
                this.getUpdatedCaughtList();
                this.loadPokemon();
            });
        },
        getUpdatedCaughtList: function (){
            this.loadPokemon();
            axios({
                method: 'GET',
                url: '/api/v1/current_user'
            }).then(response => {
                this.user = response.data;
                this.caught = this.user.caught;
            })
        },
        makeCaughtList: function() {
            for (poke in this.pokemon){
                if (poke.id + 1 in this.caught){
                    this.caughtList.push(poke)
                }
            }
        }
    },
    mounted: function() {
        this.$nextTick(function() {
            this.loadPokemon();
            axios({
                method: 'GET',
                url: '/api/v1/current_user'
            }).then(response => {
                this.user = response.data;
                this.caught = this.user.caught;
            })
        })
    },
})

// Other JS.