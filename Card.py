class Card:
    def __init__(self, value, face):
        self.value = value
        self.face = face

    def show(self):
        return f"{self.value} of {self.face}"