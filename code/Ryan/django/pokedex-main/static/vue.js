const vm = new Vue({
  el: "#app",
  delimiters: ['[[', ']]'],
  data: {
    pokemonList:[],
    pokemonID: {
      pokemonNumber: "",
      pokemonName: "",
      pokemonHeight: "",
      pokemonWeight: "",
      pokemonImageFront: "",
      pokemonImageBack: "",
      pokemonCaughtBy: "",
    },
  },
  methods: {
    // Grab the pokemon list
    loadPokemon: function() {
      axios({
        method: "get",
        url: "/apis/v1/"
      }).then(response => {
        this.pokemonList = response.data
        console.log(response.data)
        console.log(this.pokemonList)
        console.log(this.pokemonList[0].name)
      })
    },
    createPokemon: function() {},
    updatePokemon: function() {},
    deletePokemon: function() {},
  },
  created: function(){
    this.loadPokemon()
    this.createPokemon()
    this.updatePokemon()
    this.deletePokemon()
  }
})
