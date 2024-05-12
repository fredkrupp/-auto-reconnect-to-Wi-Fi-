import subprocess
import time
from pyrogram import Client
import platform
api_id = 
api_hash = 

app = Client("my_account", api_id=api_id, api_hash=api_hash)
app.start()
print("activate")
def myping(host):
    parameter = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", parameter, "1", host]
    response = subprocess.call(command)
    return response == 0


while True:
    if myping("store.steampowered.com")<10:
        app.send_message(1052872948,"живу")
        pass

    else:
        if 'netsh wlan disconnect':
            subprocess.call('netsh wlan connect name="TP-Link_6FBC"', shell=True)
        else:
            app.send_message(1052872948,"умер")
            print("Отключение...")
            subprocess.call('netsh wlan disconnect', shell=True)
            time.sleep(2)
            subprocess.call('netsh wlan connect name="TP-Link_6FBC"', shell=True)

    time.sleep(5)
