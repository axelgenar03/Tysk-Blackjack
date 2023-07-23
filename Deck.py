from Card import Card

class Deck:
    def __init__(self):
        self.deck = 0
        deck = []
        possible_suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        possible_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for val in possible_values:
            for suit in possible_suits:
                deck.append(Card(val, suit))
        self.deck = deck

    def reset(self):
        deck = []
        possible_suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        possible_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for val in possible_values:
            for suit in possible_suits:
                deck.append(Card(val, suit))
        self.deck = deck