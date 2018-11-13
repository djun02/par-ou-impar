from tkinter import *

class App:
    def __init__(self, master = None):
        self.a = master

        self.label = Label(self.a)
        self.label["text"] = "Digite um número"
        self.label.grid(columnspan=2)

        self.entry = Entry(self.a)
        self.entry.grid(row=1, column=1)

        self.button = Button(self.a)
        self.button["text"] = "Btn"
        self.button["command"] = lambda: self.mudaLabel()
        self.button.grid(row=3,column=1)

        self.label2 = Label(self.a)
        self.label["text"]


    def mudaLabel(self):
        n = int(self.entry.get())
        if n%2 == 0:
            self.label["text"] ="par"
        elif n%2 == 1:
            self.label["text"] = "impar"




root = Tk()
App(root)
root.mainloop()
