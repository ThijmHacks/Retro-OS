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

    savedir = "system/"
    if not os.path.exists(savedir):
        os.makedirs(savedir)
    with open("system/laptop_name.si", "a") as file:
        file.write(laptop_name + "\n")

    fci.switch_fase(root, "product_key")