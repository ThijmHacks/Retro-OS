import tkinter as tk
from tkinter import PhotoImage

import retro_os.booting.fasechanger


def bootloader(root):
    root.config(background="black")
    label = tk.Label(root, text="Booting...", font=("Arial", 24))
    label.pack(side='top', anchor="center")
    button = tk.Button(root, text="Load OS into disk", font=("Arial", 14),
                       command=lambda: retro_os.booting.fasechanger.switch_fase(root, "osloader"))
    button.pack()


# noinspection PyTypeChecker
def osloader(root):
    root.config(background="lightgray")
    label = tk.Label(root, text="This is the OS Loader", font=("Arial", 24))
    label.pack()

    oslogo = PhotoImage(file="~/Onedrive/Documenten/Github/ThijmHacks/Retro-OS/src/retro_os/booting/os-logo.png")

    root.oslogo = oslogo
    logolabel = tk.Label(root, image=oslogo)
    logolabel.pack()
