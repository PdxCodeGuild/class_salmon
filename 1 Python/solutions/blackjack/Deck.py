"""
# Deck.py
Deck module
"""

import random

class Card:
    """
    Card class
    """
    def __init__(self, rank, suit):
        """
        initialize card with rank and suit
        """
        self.rank = rank 
        self.suit = suit

    def __repr__(self):
        """
        returns string representation of Card object
        """
        return f'Card({self.rank}, {self.suit})'

    def __eq__(self, card):
        """
        returns true if this card's rank is equal to card.rank
        allows Card object to be compared using the == operator
        """
        return self.rank == card.rank



class Deck:
    """
    Deck class
    """
    def __init__(self):
        """
        initializes Deck object with cards property
        :cards: list of 52 Card objects sorted by rank and suit
        """
        ranks = ['A'] + list(range(2, 11)) + list('JQK')
        suits = ['clubs', 'diamonds', 'hearts', 'spades']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]

        # # equivalent to comprehension above
        # self.cards = []
        # for suit in suits:
        #     for rank in ranks:
        #         card = Card(rank, suit)
        #         self.cards.append(card)

    def __repr__(self):
        """
        returns string representation of Deck object
        """
        return str(self.cards)

    def __getitem__(self, i):
        """
        returns card at index i
        allows indexing of Deck object 
        """
        return self.cards[i]

    def __len__(self):
        """
        returns size of deck
        allows Deck object to be called with len()
        """
        return len(self.cards)

    def shuffle(self):
        """
        shuffles deck in place
        """
        random.shuffle(self.cards)

    def cut(self, i):
        """
        cuts deck at index i in place
        """
        self.cards = self.cards[i:] + self.cards[:i]

    def draw(self):
        """
        removes card at the top of the deck and returns it
        """
        return self.cards.pop()


# # card tests
# card1 = Card(2, 'Spades')
# card2 = Card(2, 'Hearts')
# # test __repr__ and __eq__
# print(card1, '=', card2, card1 == card2)
#                        # card1.__eq__(card2)

# # deck tests
# deck = Deck()
# # test __repr__
# # str(deck)
# # deck.__repr__()
# print(deck)
# random.shuffle(deck)
# # test __len__
# len(deck)
# print(deck)
# print(len(deck))
# deck.cut(8)
# print(deck)
# # test __getitem__
# print(deck[0])
# card = deck.draw()
# print(card)
# print(deck)
# deck.shuffle()
# print(deck)
# print(len(deck))

# deck = Deck()
# deck.shuffle()
# deck.cut(26)
# deck.draw()

# what goes on under the hood with __repr__
# print(thing)
# print(thing.__repr__())

# f'f-string {thing}'
# 'f-string' + str(thing)
# 'f-string' + thing.__repr__()