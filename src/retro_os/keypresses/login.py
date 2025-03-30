import tkinter

import retro_os
from retro_os.login import fasechanger as fci

def initializing_start_button(root):
    fci.switch_fase(root, "language_select")

def fix_current_retro_os(root):
    fci.switch_fase(root, "fix_current_installation")