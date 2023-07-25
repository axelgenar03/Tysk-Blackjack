from tkinter import *
from PIL import ImageTk, Image
#from main import change_hand
class GUI:

    def __init__(self) -> None:
        pass

    def gui(self,cards):
        
        
        window = Tk()
        canvas = Canvas()
        window.geometry("800x800")
        window.title("Blackjack")

        def drawcards(cards):
            Label(window, pady=80, padx=20, text=cards[0].show(), bg="#FFFFFF", fg="black", width=10, anchor='center').place(x=50, y=500)
            Label(window, pady=80, padx=20, text=cards[1].show(), bg="#FFFFFF", fg="black", width=10, anchor='center').place(x=190, y=500)
            Label(window, pady=80, padx=20, text=cards[2].show(), bg="#FFFFFF", fg="black", width=10, anchor='center').place(x=330, y=500)
            Label(window, pady=80, padx=20, text=cards[3].show(), bg="#FFFFFF", fg="black", width=10, anchor='center').place(x=470, y=500)
            Label(window, pady=80, padx=20, text=cards[4].show(), bg="#FFFFFF", fg="black", width=10, anchor='center').place(x=610, y=500)
            
        change_card1 = Button(window, text="change")
        change_card2 = Button(window, text="change")
        change_card3 = Button(window, text="change")
        change_card4 = Button(window, text="change")
        change_card5 = Button(window, text="change")
         
        change_card1.place(x=75, y=700)
        change_card2.place(x=215, y=700)
        change_card3.place(x=355, y=700)
        change_card4.place(x=495, y=700)
        change_card5.place(x=635, y=700)
 
        drawcards(cards)
        canvas.pack()
        window.mainloop()

