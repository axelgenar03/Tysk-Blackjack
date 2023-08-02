from tkinter import *
from PIL import ImageTk, Image
#from main import change_hand
class GUI:

    def __init__(self) -> None:
        pass

    def drawcards(self,window, cards):
        Label(window, pady=80, padx=20, text=cards[0].show(), bg="#FFFFFF", fg="black", width=10, anchor='center').place(x=50, y=500)
        Label(window, pady=80, padx=20, text=cards[1].show(), bg="#FFFFFF", fg="black", width=10, anchor='center').place(x=190, y=500)
        Label(window, pady=80, padx=20, text=cards[2].show(), bg="#FFFFFF", fg="black", width=10, anchor='center').place(x=330, y=500)
        Label(window, pady=80, padx=20, text=cards[3].show(), bg="#FFFFFF", fg="black", width=10, anchor='center').place(x=470, y=500)
        Label(window, pady=80, padx=20, text=cards[4].show(), bg="#FFFFFF", fg="black", width=10, anchor='center').place(x=610, y=500)
        return

    def cardidxchange(self,window,i):
            if self.cardidx[i] == False:
                self.cardidx[i] = True
                Label(window,text="!", bg="#808080",font=("Arial",25)).place(x=107+140*i, y=740)
            elif self.cardidx[i] == True:
                self.cardidx[i] = False
                Label(window,text="!",bg="#808080", fg="#808080",font=("Arial",25)).place(x=107+140*i, y=740)
            print(self.cardidx)
            return

    def placebuttons(self,window):
        change_card1 = Button(window, text="change" ,highlightbackground="#808080", command=lambda: self.cardidxchange(window,0))
        change_card2 = Button(window, text="change" ,highlightbackground="#808080", command=lambda: self.cardidxchange(window,1))
        change_card3 = Button(window, text="change" ,highlightbackground="#808080", command=lambda: self.cardidxchange(window,2))
        change_card4 = Button(window, text="change" ,highlightbackground="#808080", command=lambda: self.cardidxchange(window,3))
        change_card5 = Button(window, text="change" ,highlightbackground="#808080", command=lambda: self.cardidxchange(window,4))
            
        change_card1.place(x=75, y=700)
        change_card2.place(x=215, y=700)
        change_card3.place(x=355, y=700)
        change_card4.place(x=495, y=700)
        change_card5.place(x=635, y=700)        

    
    def gui(self,cards):
        
        self.cardidx = [False,False,False,False,False]
        window = Tk()
        window.geometry("800x800")
        window.title("Blackjack")
        window.configure(bg="#808080")
        self.drawcards(window,cards)
        self.placebuttons(window)
        window.mainloop()

