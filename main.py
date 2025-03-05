import cv2
import numpy as np
from pathlib import Path
from subprocess import run
from datetime import datetime
from os import remove
from shutil import rmtree
from sys import exit

script_directory = Path(__file__).parent
temp_file_path = script_directory / 'temp'
file_name = f"{datetime.now().strftime('%Y%m%d%H%M%S')}"
temp_file_name = temp_file_path / f"{file_name}t.png"
final_file_name = temp_file_path / f"{file_name}.png"
temp_file_path.mkdir(parents=True, exist_ok=True)


def remove_background():
    # Removes background from image
    # https://stackoverflow.com/questions/63001988/how-to-remove-background-of-images-in-python

    img = cv2.imread(temp_file_name)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mask = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)[1]
    mask = 255 - mask
    kernel = np.ones((3,3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.GaussianBlur(mask, (0,0), sigmaX=2, sigmaY=2, borderType = cv2.BORDER_DEFAULT)
    mask = (2*(mask.astype(np.float32))-255.0).clip(0,255).astype(np.uint8)
    result = img.copy()
    result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)
    result[:, :, 3] = mask
    cv2.imwrite(final_file_name, result)
    remove(temp_file_name)


def clipboard_copy(image_path):
    with open(image_path, 'rb') as image_file:
        run(['wl-copy', '--type', 'image/png'], input=image_file.read())


print('''
        ----- Clip Cut -----
         [1] New Screenshot
         [2] Clear Folder
        --------------------
        ''')

try:
    opt = int(input('Enter Option: '))
except ValueError:
    print('Goodbye!')
    exit()

if opt == 1:
    run(['gnome-screenshot', '-a', '-f', str(temp_file_name)])
    remove_background()
    clipboard_copy(final_file_name)
    print(f'{final_file_name} copied to clipboard.')
elif opt == 2:
    rmtree(temp_file_path)
    print(f'{temp_file_path} deleted sucessfully.')
else:
    print('Goodbye!')
    exit()