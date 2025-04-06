import tkinter as tk
from tkinter import PhotoImage
import os


import retro_os
from retro_os.functions.installing_retro import *
import retro_os.functions.users as usr

def login_screen(root):
    users = {
        "user1": "password123",
    }

    user_interface = tk.frame(root)
    user_interface.pack(padx=10, pady=10, fill="both", expand=True)

    username = "user1"
    username_label = tk.Label(user_interface, text=username, font=("Arial", 16))
    username_label.place(relx=0.5, rely=0.4, anchor="center")

    password_label = tk.Label(user_interface, text="Password:", font=("Arial", 12))
    password_label.place(relx=0.5, rely=0.5, anchor="center")

    password_entry = tk.Entry(user_interface, show="*", font=("Arial", 12))
    password_entry.place(relx=0.5, rely=0.55, anchor="center")

    def check_password():
        entered_password = password_entry.get()
        if users.get(username) == entered_password:
            print("pw correct")
        else:
            print("pw incorrect")

    login_button = tk.Button(user_interface, text="Login", command=check_password)
    login_button.place(relx=0.5, rely=0.65, anchor="center")