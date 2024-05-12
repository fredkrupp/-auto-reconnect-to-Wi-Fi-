import subprocess
import time
def myping(host):
    command = ["ping", "-n", "1", host]  # Используйте прямые строковые литералы для команды
    return subprocess.call(command) == 0

while True:
    if myping("www.google.com")<=0:
        print("Неудача при пинге «www.google.com». Отключение...")
    # Убедитесь, что ваши команды netsh работают правильно
        cmd1 = 'netsh wlan disconnect'
        subprocess.call(cmd1, shell=True)
        time.sleep(2)  # Используйте time.sleep вместо ts
        cmd2 = 'netsh wlan connect name="TP-Link_6FBC"'
        subprocess.call(cmd2, shell=True)
    else:
        pass