import PyInstaller.__main__

def make_executable(location):
    PyInstaller.__main__.run([
        location,
        #'--windowed', (add when installer is okay to use as a windowed version)
        '--distpath=./',
        '--clean',
        '--workpath=./temp'
    ])