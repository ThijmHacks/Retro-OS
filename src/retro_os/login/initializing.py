import tkinter as tk
from tkinter import PhotoImage
import os


import retro_os
from retro_os.functions.login import *

def initializing_start(root):
    root.config(bg="#51A69D")
    root.unbind_all('<F12>')

    frame_width = root.winfo_screenwidth() // 1.5
    frame_height = root.winfo_screenheight() // 1.5

    user_interface = tk.Frame(root, width=frame_width, height=frame_height, background="#A0D9D3")
    user_interface.place(relx=0.5, rely=0.5, anchor="center")


    start_button = tk.Button(user_interface, text="Lets go!", command= lambda: retro_os.functions.login.initializing_start_button(root))
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
    location_running.config(font=("Calibri", 11, 'bold'))
    location_running.place(relx=0.1, rely=0.3, anchor="w")

    start_button = tk.Button(user_interface, text="Fix current Retro OS\ninstallation", command= lambda: retro_os.functions.login.fix_current_retro_os(root))
    start_button.config(font=("Bauhaus 93", 14))
    start_button.place(relx=0.05,rely=0.95,anchor="sw")

    next_button = tk.Button(user_interface, text="Next", command= lambda: retro_os.functions.login.next_from_locationselect(root))
    next_button.config(font=("Bauhaus 93", 18))
    next_button.place(relx=0.95,rely=0.95,anchor="se")

def fix_current_installation(root):
    root.config(bg="#51A69D")

    frame_width = root.winfo_screenwidth() // 1.5
    frame_height = root.winfo_screenheight() // 1.5

    user_interface = tk.Frame(root, width=frame_width, height=frame_height, background="#A0D9D3")
    user_interface.place(relx=0.5, rely=0.5, anchor="center")

    back_button = tk.Button(user_interface, text="Back", command= lambda: retro_os.functions.login.initializing_start_button(root))
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
    location_running.config(font=("Calibri", 14, 'bold'))
    location_running.place(relx=0.1, rely=0.3, anchor="w")

    laptop_name_entry = tk.Entry(user_interface, background="#A0D9D3")
    laptop_name_entry.config(font=("Calibri", 12, 'italic'))
    laptop_name_entry.place(relx=0.1, rely=0.35, anchor="w")


    next_button = tk.Button(user_interface, text="Next", command= lambda: retro_os.functions.login.next_from_laptopname(user_interface, laptop_name_entry))
    next_button.config(font=("Bauhaus 93", 18,))
    next_button.place(relx=0.95,rely=0.95,anchor="se")

def product_key(root):
    root.config(bg="#51A69D")

    frame_width = root.winfo_screenwidth() // 1.5
    frame_height = root.winfo_screenheight() // 1.5

    user_interface = tk.Frame(root, width=frame_width, height=frame_height, background="#A0D9D3")
    user_interface.place(relx=0.5, rely=0.5, anchor="center")

    title_page = tk.Label(user_interface, text="Product Key", background="#A0D9D3")
    title_page.config(font=("Bauhaus 93", 24))
    title_page.place(relx=0.5, rely=0.05, anchor="n")

    product_key_text = tk.Label(user_interface, text="Enter product key below", background="#A0D9D3")
    product_key_text.config(font=("Bauhaus 93", 20))
    product_key_text.place(relx=0.5, rely=0.3, anchor="n")


    product_key_entry = tk.Entry(user_interface, background="#A0D9D3")
    product_key_entry.config(font=("Calibri", 18, 'italic'))
    product_key_entry.place(relx=0.5, rely=0.4, anchor="n")

    normal_pk = tk.Label(user_interface, text="Use this code:\n7894-2354-1245-8173", background="#A0D9D3")
    normal_pk.config(font=("Calibri", 16))
    normal_pk.place(relx=0.5, rely=0.6, anchor="n")

    next_button = tk.Button(user_interface, text="Next", command= lambda: retro_os.functions.login.next_from_productkey(root, product_key_entry))
    next_button.config(font=("Bauhaus 93", 18))
    next_button.place(relx=0.95,rely=0.95,anchor="se")

def user_setup(root):
    root.config(bg="#51A69D")

    frame_width = root.winfo_screenwidth() // 1.5
    frame_height = root.winfo_screenheight() // 1.5

    user_interface = tk.Frame(root, width=frame_width, height=frame_height, background="#A0D9D3")
    user_interface.place(relx=0.5, rely=0.5, anchor="center")

    title_page = tk.Label(user_interface, text="User Setup", background="#A0D9D3")
    title_page.config(font=("Bauhaus 93", 24))
    title_page.place(relx=0.5, rely=0.05, anchor="n")

    uname_entry = tk.Entry(user_interface, background="#A0D9D3")
    uname_entry.config(font=("Calibri", 18, 'italic'))
    uname_entry.place(relx=0.3, rely=0.3, anchor="e")

    passwd_entry = tk.Entry(user_interface, background="#A0D9D3", show="*")
    passwd_entry.config(font=("Calibri", 18, 'italic'))
    passwd_entry.place(relx=0.3, rely=0.5, anchor="e")

    next_button = tk.Button(user_interface, text="Next", command= lambda: retro_os.functions.login.next_from_usersetup(user_interface, uname_entry, passwd_entry))
    next_button.config(font=("Bauhaus 93", 18))
    next_button.place(relx=0.95,rely=0.95,anchor="se")