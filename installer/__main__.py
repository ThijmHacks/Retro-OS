import modules.pyinstaller as pyinstaller
import modules.clean as clean

pyinstaller.make_executable("../../src/__main__.py")

clean.remove_temp('./temp')