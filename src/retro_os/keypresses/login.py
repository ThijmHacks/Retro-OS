import tkinter
from tkinter import filedialog
import os
import random
from cryptography.fernet import Fernet


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

def next_from_productkey(root, product_key_entry):
    pk = str(product_key_entry.get())

    if pk == str("7894-2354-1245-8173") or pk == str("7894235412458173"):
        savedir = "retroos/system/"
        file_name = "productkey.ri"
        if not os.path.exists(savedir):
            os.makedirs(savedir)
        if os.path.exists(savedir+file_name): os.remove(savedir+file_name)
        with open(savedir+file_name, "a") as file:
            file.write(str(pk))

        if pk == str("7894-2354-1245-8173") or pk == str("7894235412458173"): fci.switch_fase(root, "user_setup")


def next_from_usersetup(root):
    print("Finished the setup")