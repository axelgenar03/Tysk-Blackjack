from tkinter import *
from PIL import ImageTk, Image
class GUI:

    def __init__(self) -> None:
        pass

    def gui(self,cards):
        window = Tk()
        canvas = Canvas()
        window.geometry("800x800")
        window.title("Blackjack")


        Label(window,pady=80,padx=40, text="Kort 1", bg="#FFFF00", fg="white").place(x=50, y=500)
        Label(window,pady=80,padx=40, text="Kort 2", bg="#3300CC", fg="white").place(x=180, y=500)
        Label(window,pady=80,padx=40, text="Kort 3", bg="#FF0099", fg="white").place(x=310, y=500)
        Label(window,pady=80,padx=40, text="Kort 4", bg="#FF0123", fg="white").place(x=440, y=500)
        Label(window,pady=80,padx=40, text="Kort 5", bg="#00FF00", fg="white").place(x=570, y=500)






        canvas.pack()
        window.mainloop()