Vue.component('search-pokemon', {
    data: function() {
        return {
            result: [],
            search: '',
            pokemon: [],
           
        }
    },
    props: ['results', 'previous_pokemon', 'next_pokemon'],
    template:   `
    <span>
    <div class='input-field'>
        <div class='row'>
            <span class='col'>
                <input type="text" v-model='search' name="poke-search" id='pokes-search'>
            </span>
            <span class='col'>
                <a @click='searchPokemon' class='btn orange waves-effect waves-light'>Search</a>
            </span>
        </div>
    </div>
    </span>

    `,
    methods: {
        searchPokemon: function() {
            let i = 0
            for (object in this.results.results) {
                // console.log(this.results.results[i].name)
                if (this.search === this.results.results[i].name) {
                    // console.log('found')
                    let foundIndex = i
                    // console.log(foundIndex)
                    axios({
                        method: 'get',
                        url: this.results.results[foundIndex].url,
                      }).then(response => {
                          // console.log(response)
                          this.pokemon = response.data
                          this.$emit('pokemon-found', this.pokemon);
                          this.search = ''
                      });
                }
                i++
            }
        },

    }
})

Vue.component('paginator', {
    data: function() {
        return {
            pokemon: [],
        }
    },
    props: ['previous_pokemon', 'next_pokemon'],
    template: `
    <div>
        <span class="row">
        <span class="col left-align">
        <a href="#" class='btn waves-effect waves-light' @click='previousPokemon' >Previous</a>
        </span>
        <span class="col">
        <a href="#" class='btn waves-effect waves-light' @click='nextPokemon' >Next</a>
        </span>
    </div>
    `,
    methods: {
        previousPokemon: function() {
            axios({
                method: 'get',
                url: this.previous_pokemon
            }).then(response => {
                // console.log(response)
                this.pokemon = response.data
                this.$emit('pokemon-found', this.pokemon);
                this.search = ''
            });
        },
        nextPokemon: function() {
            // console.log(this.next_pokemon)
            axios({
                method: 'get',
                url: this.next_pokemon
            }).then(response => {
                console.log(response.data)
                this.pokemon = response.data
                this.$emit('pokemon-found', this.pokemon);
                this.search = ''
            });
        }
    }
})




Vue.component('pokemon-display', {
    data: function() {
        return {
            result: [],
           
            
            
        }
    },
    props: ['results', 'pokemon', 'species', 'stats', 'types', 'evolution_chain', 'pic_id'],
    template: `
    <span >
        <display-card >
            
        <div v-if='pokemon.name'>

        <div class="col s12 m6 center-align">
        <div class="card blue-grey lighten-4" >
        <span class="card-title center-align"><h2>{{ pokemon.name }}</h2></span>
    
        <div class='flexbox'>
        <img v-bind:src='pic_id' alt="" class='responsive-img' id='poke-pic'>
        </div>
        <q>{{ species.flavor_text_entries[0].flavor_text.replace('', ' ') }}</q>
        <h4>Evolves from:</h4>
           <p v-if='species.evolves_from_species == null'>N/A</p></a>
           <a href="#" class='btn waves-effect waves-light' @click='goTo' v-if='species.evolves_from_species !== null'> {{ species.evolves_from_species.name }}</a>
        <div class="card-content">
        <div >
        <u><p class='right-align'>ID:{{ pokemon.id }}</p></u>
        <div class="card-action">
        </div>
        <div class='row'>
        <div class='col'>
        <h4>Stats:</h4>
        </div>
        <div class='col'>
        <span>
        <span>
        <h5>HP:</h5><p class='stats green-text'>{{ stats['hp'] }}</p>
        </span>
        <span>
        <h5>Attack:</h5><p class='stats red-text'>{{ stats['attack'] }}</p>
        </span>
        <span>
        <h5>Defense:</h5><p class='stats blue-text darken-5'>{{ stats['defense'] }}</p>
        </span>
        </span>
        <span>
        <span>
        <h5>Special-Attack:</h5><p class='stats purple-text darken-3'>{{ stats['special-attack'] }}</p>
        </span>
        <span>
        <h5>Special-Defense:</h5><p class='stats teal-text accent-2'>{{ stats['special-defense'] }}</p>
        </span>
        <span>
        <h5>Speed:</h5><p class='stats yellow-text darken-4'>{{ stats['speed'] }}</p>
        </span>
        </span>
        </div>
        </div>
        <div>
        <h4 v-if='types[1]'>Types</h4>
        <h4 v-if='!types[1]'>Type</h4>
        <span>
        <p>{{ types[0] }}</p>
        <p v-if='types[1]'>{{ types[1] }}</p>
        </span>
        </div>
        <span>
        <h5>Weight:</h5>
        <p>{{ pokemon.weight }}</p>
        </span>
        <h4>In-Game Models</h4>
        <span class='row'>
        <div class='col'>
        <p>Front:</p>
        <p class='center-align'><img v-bind:src='pokemon.sprites.front_default' alt="" ></p>
        </div>
        <div class='col'>
        <p>Back:</p>
        <p class='center-align'><img v-bind:src='pokemon.sprites.back_default' alt=''></p>
        </span>
        </div>
        </div>
        </div>
        </display-card>
    `,
    methods: {
        goTo: function() {
            let i = 0
            for (object in this.results.results) {
                // console.log(this.species.evolves_from_species.name)
                // console.log(this.results.results[i].name)
                if (this.species.evolves_from_species.name === this.results.results[i].name) {
                    // console.log('found')
                    let foundIndex = i
                    // console.log(foundIndex)
                    axios({
                        method: 'get',
                        url: this.results.results[foundIndex].url,
                      }).then(response => {
                          // console.log(response)
                          this.pokemon = response.data
                          this.$emit('pokemon-found', this.pokemon);
                          this.search = ''
                      });
                }
                i++
            }
        }
    }
})




var app = new Vue({
    el: '#app',
    data: {
        item: [],
        evolution_chain: [],
        results: [],
        search: '',
        pokemon: [],
        species: [],
        types: {0: '', 1: null},
        previous_form: [],
        stats: {
            'hp': 0,
            'attack': 0,
            'defense': 0,
            'special-attack': 0,
            'special-defense': 0,
            'speed': 0,
        },
        pic_id: 0,
        id: 0,
        next_pokemon: '',
        previous_pokemon: '',
        // groupedProps: {pokemon: this.pokemon,
        //      species: this.species    
        // },
    },
    methods: {
        foundPokemon: function(event) {
            // console.log(event, 'foundPokemon')
            this.pokemon = event
            this.types = {0: '', 1: null}
            this.pic_id = `https://pokeres.bastionbot.org/images/pokemon/${this.pokemon.id}.png`
            this.id =this.pokemon.id
            this.previous_pokemon = `https://pokeapi.co/api/v2/pokemon/${this.pokemon.id - 1}/`
            this.next_pokemon = `https://pokeapi.co/api/v2/pokemon/${this.pokemon.id + 1}/`
            axios({
                method: 'get',
                url: this.pokemon.species.url,
            }).then(response => {
                // console.log(response)
                this.species = response.data
                let i=0
                for (object in this.pokemon.types) {
                    // console.log(this.pokemon.types[i].type.name)
                    this.types[i]=this.pokemon.types[i].type.name
                    i++
                }
                i=0
                for (object in this.pokemon.stats)  {
                    // console.log(this.pokemon.stats[i].base_stat)
                    this.stats[this.pokemon.stats[i].stat.name] = this.pokemon.stats[i].base_stat
                    i++
                }
                axios({
                    method: 'get',
                    url: this.species.evolution_chain.url,
                }).then(response => { 
                    this.evolution_chain = response.data
                    console.log(this.evolution_chain.chain.evolves_to[0])
                })
            })
        },
        retrieve: function() {
            axios({
                method: 'get',
                url: 'https://pokeapi.co/api/v2/pokemon/88/',
            }).then(response => {
                this.item = response.data
            })
        }
    },
    
    created: function() {
        axios({
            method: 'get',
            url: ' https://pokeapi.co/api/v2/pokemon/?limit=151',
          }).then(response => {
              // console.log(response)
              this.results = response.data

          })
    },
    updated: function() {

    }

})