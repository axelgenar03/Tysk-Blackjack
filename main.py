import tkinter
from Deck import Deck
from Wallet import Wallet
import random
wallet = Wallet()
deck_class = Deck()
deck = deck_class.deck



def deal_hand():
    user_hand = []
    for i in range(5):
        index = random.randint(0,len(deck))
        user_hand.append(deck[index])
        del deck[index]
    print("\nYour hand: \n---------------")
    for card in user_hand:
        print(card.show())
    print("---------------")


def dealer_hand():
    user_hand = []
    for i in range(5):
        index = random.randint(0,len(deck))
        user_hand.append(deck[index])
        del deck[index]
    #for card in user_hand:
        




deal_hand()

dealer_hand()


#print(wallet.balance)
#wallet.deduct_balance(int(input("Enter Amount to Deduct: ")))



