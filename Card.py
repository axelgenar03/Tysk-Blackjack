class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def show(self):
        return f"{self.value}"
    
    def get_value(self):
        return self.value
    
    def get_suit(self):
        return self.suit
    
    def set_value(self, value):
        self.value = value

    def set_suit(self, suit):
        self.suit = suit