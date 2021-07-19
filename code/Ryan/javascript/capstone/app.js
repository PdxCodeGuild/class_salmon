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
                url: `http://deckofcardsapi.com/api/deck/${this.deckID}/draw/?count=1`
              }).then(response => {
                this.player1Cards = response.data;
                this.cardsRemaining = response.data.remaining;
                this.output = "Player 2 Turn"
              })
        },

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

    },

})



// -----------------------------------------------------------------------------
// A Brand New Deck:
// http://deckofcardsapi.com/api/deck/new/
// Open a brand new deck of cards.
// A-spades, 2-spades, 3-spades... followed by diamonds, clubs, then hearts.
//
// Response:
// {
//     "success": true,
//     "deck_id": "3p40paa87x90",
//     "shuffled": false,
//     "remaining": 52
// }
// -----------------------------------------------------------------------------
// Reshuffle the Cards:
// http://deckofcardsapi.com/api/deck/<<deck_id>>/shuffle/
// Don't throw away a deck when all you want to do is shuffle.
// Include the deck_id on your call to shuffle your cards.
// Don't worry about reminding us how many decks you are playing with.
//
// Response:
// {
//    "success": true,
//    "deck_id": "3p40paa87x90",
//    "shuffled": true,
//    "remaining": 52
// }
// -----------------------------------------------------------------------------
// Adding to Piles
// http://deckofcardsapi.com/api/deck/<<deck_id>>/pile/<<pile_name>>/add/?cards=AS,2S
// Piles can be used for discarding, players hands, or whatever else.
// Piles are created on the fly, just give a pile a name and add a drawn card to the pile.
// If the pile didn't exist before, it does now.
// After a card has been drawn from the deck it can be moved from pile to pile.
//
// Note: This will not work with multiple decks.
//
// Response:
// {
//     "success": true,
//     "deck_id": "3p40paa87x90",
//     "remaining": 12,
//     "piles": {
//         "discard": {
//             "remaining": 2
//         }
//     }
// }
// -----------------------------------------------------------------------------
// Drawing from Piles
// http://deckofcardsapi.com/api/deck/<<deck_id>>/pile/<<pile_name>>/draw/?cards=AS
// http://deckofcardsapi.com/api/deck/<<deck_id>>/pile/<<pile_name>>/draw/?count=2
// http://deckofcardsapi.com/api/deck/<<deck_id>>/draw/bottom/
// Specify the cards that you want to draw from the pile.
// The default is to just draw off the top of the pile (it's a stack).
// Or add the bottom parameter to the URL to draw from the bottom.
//
// Response:
// {
//     "success": true,
//     "deck_id": "3p40paa87x90",
//     "remaining": 12,
//     "piles": {
//         "discard": {
//             "remaining": 1
//         }
//     },
//     "cards": [
//         {
//             "image": "http://deckofcardsapi.com/static/img/AS.png",
//             "value": "ACE",
//             "suit": "SPADES",
//             "code": "AS"
//         }
//     ]
// }
