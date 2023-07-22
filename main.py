from Deck import Deck
import random
deck_class = Deck()
deck = deck_class.deck



def deal_hand():
    user_hand = []
    user_hand.append(deck[random.randint(0,52)])
    user_hand.append(deck[random.randint(0,52)])
    for card in user_hand:
        print(card.show())

deal_hand()





