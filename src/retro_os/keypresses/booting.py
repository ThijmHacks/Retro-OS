import retro_os

def bootloader_on_f12(event, root):
    retro_os.booting.fasechanger.switch_fase(root, "otheros")

def bootloader_await_5s(root):
    retro_os.booting.fasechanger.switch_fase(root, "osloader")
