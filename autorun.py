import os
import getpass
from pathlib import Path


def add_to_startup(file_path=None):

    if not file_path:
        file_path = f'{Path.home()}main.py'
    

    startup_folder = Path(os.environ['APPDATA']).joinpath('Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup').as_posix()
    

    bat_file_path = f"{startup_folder}\\open2.bat"
    
    try:

        with open(bat_file_path, 'w+') as bat_file:
            bat_file.write(f"python {file_path}")
        

        print("Файл успешно добавлен в автозагрузку.")
    except Exception as e:

        print(f"Произошла ошибка при добавлении файла в автозагрузку: {e}")


add_to_startup()