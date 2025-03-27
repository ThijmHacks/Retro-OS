import tkinter as tk

import retro_os.booting.fasechanger


def bootloader(root):
    label = tk.Label(root, text="Booting...", font=("Arial", 24))
    label.pack()
    button = tk.Button(root, text="Load OS into disk", font=("Arial", 14),
                       command=lambda: retro_os.booting.fasechanger.switch_fase(root, "osloader"))
    button.pack()

def osloader(root):
    label = tk.Label(root, text="This is the OS Loader", font=("Arial", 24))
    label.pack()
