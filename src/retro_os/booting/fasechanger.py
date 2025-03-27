import tkinter as tk
from retro_os.booting.bootingfase import *

def switch_fase(root, fase_name):

    for widget in root.winfo_children():
        widget.destroy()

    # Match the fase name to the corresponding function
    match fase_name:
        case "bootloader":
            bootloader(root)
        case "osloader":
            osloader(root)
        case _:
            print(f"fase {fase_name} not found.")
