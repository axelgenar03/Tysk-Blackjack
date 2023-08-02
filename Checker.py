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
    
    def reset_categ(self):
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
   
    def controll_score(self, hand):
        self.reset_categ()
        self.categorize_hand(hand)
        if self.royal_straight_flush(hand):
            print("Royal Straight Flush")
            return True
        elif self.straight_flush(hand):
            print("Straight Flush")
            return True
        elif self.four_of_a_kind():
            print("Four of a Kind")
            return True
        elif self.full_house():
            print("Full House")
            return True
        elif self.flush():
            print("Flush")
            return True
        elif self.straight(hand):
            print("Straight")
            return True
        elif self.three_of_a_kind():
            print("Three of a Kind")
            return True
        elif self.two_pair():
            print("Two Pair")
            return True
        elif self.pair():
            print("Pair")
            return True
        else:
            print("High Card")
            return self.high_card(hand)



    # !! POKER HANDS !!

    def royal_straight_flush(self, hand):
        hand = hand
        return False
    
    def straight_flush(self, hand):
        straight = True
        flush = True
        straight_flush = False
        straight = self.straight(hand)
        flush = self.flush()
        if straight and flush:
            straight_flush = True
            self.score = 9
        return straight_flush

    def four_of_a_kind(self):
        four_of_a_kind = True
        values_amount_list = list(self.values_dict.values())
        if 4 in values_amount_list:
            self.score = 8
        else:
            four_of_a_kind = False
        return four_of_a_kind
    
    def full_house(self):
        full_house = True
        values_amount_list = list(self.values_dict.values())
        if 3 in values_amount_list and 2 in values_amount_list:
            self.score = 7
        else:
            full_house = False
        return full_house

    def flush(self):
        flush = True
        suits_amount_list = list(self.suits_dict.values())
        if 5 in suits_amount_list:
            self.score = 6
        else:
            flush = False
        return flush

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

    def three_of_a_kind(self):
        three_of_a_kind = True
        values_amount_list = list(self.values_dict.values())
        if 3 in values_amount_list:
            self.score = 4
        else:
            three_of_a_kind = False
        return three_of_a_kind

    def two_pair(self):
        two_pair = True
        values_amount_list = list(self.values_dict.values())
        amount_of_pairs = 0
        for num in values_amount_list:
            if num == 2:
                amount_of_pairs += 1
        if amount_of_pairs == 2:
            self.score = 3
        else:
            two_pair = False
        return two_pair

    def pair(self):
        pair = True
        values_amount_list = list(self.values_dict.values())
        if 2 in values_amount_list:
            self.score = 2
        else:
            pair = False
        return pair

    def high_card(self, hand):
        high_card = True
        high = -1
        for card in hand:
            x = self.card_order.index(card.value)
            if high == 0:
                break
            if x > high or x == 0:
                high = x
        self.score = 1
        return high_card

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

