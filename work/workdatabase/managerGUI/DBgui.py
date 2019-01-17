import tkinter as tk


class firstGUI(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("My First GUI")
        self.grid()
        self._label = Label(self, text = "I'm a label!")
        self._label.grid()