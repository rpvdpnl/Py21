import random

class Deck:
    
    def __init__(self):
        self.suits = ['H', 'D', 'C', 'S']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.deck = []
        i = 0

        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append({
                    'id': i,
                    's': suit,
                    'r': rank,
                    'v': 10 if rank in ['J', 'Q', 'K'] else (11 if rank == 'A' else int(rank))
                })
                i += 1
                
    def __str__(self):
        return str(self.deck)
                                
    def shuffle(self):
        random.shuffle(self.deck)

