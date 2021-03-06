import random

##### Class represeting a BlackJack Deck ######
"""
    Attributes of a Deck
    - 52 cards, 4 of each, ignoring suit for blackjack

    Required functionality
    - to be shuffled
    - to deal a card
    

"""


class Deck:

    # A list of tuples should be a good choice as they are immutable
    def __init__(self):
        self.cards = [("2", 2), ("3", 3), ("4", 4),
                      ("5", 5), ("6", 6), ("7", 7),
                      ("8", 8), ("9", 9), ("10", 10),
                      ("J", 10), ("Q", 10), ("K", 10),
                      ("A", 11)] * 4

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


