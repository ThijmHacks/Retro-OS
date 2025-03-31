import tkinter as tk
from retro_os.login.initializing import *

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
        case _:
            print(f"fase {fase_name} not found.")
