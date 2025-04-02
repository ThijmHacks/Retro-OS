import tkinter as tk
from tkinter import filedialog
import os
import random
from cryptography.fernet import Fernet


import retro_os
from retro_os.login import fasechanger as fci
import retro_os.functions.users as usr

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


def next_from_usersetup(root, username, password):
    usr.create_user_file()
    uname = username.get()
    pword = password.get()

    if hasattr(next_from_usersetup, 'uname_too_small') and next_from_usersetup.uname_too_small:
        next_from_usersetup.uname_too_small.destroy()

    if hasattr(next_from_usersetup, 'passwd_too_small') and next_from_usersetup.passwd_too_small:
        next_from_usersetup.passwd_too_small.destroy()


    passwd_too_small = tk.Label(root, text="Password to small\nPlease enter more then 3 characters.",
                                background="#A0D9D3")
    passwd_too_small.config(font=("Calibri", 15, 'italic'))

    uname_too_small = tk.Label(root, text="Username to small,\nPlease enter more then 3 characters.",
                               background="#A0D9D3")
    uname_too_small.config(font=("Calibri", 15, 'italic'))

    next_from_usersetup.uname_too_small = uname_too_small
    next_from_usersetup.passwd_too_small = passwd_too_small

    uname_good = False
    pword_good = False

    if len(uname) <= 3:
        uname_too_small.place(relx=0.35, rely=0.3, anchor="w")
        uname_good = False
    elif len(uname) >= 4:
        uname_too_small.destroy()
        uname_good = True

    if len(pword) <= 3:
        passwd_too_small.place(relx=0.35, rely=0.5, anchor="w")
        pword_good = False
    elif len(pword) >= 4:
        passwd_too_small.destroy()
        pword_good = True

    if pword_good and uname_good:
        usr.create_user(uname, pword)
        fci.switch_fase(root, "checking_information")

def checking_information_check(root):
    user_list = retro_os.functions.users.load_users()
    user = random.choice(list(user_list))

    username = tk.Label(root, text=f"The username is: {user}")
    username.config(font=("Calibri", 18))
    username.place(relx=0.5,rely=3,anchor="e")