import tkinter as tk
from tkinter import PhotoImage

import retro_os
from retro_os.keypresses.login import *


def initializing_start(root):
    root.config(bg="#51A69D")
    root.unbind_all('<F12>')

    frame_width = root.winfo_screenwidth() // 1.5
    frame_height = root.winfo_screenheight() // 1.5

    user_interface = tk.Frame(root, width=frame_width, height=frame_height, background="#A0D9D3")
    user_interface.place(relx=0.5, rely=0.5, anchor="center")


    start_button = tk.Button(user_interface, text="Lets go!", command= lambda: retro_os.keypresses.login.initializing_start_button(root))
    start_button.config(font=("Bauhaus 93", 36))
    start_button.place(relx=0.5,rely=0.85,anchor="center")


    title_welcome = tk.Label(user_interface, text="Welcome to\nRetro OS", background="#A0D9D3")
    title_welcome.config(font=("Bauhaus 93", 72))
    title_welcome.place(relx=0.5,rely=0.35, anchor="center")




def language_select(root):
    root.config(bg="#51A69D")

    frame_width_2 = root.winfo_screenwidth() // 1.5
    frame_height_2 = root.winfo_screenheight() // 1.5

    user_interface_2 = tk.Frame(root, width=frame_width_2, height=frame_height_2, background="#A0D9D3")
    user_interface_2.place(relx=0.5, rely=0.5, anchor="center")