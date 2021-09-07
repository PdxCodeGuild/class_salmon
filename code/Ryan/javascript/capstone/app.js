const vm = new Vue({
    el: '#app',
    data: {
        deckID: "",
        player1Cards: [],
        player1Score: 0,
        player2Cards: [],
        player2Score: 0,
        isShuffled: false,
        cardsRemaining: "0",
        output: "",

        p1hand:[],
        p2hand:[],
    },
    methods: {
      // Get a new deck -> Output deck_id
        loadNewDeck: function() {
            axios({
                method: 'get',
                url: 'http://deckofcardsapi.com/api/deck/new/'
              }).then(response => {
              this.deckID = response.data.deck_id
              this.cardsRemaining = response.data.remaining
              // console.log(response)
              }
            )
        },

      // Shuffle the current deck
        shuffleDeck: function () {
            axios({
                method: "get",
                url: `http://deckofcardsapi.com/api/deck/${this.deckID}/shuffle/`,
              }).then(response => {
                  this.isShuffled = response.data.shuffled
                  // console.log(response)
              }
            )
        },

      // Player 1 draw card
        drawCardP1: function () {
          axios({
                method: "get",
                url: `http://deckofcardsapi.com/api/deck/${this.deckID}/draw/?count=52`
              }).then(response => {
                this.player1Cards = response.data;
                this.cardsRemaining = response.data.remaining;
                this.output = "Player 2 Turn"
                console.log(this.player1Cards)
                console.log(this.player1Cards.data)
                console.log(this.player1Cards.cards)
                console.log(this.player1Cards.cards[0])
                console.log(this.player1Cards.cards.length)

                // how to deal to players
                for(let i = 0; i < 52; i++){
                  if (i % 2 === 0){this.p1hand.push(this.player1Cards.cards[i])}
                  else {this.p2hand.push(this.player1Cards.cards[i])}
                }

                // this.p1hand.push(this.player1Cards.cards[0])
                // this.p2hand.push(this.player1Cards.cards[1])

                console.log(this.p1hand)
                console.log(this.p2hand)
              })
        },

        // // Player 1 draw card
        //   drawCardP1: function () {
        //     axios({
        //           method: "get",
        //           url: `http://deckofcardsapi.com/api/deck/${this.deckID}/draw/?count=1`
        //         }).then(response => {
        //           this.player1Cards = response.data;
        //           this.cardsRemaining = response.data.remaining;
        //           this.output = "Player 2 Turn"
        //         })
        //   },

      // Player 2 draw card
        drawCardP2: function () {
          axios({
                method: "get",
                url: `http://deckofcardsapi.com/api/deck/${this.deckID}/draw/?count=1`
              }).then(response => {
                this.player2Cards = response.data;
                this.cardsRemaining = response.data.remaining;
                this.calcWinner();
              })
        },

      // Compare the results
        calcWinner: function () {
        // Assign numerical value to face cards
          let p1Value = this.player1Cards.cards[0].value
          if(p1Value == "ACE") {
            p1Value = 14;
          }else if (p1Value == "KING") {
            p1Value = 13;
          }else if (p1Value == "QUEEN") {
            p1Value = 12;
          }else if (p1Value == "JACK") {
            p1Value = 11;
          }

          let p2Value = this.player2Cards.cards[0].value
          if(p2Value == "ACE") {
            p2Value = 14;
          }else if (p2Value == "KING") {
            p2Value = 13;
          }else if (p2Value == "QUEEN") {
            p2Value = 12;
          }else if (p2Value == "JACK") {
            p2Value = 11;
          }

          // If the values are equal, or p1 wins
          // Give point to winner
          if (p1Value == p2Value){
            this.output = "Tie"
          }else if (p1Value > p2Value){
            this.output = "Player 1 Point!"
            this.player1Score = this.player1Score + 1
          }else {
            this.output = "Player 2 Point!"
            this.player2Score = this.player2Score + 1
          }

        },

        created: function(){
          this.drawCardP1
        }
      },

})

// API: http://deckofcardsapi.com/
