import keyboard
import pathlib
from subprocess import run
from datetime import datetime

hotkey = 'ctrl+shift+p'

script_directory = pathlib.Path(__file__).parent
temp_file_path = script_directory / 'temp'
print(f"Temp directory path: {temp_file_path}")


temp_file_path.mkdir(parents=True, exist_ok=True)

def clip():

    temp_file_name = temp_file_path / f"{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
    print(f"Saving screenshot to: {temp_file_name}")
    run(['gnome-screenshot', '-a', '--file', str(temp_file_name)], check=True)



def erase_clip():
    for file in temp_file_path.iterdir():
        if file.is_file():
            file.unlink()


keyboard.add_hotkey(hotkey, clip)
keyboard.wait('esc')
erase_clip()