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
        if card.suit == "Hearts":
            suits_dict["Hearts"] += 1
        elif card.suit == "Diamonds":
            suits_dict["Diamonds"] += 1
        elif card.suit == "Spades":
            suits_dict["Spades"] += 1
        elif card.suit == "Clubs":
            suits_dict["Clubs"] += 1

    for card in hand:
        if card.value == "A":
            values_dict["A"] += 1
        elif card.value == "2":
            values_dict["2"] += 1
        elif card.value == "3":
            values_dict["3"] += 1
        elif card.value == "4":
            values_dict["4"] += 1
        elif card.value == "5":
            values_dict["5"] += 1
        elif card.value == "6":
            values_dict["6"] += 1
        elif card.value == "7":
            values_dict["7"] += 1
        elif card.value == "8":
            values_dict["8"] += 1 
        elif card.value == "9":
            values_dict["9"] += 1
        elif card.value == "10":
            values_dict["10"] += 1
        elif card.value == "J":
            values_dict["J"] += 1
        elif card.value == "Q":
            values_dict["Q"] += 1
        elif card.value == "K":
            values_dict["K"] += 1
        
    return suits_dict, values_dict

checked_suits, checked_values = check(hand)

print(str(checked_suits) + "\n")
print(checked_values)
