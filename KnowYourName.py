import platform
import shutil
import PySimpleGUI as sg
import subprocess
import re


layout = [
    [sg.Text(f"Имя вашего устройства: {platform.node()}")],
    [sg.Text(f"Версия Windows: {platform.win32_ver()[0]}")],
    [sg.Text(f"Java: {('Не установлена', 'Установлена')[shutil.which('java') is not None]}")],
    [sg.Text(f"Версия Java: {subprocess.check_output(['java', '-version'], stderr=subprocess.STDOUT)}")]
]

window = sg.Window("Информация о ПК", layout=layout)

while True:
    event, values = window.read()

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED:
        break