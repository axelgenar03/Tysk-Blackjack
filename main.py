from Deck import Deck
from Wallet import Wallet
import random
wallet = Wallet()
deck_class = Deck()
deck = deck_class.deck
global player_hand


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
    return user_hand
    
    
def dealer_hand():
    dealer_hand = []
    for i in range(5):
        index = random.randint(0,len(deck))
        dealer_hand.append(deck[index])
        del deck[index]
    #for card in user_hand:

def change_hand(player_hand):
    amount_change = int(input("How many cards do you want to change?:\n")) 
    i = amount_change
    while i > 0:
        if i == amount_change:
            bad_card = int(input("Choose a card to exchange:\n"))
        else:  
            bad_card = int(input("Choose another card to exchange:\n"))
        bad_card -= 1
        index = random.randint(0,len(deck))
        player_hand[bad_card] = (deck[index])
        del deck[index]
        i-=1    
    print("\nYour hand: \n---------------")

    for card in player_hand:
        print(card.show())
    print("---------------")
        

player_hand = deal_hand()
dealer_hand()
change_hand(player_hand)

