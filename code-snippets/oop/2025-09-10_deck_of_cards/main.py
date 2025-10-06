import random


class DeckOfCards:
    # Class-level constants: order matters for tests and expected behaviour
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self):
        # Private list to hold (rank, suit) tuples
        self.__cards = []
        # Build a fresh ordered deck on initialization
        self.create_deck()
     
    def create_deck(self):
        # Create all 52 cards in suit-major, rank-minor order
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.__cards.append ((rank, suit))

    def shuffle_deck(self):
        # In-place shuffle of the deck; random.seed outside can make this deterministic
        random.shuffle(self.__cards)

    def deal_card(self):
        # Deal from the "top" of the deck: the end of the list
        # Return None if the deck is empty
        if len(self.__cards) == 0:
            return None
        else: 
            return self.__cards.pop()

    # don't touch below this line

    def __str__(self):
        # Friendly string showing how many cards remain
        return f"The deck has {len(self.__cards)} cards"
