import retro_os

def on_f2(event, root):
    print("F2 has been pressed")
    retro_os.booting.fasechanger.switch_fase(root, "otheros")

def on_space(event, root):
    print("Space has been pressed")
    retro_os.booting.fasechanger.switch_fase(root, "osloader")