import subprocess
import time
import platform
print("activate")

def myping(host):
    parameter = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", parameter, "1", host]
    response = subprocess.call(command)
    return response == 0
while True:
    if myping("www.google.com")<=7:
        cmd1 = 'netsh wlan disconnect'
        cmd2 = 'netsh wlan connect name="TP-Link_6FBC"'
        if 'netsh wlan disconnect':
            subprocess.call(cmd2, shell=True)
        else:
            print("Отключение...")
            subprocess.call(cmd1, shell=True)
            time.sleep(2)
            subprocess.call(cmd2, shell=True)
    else:
        pass
    time.sleep(5)
