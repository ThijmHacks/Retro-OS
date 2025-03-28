import tkinter as tk
from retro_os.booting.fasechanger import switch_fase as sf


class RetroOS():
    def __init__(self):
        root = tk.Tk()
        root.title("RetroOS")
        root.attributes("-fullscreen", True)
        sf(root, "bootloader")
        root.mainloop()