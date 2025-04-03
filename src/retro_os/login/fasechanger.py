import tkinter as tk
from itertools import product

from retro_os.login.initializing import *
from retro_os.login.login import *

def switch_fase(root, fase_name):

    for widget in root.winfo_children():
        widget.destroy()

    # Match the fase name to the corresponding function
    match fase_name:
        case "initializing_start":
            initializing_start(root)
        case "location_select":
            location_select(root)
        case "fix_current_installation":
            fix_current_installation(root)
        case "laptop_name":
            laptop_name(root)
        case "product_key":
            product_key(root)
        case "user_setup":
            user_setup(root)
        case "checking_information":
            checking_information(root)
        case "login_screen":
            login_screen(root)
        case _:
            print(f"fase {fase_name} not found.")
