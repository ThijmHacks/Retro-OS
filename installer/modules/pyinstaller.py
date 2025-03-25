import PyInstaller.__main__

def make_executable(location):
    PyInstaller.__main__.run([
        location,
        '--onefile',
        '--windowed',
        '--distpath=./',
        '--clean',
        '--workpath=../installer/wp'
    ])