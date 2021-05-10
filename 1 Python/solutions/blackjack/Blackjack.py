# BlackJack.py
from Deck import Card, Deck

class Hand:
    """
    represents a player's hand in blackjack
    """
    def __init__(self, card1, card2):
        """
        initializes Hand object with two cards
        """
        self.cards = [card1, card2]
        # self.points = {'A': 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'J': 10, 'Q': 10, 'K': 10}
        # equivalent to above
        face = [(fc, 10) for fc in 'JQK']
        number = [(num, num) for num in range(2, 11)]
        self.points = dict([('A', 1)] + face + number)

    def __repr__(self):
        """
        returns string representation of Hand
        """
        return str(self.cards)

    def score(self):
        """
        returns total of points in hand (handles ace hi/lo)
        """
        # handle ace hi/lo
        points = 0
        aces = None
        for card in self.cards:
            points += self.points[card.rank]
            if card.rank == 'A': # change aces flag to true
                aces = True

        # if we have at least one ace and our total points <= 11,
        # choose ace high
        if points <= 11 and aces:
            points += 10

        return points

        # # old solution (doesn't handle ace hi/lo)
        # return sum([self.points[card.rank] for card in self.cards])

    def add(self, card):
        """
        adds card to hand
        """
        self.cards.append(card)


class Dealer(Hand):
    """
    Dealer extends Hand
    """
    def __init__(self, card1, card2):
        super().__init__(card1, card2)

    def one_face_down(self):
        """
        prints dealer's hand with first card hidden
        """ 
        hidden = Card('Hidden', 'Hidden')
        return [hidden] + self.cards[1:]

        # for i in range(1, len(self.cards)):
        #     print(self.cards[i])

    def visible_score(self):
        # self.points = {'A': 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'J': 10, 'Q': 10, 'K': 10}
        hidden_card = self.cards[0]
        return self.score() - self.points[hidden_card.rank]


class Game:
    def __init__(self, cut_index, num_players=1):
        """
        initialize Game object with the following properties:
        :deck: Deck object, shuffled and cut with the cut_index
        :players: list of Hand objects
        :dealer: Dealer object
        """
        # set up deck
        self.deck = Deck()
        self.deck.shuffle()
        self.deck.cut(cut_index)

        # create player hands
        self.players = []
        for i in range(num_players):
            # fill player hand with two cards drawn from the game's deck
            player = Hand(self.deck.draw(), self.deck.draw())
            self.players.append(player)

        # create dealer
        # fill dealer hand with two cards drawn from the game's deck
        self.dealer = Dealer(self.deck.draw(), self.deck.draw())


    def play(self):
        """
        Game logic
        """
        # display player's visible cards and visible score
        print('-'*48)
        print("Dealer's hand")
        print(self.dealer.one_face_down())
        print("Dealer's score:", self.dealer.visible_score())
        print('-'*48)

        # loop through players
        for i, player in enumerate(self.players):
            print('-'*48)
            print(f"Player {i+1}'s turn")
            print(player) # display player's hand
            print(f"Score: {player.score()}")
            print('-'*48)
            while player.score() < 21: # loop while player is hitting and not blackjack or busted
                while True: # input validation
                    move = input('Hit or stay: ').strip().lower()
                    if move in ['hit', 'h', 'stay', 's']:
                        break
                # if the player hits, draw from the deck and add a card to their hand
                if move.startswith('h'):
                    player.add(self.deck.draw())
                    print(player) 
                else: # if the player stays, stop asking for another move
                    break
            if player.score() > 21:
                print('Player busted')
            elif player.score() == 21:
                print('Blackjack!')

        # dealer's move
        print('-'*48)
        print("Dealer's turn")
        print('-'*48)
        print(self.dealer.one_face_down())
        # dealer hits if their score < 17
        while self.dealer.score() < 17:
            print('Dealer hits')
            # draw a card from the deck and add it to the dealer's hand
            self.dealer.add(self.deck.draw())
            print(self.dealer.one_face_down())
        # stay if 17 <= score < 21
        if self.dealer.score() < 21:
            print('Dealer stays!')
        # blackjack
        elif self.dealer.score() == 21:
            print('Blackjack!')
        # busted
        else:
            print('Dealer busted!')

        # reveal dealer's full hand
        print('-'*48)
        print("Dealer's final hand")
        print('-'*48)
        print(self.dealer)
        print("Dealer's score:", self.dealer.score())

        # calculate winner(s)
        for i, player in enumerate(self.players):
            print('-'*48)
            print(f"Player {i+1}'s hand")
            print(player)            
            print(f"Score: {player.score()}")
            print('-'*48)
            # player loses if they busted or if their score is less than the dealer's
            if (player.score() > 21) or player.score() <= self.dealer.score() <= 21:
                print(f'Player {i+1} loses :(')
            else:
                print(f'Player {i+1} wins!')


if __name__ == '__main__':
    print('-'*48)
    print("Welcome to Blackjack!")
    print('-'*48)

    while True: # input validation
        try:
            players = int(input('How many players: '))
            break
        except ValueError:
            pass

    while True: # loop game
        while True: # input validation
            try:
                cut = int(input("Cut the deck: "))
                break
                # if 0 <= cut < 52:
                #     break
                # raise ValueError
            except ValueError:
                print('Enter a number to cut the deck by.')

        # create Game object
        blackjack = Game(cut, players)
        blackjack.play()

        # ask if user wants to play again 
        while True: # input validation
            play_again = input('Do you want to play again: ').strip().lower()
            if play_again in ['y', 'yes', 'n', 'no']:
                break
        if play_again.startswith('n'):
            print('Goodbye!')
            break
