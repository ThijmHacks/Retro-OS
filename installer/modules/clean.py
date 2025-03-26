import shutil
import os
import stat


def remove_temp(location):
    shutil.rmtree(location)

def remove_files(folder, spec):
    shutil.rmtree(folder)
    os.remove(spec)