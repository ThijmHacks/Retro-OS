import retro_os
import retro_os.login.fasechanger as fc


def bootloader_on_f12(event, root):
    retro_os.booting.fasechanger.switch_fase(root, "otheros")

def bootloader_await_5s(root):
    retro_os.booting.fasechanger.switch_fase(root, "osloader")

def osloader_await_10s(root):
    fc.switch_fase(root, "initializing_start")
