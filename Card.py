class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def show(self):
        return f"{self.value} of {self.suit}"