import tkinter
from tkinter import filedialog
import os
import random

import retro_os
from retro_os.login import fasechanger as fci

def initializing_start_button(root):
    fci.switch_fase(root, "location_select")

def fix_current_retro_os(root):
    fci.switch_fase(root, "fix_current_installation")

def next_from_locationselect(root):
    fci.switch_fase(root, "laptop_name")

def next_from_laptopname(root, laptop_entry):
    laptop_name = laptop_entry.get()

    if laptop_name == "": laptop_name = "retro-os" + str(random.randint(100,999))

    savedir = "retroos/system/"
    file_name = "laptop_name.ri"
    if not os.path.exists(savedir):
        os.makedirs(savedir)
    if os.path.exists(savedir+file_name): os.remove(savedir+file_name)
    with open(savedir+file_name, "a") as file:
        file.write(laptop_name)

    fci.switch_fase(root, "product_key")