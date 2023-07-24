class Checker:
    def __init__(self):
        self.suits_dict = {
            "Hearts": 0,
            "Diamonds": 0,
            "Spades": 0,
            "Clubs": 0
        }

        self.values_dict = {
            "A": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0,
            "7": 0,
            "8": 0,
            "9": 0,
            "10": 0,
            "J": 0,
            "Q": 0,
            "K": 0
        }
        self.score = 0
        self.hand = []

    def categorize_hand(self, player_hand) -> bool:
        for card in player_hand:
            self.suits_dict[card.get_suit()] += 1

        for card in player_hand:
            self.values_dict[card.get_value()] += 1
        return True
    
    def high_card(self, player_hand):
        # TODO logiken för high card
        return 1

    # High card
    # Pair
    # Two pair
    # Three of a kind
    # Straight
    # Flush
    # Full house
    # Four of a kind
    # Straight flush
    # Royal straight flush

