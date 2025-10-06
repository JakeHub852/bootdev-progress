# Ordering config:
# - Lower index in RANKS/SUITS means lower value.
# - Cards compare by rank first; if ranks tie, compare suit. 
# - Equality requires both rank and suit to match.


SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card:
    def __init__(self, rank, suit):
        # Store raw values
        self.rank = rank
        self.suit = suit
        # Precompute indices once so comparisons are O(1).
        # Assumes rank/suit exist in RANKS/SUITS; .index() raises ValueError otherwise.
        self.rank_index = RANKS.index(rank)
        self.suit_index = SUITS.index(suit)
        
    def __eq__(self, other):
        # Equal only if both rank and suit match
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        # Primary: rank; secondary (tiebreaker): suit
        if self.rank_index < other.rank_index:
            return True
        elif self.rank_index == other.rank_index:
            return self.suit_index < other.suit_index
        else:
            return False

    def __gt__(self, other):
        # Mirror logic of __lt__ for consistency
        if self.rank_index > other.rank_index:
            return True
        elif self.rank_index == other.rank_index:
            return self.suit_index > other.suit_index
        else:
            return False

    # don't touch below this line

    def __str__(self):
        return f"{self.rank} of {self.suit}"
