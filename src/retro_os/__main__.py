#Import modules from internet.
import tkinter as tk

#My own modules


#Project modules
from retro_os.window import window


class retro_os():
    def __init__(self):
        root = tk.Tk()
        retroos = window(root)

        retroos.master.title("Retro OS")
        retroos.master.attributes("-fullscreen", True)

        retroos.mainloop()