import tkinter

import retro_os
from retro_os.login import fasechanger as fci

def initializing_start_button(root):
    fci.switch_fase(root, "language_select")