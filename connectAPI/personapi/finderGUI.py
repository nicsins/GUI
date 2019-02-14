import tkinter as tk
from tkinter import *


class GUI:
    def __init__(self):
        self.main_window=tk.Tk()

        self.canvas=tk.Canvas(self.main_window,width=250,height=250,bg="blue",fg="beige")
