import tkinter as tk
from tkinter import PhotoImage
import os


import retro_os
from retro_os.functions.installing_retro import *
import retro_os.functions.users as usr

def login_screen(root):
    root.config(bg="#51A69D")
    root.unbind_all('<F12>')

    frame_width = root.winfo_screenwidth() // 1.5
    frame_height = root.winfo_screenheight() // 1.5

    user_interface = tk.Frame(root, width=frame_width, height=frame_height, background="#A0D9D3")
    user_interface.place(relx=0.5, rely=0.5, anchor="center")


    title_welcome = tk.Label(user_interface, text="System has started", background="#A0D9D3")
    title_welcome.config(font=("Bauhaus 93", 72))
    title_welcome.place(relx=0.5,rely=0.35, anchor="center")