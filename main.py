import subprocess
import time
print("activate")
def myping(host):
    command = ["ping", "-n", "1", host]
    return subprocess.call(command) == 0

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
