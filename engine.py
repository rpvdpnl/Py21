import random

class BlackjackEngine:
    def __init__(self, num_decks=1):
        """
        Initialize the Blackjack engine with the specified number of decks.
        """
        self.num_decks = num_decks
        self.reset_deck()

    def reset_deck(self):
        """
        Create a shuffled deck of cards based on the number of decks.
        """
        single_deck = [str(value) for value in range(2, 11)] + ['J', 'Q', 'K', 'A']
        self.deck = single_deck * 4 * self.num_decks
        random.shuffle(self.deck)

    def draw_card(self):
        """
        Draw a single card from the deck. If the deck is empty, reset it.
        """
        if not self.deck:
            self.reset_deck()
        return self.deck.pop()

    def calculate_hand_value(self, hand):
        """
        Calculate the value of a hand in Blackjack.
        """
        value = 0
        aces = 0

        for card in hand:
            if card in ['J', 'Q', 'K']:
                value += 10
            elif card == 'A':
                value += 11
                aces += 1
            else:
                value += int(card)

        # Adjust for aces if necessary
        while value > 21 and aces:
            value -= 10
            aces -= 1

        return value

    def play_round(self, player_strategy=None):
        """
        Simulate a single round of Blackjack. Returns the outcome.
        """
        if player_strategy is None:
            player_strategy = self.default_strategy

        # Initial hands
        player_hand = [self.draw_card(), self.draw_card()]
        dealer_hand = [self.draw_card(), self.draw_card()]

        # Player's turn
        while player_strategy(player_hand, dealer_hand[0], self.calculate_hand_value(player_hand)):
            player_hand.append(self.draw_card())

        player_value = self.calculate_hand_value(player_hand)
        if player_value > 21:
            return "Loss"  # Player busted

        # Dealer's turn
        while self.calculate_hand_value(dealer_hand) < 17:
            dealer_hand.append(self.draw_card())

        dealer_value = self.calculate_hand_value(dealer_hand)

        # Determine outcome
        if dealer_value > 21 or player_value > dealer_value:
            return "Win"
        elif player_value == dealer_value:
            return "Push"  # Tie
        else:
            return "Loss"

    def default_strategy(self, player_hand, dealer_upcard, player_value):
        """
        Basic strategy: Always hit if hand value is below 17.
        """
        return player_value < 17


# Example usage
if __name__ == "__main__":
    engine = BlackjackEngine(num_decks=1)
    result = engine.play_round()
    print(f"Round result: {result}")
