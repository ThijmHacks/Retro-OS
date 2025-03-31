import tkinter as tk
from tkinter import PhotoImage
import os


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




def location_select(root):
    root.config(bg="#51A69D")

    frame_width = root.winfo_screenwidth() // 1.5
    frame_height = root.winfo_screenheight() // 1.5

    user_interface = tk.Frame(root, width=frame_width, height=frame_height, background="#A0D9D3")
    user_interface.place(relx=0.5, rely=0.5, anchor="center")

    title_page = tk.Label(user_interface, text="Please select the location.", background="#A0D9D3")
    title_page.config(font=("Bauhaus 93", 24))
    title_page.place(relx=0.5, rely=0.05, anchor="n")

    running_directory = os.getcwd()
    location_running = tk.Label(user_interface, text=f"Current location: {running_directory}", background="#A0D9D3")
    location_running.config(font=("Calibris", 11, 'bold'))
    location_running.place(relx=0.1, rely=0.3, anchor="w")

    start_button = tk.Button(user_interface, text="Fix current Retro OS\ninstallation", command= lambda: retro_os.keypresses.login.fix_current_retro_os(root))
    start_button.config(font=("Bauhaus 93", 14))
    start_button.place(relx=0.05,rely=0.95,anchor="sw")

    next_button = tk.Button(user_interface, text="Next", command= lambda: retro_os.keypresses.login.next_from_locationselect(root))
    next_button.config(font=("Bauhaus 93", 18))
    next_button.place(relx=0.95,rely=0.95,anchor="se")

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

def laptop_name(root):
    root.config(bg="#51A69D")

    frame_width = root.winfo_screenwidth() // 1.5
    frame_height = root.winfo_screenheight() // 1.5

    user_interface = tk.Frame(root, width=frame_width, height=frame_height, background="#A0D9D3")
    user_interface.place(relx=0.5, rely=0.5, anchor="center")

    title_page = tk.Label(user_interface, text="General laptop\ninformation", background="#A0D9D3")
    title_page.config(font=("Bauhaus 93", 24))
    title_page.place(relx=0.5, rely=0.05, anchor="n")

    location_running = tk.Label(user_interface, text="Please enter a name for your laptop.", background="#A0D9D3", justify="left")
    location_running.config(font=("Calibris", 14, 'bold'))
    location_running.place(relx=0.1, rely=0.3, anchor="w")

    laptop_name_entry = tk.Entry(user_interface, background="#A0D9D3")
    laptop_name_entry.config(font=("Calibris", 12, 'italic'))
    laptop_name_entry.place(relx=0.1, rely=0.35, anchor="w")


    next_button = tk.Button(user_interface, text="Next", command= lambda: retro_os.keypresses.login.next_from_laptopname(root, laptop_name_entry))
    next_button.config(font=("Bauhaus 93", 18,))
    next_button.place(relx=0.95,rely=0.95,anchor="se")

def product_key(root):
    root.config(bg="#51A69D")

    frame_width = root.winfo_screenwidth() // 1.5
    frame_height = root.winfo_screenheight() // 1.5

    user_interface = tk.Frame(root, width=frame_width, height=frame_height, background="#A0D9D3")
    user_interface.place(relx=0.5, rely=0.5, anchor="center")

    title_page = tk.Label(user_interface, text="General laptop\ninformation", background="#A0D9D3")
    title_page.config(font=("Bauhaus 93", 24))
    title_page.place(relx=0.5, rely=0.05, anchor="n")