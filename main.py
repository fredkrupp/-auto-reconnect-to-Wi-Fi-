import subprocess
import time

def check_internet_connection():
    try:
        # Ping Google DNS (8.8.8.8) to check internet connection
        subprocess.check_call(["ping", "-c", "1", "8.8.8.8"])
        return True
    except subprocess.CalledProcessError:
        return False

def reconnect_to_wifi(ssid):
    try:
        # Disconnect from Wi-Fi
        subprocess.check_call(["netsh", "wlan", "disconnect"])
        # Connect to Wi-Fi
        subprocess.check_call(["netsh", "wlan", "connect", 'name="' + ssid + '"'])
        print("Reconnected to Wi-Fi:", ssid)
    except subprocess.CalledProcessError as e:
        print("Failed to reconnect to Wi-Fi:", e)

if __name__ == "__main__":
    # Wi-Fi network name
    wifi_ssid = "TP-Link_6FBC"

    while True:
        if not check_internet_connection():
            print("No internet connection. Reconnecting to Wi-Fi...")
            reconnect_to_wifi(wifi_ssid)

