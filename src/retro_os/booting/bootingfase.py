import os.path
import tkinter as tk
from tkinter import PhotoImage
import PIL.ImageOps
from PIL import Image, ImageTk, ImageFilter, ImageEnhance

import retro_os
from retro_os.functions.booting import *
from retro_os.login.initializing import initializing_start


def bootloader(root):
    root.bind('<F12>', lambda event: bootloader_on_f12(event, root))
    root.config(bg="black")


    laptoplogo_path = os.path.expanduser("~/Onedrive/Documenten/Github/ThijmHacks/Retro-OS/src/retro_os/booting/laptop-logo.png")
    laptoplogo = Image.open(laptoplogo_path)
    laptoplogo_small = laptoplogo
    width, height = laptoplogo_small.size
    nwidth = int(width /10)
    nheight = int(height / 10)
    laptoplogo_resized = laptoplogo_small.resize((nwidth, nheight))
    laptoplogo = ImageTk.PhotoImage(laptoplogo_resized)


    root.laptoplogo = laptoplogo
    logolabel = tk.Label(root, image=laptoplogo, background="black")
    logolabel.place(relx=0.5, rely=0.3, anchor="center")


    global loading
    loading = root.after(10000, lambda: bootloader_await_5s(root))

def osloader(root):
    root.unbind_all('<F12>')
    root.config(background="black")

    oslogo_path = os.path.expanduser("~/Onedrive/Documenten/Github/ThijmHacks/Retro-OS/src/retro_os/booting/os-logo.png")
    oslogo_small = Image.open(oslogo_path)
    width, height = oslogo_small.size
    nwidth = width * 8
    nheight = height * 8
    oslogo_resized = oslogo_small.resize((nwidth, nheight))

    oslogo_sharp = oslogo_resized.filter(ImageFilter.SHARPEN)

    oslogo = ImageTk.PhotoImage(oslogo_sharp)

    root.oslogo = oslogo
    logolabel = tk.Label(root, image=oslogo, background="black")
    logolabel.place(relx=0.5, rely=0.5, anchor="center")


    root.after(10000, lambda: osloader_await_10s(root))

def otheros(root):
    root.config(background="darkblue")
    root.unbind_all('<F12>')
    while True:
        root.after_cancel(loading)