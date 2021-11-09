from json import loads
from os import system
from threading import Thread
from time import sleep

from colorama import Fore, init
from requests import get, post, Response

system("title FWS")
init(autoreset = True)

print(Fore.BLUE + r'''
  ______
 / _____)
( (____  ____  _____ ____  ____  _____  ____ 
 \____ \|  _ \(____ |    \|    \| ___ |/ ___)
 _____) ) |_| / ___ | | | | | | | ____| |
(______/|  __/\_____|_|_|_|_|_|_|_____)_|
        |_|
──────────────────────────────────────────────────

Discord Webhooks Spammer v2.3.8
''')

# Needed functions
def close_app():
    input("Press any key to exit the application...")
    SystemExit(0)

print(Fore.LIGHTMAGENTA_EX + "\n──────────── SETTINGS ────────────")
print(Fore.LIGHTBLUE_EX + "\nEnter the webhook URL:")
webhook_url: str = input("~> ")

if not webhook_url.startswith("https://discord.com/api/webhooks/"):
    print(Fore.LIGHTRED_EX + "Invalid webhook url, please re-enter the actual one!")
    while True:
        try:
            webhook_url: str = input("~> ")
            if not webhook_url.startswith("https://discord.com/api/webhooks/"):
                raise Exception
        except Exception:
            print(Fore.LIGHTRED_EX + "Invalid webhook url, please re-enter the actual one!")
            webhook_url: str = input("~> ")
        else:
            break

test_code: int = get(webhook_url).status_code

if test_code == 404:
    print(Fore.LIGHTRED_EX + "[404] Specified webhook doesn't exist or was deleted!")
    close_app()
elif test_code == 401 or test_code == 403:
    print(Fore.LIGHTRED_EX + "[401/403] The Authorization header was missing or invalid. Access forbidden!")
    close_app()
elif test_code == 502:
    print(Fore.LIGHTRED_EX + "[502] There was not a gateway available to process the request!")
    close_app()
elif test_code == 405:
    print(Fore.LIGHTRED_EX + "[405] The HTTP method used is not valid for the location specified!")
    close_app()

print(Fore.LIGHTBLUE_EX + "\nEnter the webhook's username:")
username: str = input("~> ")

if len(username) < 1 or len(username) > 80:
    print(Fore.LIGHTRED_EX + "[!] Username's length is smaller than 1 or bigger than 80! Please enter it again")
    while True:
        username: str = input("~> ")
        if len(username) <= 1 or len(username) >= 80:
            print(Fore.LIGHTRED_EX + "[!] Username's length is smaller than 1 or bigger than 80! Please enter it again")
        else:
            break

print(Fore.LIGHTBLUE_EX + "\nEnter the message content:")
message: str = input("~> ")

if len(message) <= 0 or len(message) >= 2000:
    print(Fore.LIGHTRED_EX + "[!] Message content is too short or long! Please enter it again")
    while True:
        try:
            message: str = input(Fore.BLUE + "~> " + Fore.WHITE)
            if len(message) <= 0 or len(message) >= 2000:
                raise Exception
        except Exception:
            print(Fore.LIGHTRED_EX + "[!] Message content is too short or long! Please enter it again")
        else:
            break

print(Fore.LIGHTBLUE_EX + "\nHow many messages per row?")
thread_count: int = 0

while True:
    try:
        thread_count = int(input("~> "))
        if thread_count >= 11 or thread_count <= 0:
            raise Exception
    except ValueError:
        print(Fore.LIGHTRED_EX + "[!] Please enter an integer!")
    except Exception:
        print(Fore.LIGHTRED_EX + "[!] 10+ or 0 messages per row is strictly forbidden! Please enter it again!")
    else:
        break
print(Fore.LIGHTBLUE_EX + "\nEnter the cooldown after each request (float/int):")

while True:
    try:
        delay: float = float(input("~> "))
        if delay <= 0:
            print(Fore.LIGHTRED_EX + "[!] Delay is smaller than 0! Please enter it again")
    except ValueError:
        print(Fore.LIGHTRED_EX + "[!] Please enter an integer or float type number!")
    else:
        break
print(Fore.LIGHTBLUE_EX + "\nSend text-to-speech messages? [y/n]")
isTTS: bool = False
if input("~> ").lower().startswith("y"):
    isTTS: bool = True

print(Fore.LIGHTBLUE_EX + "\nConnect to a proxy? [y/n]")
proxy = ""
if input("~> ").lower().startswith("y"):
    print(Fore.LIGHTBLUE_EX + "\nPlease enter your proxy server IP (ip:port)")
    proxy = dict(http = "http://" + input("~> "))

print(Fore.LIGHTMAGENTA_EX + "\n──────────── SPAMMING ────────────")

webdata: dict = {
    "username": username,
    "content": message,
    "tts": isTTS
}

# https://discord.com/api/webhooks/904282490246688810/x3MkEp8uMr-K10zqTbLt
# -8jh5q3yUkiNHQ3cJExVLJ9E1Eg1DAa2rcrJUp_N5eaKPu4B
if proxy.__len__() >= 1:
    def do_request() -> None:
        while True:
            request: Response = post(url = webhook_url, data = webdata, proxies = proxy, allow_redirects = False)

            if request.status_code == 429:
                print("[!] Webhook is ratelimited! Bypassing...")
                wh_sleep: float = (int(loads(request.content.decode("utf-8"))["retry_after"]) / 1000) + 0.15
                sleep(wh_sleep)
                print("Webhook ratelimit bypassed successfully!")
            elif request.status_code == 404:
                print("[!] Webhook is deleted!")
                input("Press any key to exit the application...")
                SystemExit(0)
            elif request.status_code == 502:
                print("There was not a gateway available to process your request. Wait a bit and retry.")
                input("Press any key to exit the application...")
                SystemExit(0)
            sleep(delay)

    print(Fore.LIGHTBLACK_EX + "Creating threads...\n")
    print(Fore.LIGHTYELLOW_EX + "[?] Requests are sending! We'll inform you if we've got an error.")
    threads: list[Thread] = []
    for i in range(thread_count):
        t: Thread = Thread(target = do_request)
        threads.append(t)
        threads[i].start()
        threads[i].join()
else:
    def do_request():
        while True:
            request: Response = post(url = webhook_url, data = webdata, allow_redirects = False)

            if request.status_code == 429:
                print("[!] Webhook is ratelimited! Bypassing...")
                wh_sleep: float = (int(loads(request.content.decode("utf-8"))["retry_after"]) / 1000) + 0.15
                sleep(wh_sleep)
                print("Webhook ratelimit bypassed successfully!")
            elif request.status_code == 404:
                print("[!] Webhook is deleted!")
                input("Press any key to exit the application...")
                SystemExit(0)
            elif request.status_code == 502:
                print("There was not a gateway available to process your request. Wait a bit and retry.")
                input("Press any key to exit the application...")
                SystemExit(0)

            sleep(delay)

    print(Fore.LIGHTBLACK_EX + "Creating threads...\n")
    print(Fore.LIGHTYELLOW_EX + "[?] Requests are sending! We'll inform you if we've got an error.")
    threads: list[Thread] = []
    for i in range(thread_count):
        t: Thread = Thread(target = do_request)
        threads.append(t)
        threads[i].start()
        threads[i].join()

SystemExit(0)
