import os.path
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

import retro_os

def on_f2(event, root):
    print("F2 has been pressed")
    retro_os.booting.fasechanger.switch_fase(root, "otheros")

def on_space(event, root):
    print("Space has been pressed")
    retro_os.booting.fasechanger.switch_fase(root, "osloader")

def bootloader(root):
    root.bind('<F2>', lambda event: on_f2(event, root))
    root.bind('<space>', lambda event: on_space(event, root))

    root.config(background="black")
    label = tk.Label(root, text="Booting...", font=("Arial", 24))
    label.pack(side='top', anchor="center")

def osloader(root):
    root.config(background="lightgray")

    oslogo_path = os.path.expanduser("~/Onedrive/Documenten/Github/ThijmHacks/Retro-OS/src/retro_os/booting/os-logo.png")
    oslogo_small = Image.open(oslogo_path)
    width, height = oslogo_small.size
    nwidth = width * 4
    nheight = height * 4
    oslogo_resized = oslogo_small.resize((nwidth, nheight))

    oslogo = ImageTk.PhotoImage(oslogo_resized)

    root.oslogo = oslogo
    logolabel = tk.Label(root, image=oslogo, background="lightgray")
    logolabel.place(relx=0.5, rely=0.5, anchor="center")

def otheros(root):
    root.config(background="blue")