import tkinter as tk

class window(tk.Frame):
    def __init__(self, master):
        print("Working Window")
        super().__init__(master)
        self.pack()