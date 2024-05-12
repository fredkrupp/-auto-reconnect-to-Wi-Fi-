import os
import getpass
from pathlib import Path

USER_NAME = getpass.getuser()

def add_to_startup(file_path=None):
    if not file_path:
        file_path = r"C:\Users\PC\main.py"
    
    bat_path = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    bat_file_path = os.path.join(bat_path, 'open.bat')
    
    try:
        with open(bat_file_path, 'w+') as bat_file:
            bat_file.write(f"python {file_path}")
        print("Файл успешно добавлен в автозагрузку.")
    except Exception as e:
        print("Произошла ошибка при добавлении файла в автозагрузку: ", e)

add_to_startup()
