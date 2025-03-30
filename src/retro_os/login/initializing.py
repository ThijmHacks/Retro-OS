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

    frame_width = root.winfo_screenwidth() // 1.5
    frame_height = root.winfo_screenheight() // 1.5

    user_interface = tk.Frame(root, width=frame_width, height=frame_height, background="#A0D9D3")
    user_interface.place(relx=0.5, rely=0.5, anchor="center")

    start_button = tk.Button(user_interface, text="Fix current Retro OS\ninstallation", command= lambda: retro_os.keypresses.login.fix_current_retro_os(root))
    start_button.config(font=("Bauhaus 93", 12))
    start_button.place(relx=0.05,rely=0.95,anchor="sw")

def fix_current_installation(root):
    root.config(bg="#51A69D")

    frame_width = root.winfo_screenwidth() // 1.5
    frame_height = root.winfo_screenheight() // 1.5

    user_interface = tk.Frame(root, width=frame_width, height=frame_height, background="#A0D9D3")
    user_interface.place(relx=0.5, rely=0.5, anchor="center")

    back_button = tk.Button(user_interface, text="Back", command= lambda: retro_os.keypresses.login.initializing_start_button(root))
    back_button.config(font=("Bauhaus 93", 36))
    back_button.place(relx=0.5,rely=0.85,anchor="center")

    title_fixing = tk.Label(user_interface, text="This function cant be used yet,\n press the back button below to go back.", background="#A0D9D3")
    title_fixing.config(font=("Bauhaus 93", 42))
    title_fixing.place(relx=0.5,rely=0.35, anchor="center")


