
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
    #show_player_hand(player_hand)
