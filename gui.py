from tkinter import *
from PIL import ImageTk, Image
class GUI:

    def __init__(self) -> None:
        pass

    def gui(self,cards):
        print(cards)
        
        window = Tk()
        canvas = Canvas()
        window.geometry("800x800")
        window.title("Blackjack")


        Label(window, pady=80, padx=20, text=cards[0].show(), bg="#FFFFFF", fg="black", width=10, anchor='center').place(x=50, y=500)
        Label(window, pady=80, padx=20, text=cards[1].show(), bg="#FFFFFF", fg="black", width=10, anchor='center').place(x=190, y=500)
        Label(window, pady=80, padx=20, text=cards[2].show(), bg="#FFFFFF", fg="black", width=10, anchor='center').place(x=330, y=500)
        Label(window, pady=80, padx=20, text=cards[3].show(), bg="#FFFFFF", fg="black", width=10, anchor='center').place(x=470, y=500)
        Label(window, pady=80, padx=20, text=cards[4].show(), bg="#FFFFFF", fg="black", width=10, anchor='center').place(x=610, y=500)






        canvas.pack()
        window.mainloop()