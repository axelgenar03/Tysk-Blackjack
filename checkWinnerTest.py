from Deck import Deck
import random

d = Deck()
deck = d.deck


def deal_hand() -> list:
    user_hand = []
    for i in range(5):
        index = random.randint(0,len(deck))
        user_hand.append(deck[index])
        del deck[index]
    print("\nYour hand: \n---------------")
    for card in user_hand:
        print(card.show())
    print("---------------")
    return user_hand


hand = deal_hand()

def check(hand) -> dict:
    suits_dict = {
        "Hearts": 0,
        "Diamonds": 0,
        "Spades": 0,
        "Clubs": 0
    }

    values_dict = {
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
    for card in hand:
        suits_dict[card.get_suit()] += 1

    for card in hand:
        values_dict[card.get_value()] += 1
        
    return suits_dict, values_dict

checked_suits, checked_values = check(hand)

print(str(checked_suits) + "\n")
print(checked_values)
