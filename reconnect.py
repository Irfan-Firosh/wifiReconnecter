import os
import time
import requests
import pyuac

def check_connection():
    try:
        response = requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def connect(router_name):
    try:
        os.system(f'''cmd /c "netsh wlan connect name={router_name}"''')
        print("========================Connected Succesfully=======================")
    except:
        print("Error Connecting")
        
def main():
    if check_connection() == True:
        print("Connected")
    if check_connection() == False:
        print("==========================Connection Error=========================")
        connect("YOUR WIFI SSID")
    time.sleep(60) # Adjust based on frequency of checking...

if not pyuac.isUserAdmin():
    pyuac.runAsAdmin()
else:        
    while True:
        main()
