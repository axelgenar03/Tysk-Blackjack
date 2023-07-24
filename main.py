from Deck import Deck
from Wallet import Wallet
from Checker import Checker
import sys
from termcolor import colored
import random
import os

checker = Checker()
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
    j = 1
    for card in user_hand:
        print(f"[{j}] {card.show()}")
        j += 1
    print("---------------")
    return user_hand
    
    
def dealer_hand():
    dealer_hand = []
    for i in range(5):
        index = random.randint(0,len(deck))
        dealer_hand.append(deck[index])
        del deck[index]
    #for card in user_hand:

def show_player_hand(player_hand):
    os.system("cls" if os.name == "nt" else "clear")
    print("\nYour hand: \n---------------")
    j = 1
    for card in player_hand:
        print(f"[{j}] {card.show()}")
        j += 1
    print("---------------\n")

"""
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
""" 

def change_hand(player_hand):
    show_player_hand(player_hand)
    player_choice = input("Would you like to change any cards? [Y/N]: ").upper()
    if player_choice == "N":
        return False
    elif player_choice == "Y":
        pass
    else:
        return False
    notice = colored("""\nNOTE!\nEnter using this format: \'1,4,5\'. The example swaps cards 1, 4 and 5! If only one card needs to be swapped, just enter that one with no comma\n""", "red")
    cards_to_swap_input = input(notice + "Enter the cards you want to swap: ")
    cards_to_swap = cards_to_swap_input.split(",")
    for i in range(len(cards_to_swap)):
        cards_to_swap[i] = int(cards_to_swap[i])
    for i in range(len(cards_to_swap)):
        index = random.randint(0, len(deck))
        player_hand[cards_to_swap[i] - 1] = deck[index]
        del deck[index]
    show_player_hand(player_hand)

player_hand = deal_hand()
dealer_hand()
change_hand(player_hand)
change_hand(player_hand)

checker.categorize_hand(player_hand)
print(f"{checker.values_dict} \n {checker.suits_dict}")