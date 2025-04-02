import tkinter as tk

from retro_os.booting.fasechanger import switch_fase as sf
from retro_os.login.fasechanger import switch_fase as sfn

class RetroOS:
    def __init__(self):
        root = tk.Tk()
        root.title("RetroOS")
        root.attributes("-fullscreen", True)
        #sf(root, "bootloader")
        sfn(root, "checking_information")

        root.mainloop()