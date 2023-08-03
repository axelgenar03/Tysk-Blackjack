from Deck import Deck
from Wallet import Wallet
from Checker import Checker
import sys
from termcolor import colored
import random
import os
from tkinter import *
from PIL import ImageTk, Image
diamonds_img = [None,None,None,None,None]
clubs_img = [None,None,None,None,None]
hearts_img = [None,None,None,None,None]
spades_img = [None,None,None,None,None]
checker = Checker()
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

player_hand = deal_hand()


checker.categorize_hand(player_hand)
print(f"{checker.values_dict}")



cardidx = [False,False,False,False,False]
def drawcards(window,cards):
    global global_img  # Declare the global_img variable to store the image reference
    Label(window, pady=80, padx=20, text=cards[0].show(), bg="#FFFFFF", fg="black", width=10, anchor='center').place(x=50, y=500)
    Label(window, pady=80, padx=20, text=cards[1].show(), bg="#FFFFFF", fg="black", width=10, anchor='center').place(x=190, y=500)
    Label(window, pady=80, padx=20, text=cards[2].show(), bg="#FFFFFF", fg="black", width=10, anchor='center').place(x=330, y=500)
    Label(window, pady=80, padx=20, text=cards[3].show(), bg="#FFFFFF", fg="black", width=10, anchor='center').place(x=470, y=500)
    Label(window, pady=80, padx=20, text=cards[4].show(), bg="#FFFFFF", fg="black", width=10, anchor='center').place(x=610, y=500)
   
    
 #function to draw card valorer
    def diamonds(window, x):
        global diamonds_img  
        diamond_img = Image.open('suits_images/diamonds.png')
        resized_diamond_img = diamond_img.resize((50, 50))
        diamonds_img[x] = ImageTk.PhotoImage(resized_diamond_img)
        label = Label(window, image=diamonds_img[x])
        label.configure(bg="#FFFFFF")
        xcord = x * 140
        xcord +=50
        print(xcord)
        label.place(x=xcord,y=500)
    
    def clubs(window, x):
        global clubs_img  
        club_img = Image.open('suits_images/blubs.png')
        resized_club_img = club_img.resize((50, 50))
        clubs_img[x] = ImageTk.PhotoImage(resized_club_img)
        label = Label(window, image=clubs_img[x])
        label.configure(bg="#FFFFFF")
        xcord = x * 140
        xcord +=50
        print(xcord)
        label.place(x=xcord,y=500)
    
    def hearts(window, x):
        global hearts_img
        heart_img = Image.open('suits_images/hearts.png')
        resized_heart_img = heart_img.resize((50, 50))
        hearts_img[x] = ImageTk.PhotoImage(resized_heart_img)
        label = Label(window, image=hearts_img[x])
        label.configure(bg="#FFFFFF")
        xcord = x * 140
        xcord +=50
        print(xcord)
        label.place(x=xcord,y=500)

    def spades(window, x):
        global spades_img  
        spade_img = Image.open('suits_images/spades.png')
        resized_spade_img = spade_img.resize((50, 50))
        spades_img[x] = ImageTk.PhotoImage(resized_spade_img)
        label = Label(window, image=spades_img[x])
        label.configure(bg="#FFFFFF")
        xcord = x * 140
        xcord +=50
        print(xcord)
        label.place(x=xcord,y=500)
    
    z = 0
    while z < 5:
        print(z)
        if cards[z].suit == "Diamonds":
            diamonds(window,z)
        if cards[z].suit == "Clubs":
            clubs(window,z)
        if cards[z].suit == "Hearts":
            hearts(window,z)
        if cards[z].suit == "Spades":
            spades(window,z)
        z+=1
    
    return

def placebuttons(window):


        change_card1 = Button(window, text="change" ,highlightbackground="#808080", command=lambda: cardidxchange(window,0))
        change_card2 = Button(window, text="change" ,highlightbackground="#808080", command=lambda: cardidxchange(window,1))
        change_card3 = Button(window, text="change" ,highlightbackground="#808080", command=lambda: cardidxchange(window,2))
        change_card4 = Button(window, text="change" ,highlightbackground="#808080", command=lambda: cardidxchange(window,3))
        change_card5 = Button(window, text="change" ,highlightbackground="#808080", command=lambda: cardidxchange(window,4))
        
        change_card1.place(x=75, y=700)
        change_card2.place(x=215, y=700)
        change_card3.place(x=355, y=700)
        change_card4.place(x=495, y=700)
        change_card5.place(x=635, y=700)

        change_card_button = Button(window, text="draw" ,highlightbackground="#808080", command=lambda: drawnewcards(cardidx,player_hand,window))
        change_card_button.place(x=690, y=740)

def drawnewcards(cardidx,player_hand,window):
    i = 0
    while i < 5:
        if cardidx[i] == True:
            index = random.randint(0, len(deck))
            player_hand[i] = deck[index]
            del deck[index]
            placebuttons(window)
        i += 1
    drawcards(window,player_hand)
    show_player_hand(player_hand)
    checker.controll_score(player_hand)
    print(checker.score)
    return 


def cardidxchange(window,i):
            if cardidx[i] == False:
                cardidx[i] = True
                Label(window,text="!", bg="#808080",font=("Arial",25)).place(x=107+140*i, y=740)
            elif cardidx[i] == True:
                cardidx[i] = False
                Label(window,text="!",bg="#808080", fg="#808080",font=("Arial",25)).place(x=107+140*i, y=740)
            print(cardidx)
            return

def gui(cards):
        window = Tk()
        window.geometry("800x800")
        window.title("Blackjack")
        window.configure(bg="#808080")
        placebuttons(window)
        drawcards(window,cards)
        window.mainloop()    

gui(player_hand)
