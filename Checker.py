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

        self.card_order = [
            "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"
        ]
        self.score = 0
        self.final_hand = []

    def categorize_hand(self, player_hand) -> bool:
        for card in player_hand:
            self.suits_dict[card.get_suit()] += 1

        for card in player_hand:
            self.values_dict[card.get_value()] += 1
        return True
   
    def royal_straight_flush(self, hand):
        pass
    
    def straight_flush(self, hand):
        low = 100
        for card in hand:
            i = self.card_order.index(card.value)
            if i < low:
                low = i
        print(low)

    def four_of_a_kind(self, hand):
        pass
    
    def full_house(self, hand):
        pass

    def flush(self, hand):
        pass

    def straight(self, hand):
        straight = True
        low = 100
        for card in hand:
            x = self.card_order.index(card.value)
            if x < low:
                low = x
        low += 1
        hand_values = []
        for card in hand:
            hand_values.append(card.value)
        for i in range(len(hand)-1):
            if self.card_order[low + i] != hand_values[i + 1]:
                straight = False
                break
        if straight:
            self.score = 5
        return straight


    def three_of_a_kind(self, hand):
        pass

    def two_pair(self, hand):
        pass

    def pair(self, hand):
        pass

    def high_card(self, hand):
        pass

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

