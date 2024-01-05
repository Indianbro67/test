import importlib
import subprocess
import platform
try:
    importlib.import_module('telegram')
except ImportError:
    print("The 'telegram' module is not installed. Installing it...")
    subprocess.check_call(['pip', 'install', 'python-telegram-bot==13.8'])
try:
    importlib.import_module('requests')
except ImportError:
    print("The 'requests' module is not installed. Installing it...")
    subprocess.check_call(['pip', 'install', 'requests'])

try:
    importlib.import_module('colorama')
except ImportError:
    print("The 'colorama' module is not installed. Installing it...")
    subprocess.check_call(['pip', 'install', 'colorama'])

try:
    importlib.import_module('urllib3')
except ImportError:
    print("The 'urllib3' module is not installed. Installing it...")
    subprocess.check_call(['pip', 'install', 'urllib3'])
try:
    importlib.import_module('telethon')
except ImportError:
    print("The 'telethon' module is not installed. Installing it...")
    subprocess.check_call(['pip', 'install', 'telethon==1.24.0'])
if platform.system() == "Windows":
    subprocess.call('cls', shell=True)
else:
    subprocess.call('clear', shell=True)
import os
import sys 
import random
import sys
import uuid
import time
import requests
import urllib3
from datetime import datetime, timedelta
from telethon.sync import TelegramClient
from colorama import Fore
from colorama import init
from telethon.errors import FloodWaitError, ChatAdminRequiredError
from telegram import Bot
from telegram.error import TelegramError
from telegram.utils.request import Request

init(autoreset=True)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN
ORANGE = Fore.LIGHTYELLOW_EX
RED = Fore.RED
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
BLUE = Fore.BLUE

MAGENTA = "\033[95m"
RED = "\033[91m"
ORANGE = "\033[93m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"
            
current_platform = platform.system()

banner_frames = [
    f"{MAGENTA}\n",
    f"{MAGENTA}++++++---++++++++++++---++++++++++++---++++++++++++---++++++++++++---++++++{RESET}",
    f"{RED}+ ____  _        _    ____ _  __  ____  _______     _____ _     _       +{RESET}",
    f"{RED}-| __ )| |      / \  / ___| |/ / |  _ \\| ____\\ \   / /_ _| |   | |      -{RESET}",
    f"{ORANGE}+|  _ \| |     / _ \| |   | ' /  | | | |  _|  \ \ / / | || |   | |      +{RESET}",
    f"{YELLOW}-| |_) | |___ / ___ \ |___| . \  | |_| | |___  \ V /  | || |___| |___   -{RESET}",
    f"{GREEN}+|____/|_____/_/   \_\____|_|\_\ |____/|_____|  \_/  |___|_____|_____|  +{RESET}",
    f"{GREEN}-                                                                       -{RESET}",
    f"{MAGENTA}++++++---++++++++++++---++++++++++++---++++++++++++---++++++++++++---++++++{RESET}",
    f"{MAGENTA}",
    f"{BLUE} TELEGRAM PURCHASE LICENSE KEY FROM {RED}= https://t.me/Black_Devil_Admin {RESET}",
    f"{BLUE} TELEGRAM SUPPORT GROUP {RED}= https://t.me/adult_girls_chatting_groupp {RESET}",
    f"{MAGENTA}",
    f"{MAGENTA}++++++---++++++++++++---++++++++++++---++++++++++++---++++++++++++---++++++{RESET}",
]

termux_banner = f"{CYAN}\n"
termux_banner += f"{MAGENTA}╔════════════════════════════════╗{RESET}\n"
termux_banner += f"{RED}║                                ║{RESET}\n"
termux_banner += f"{RED}║   {GREEN}(っ◔◡◔)っ ♥ BLACK DEVIL ♥    {CYAN}║{RESET}\n"
termux_banner += f"{ORANGE}║                                ║{RESET}\n"
termux_banner += f"{GREEN}╚════════════════════════════════╝{RESET}\n"

def get_mac_address():
    mac = ''.join(['{:08b}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(5, -1, -1)])
    return mac

def clear_terminal():
    os.system("cls" if current_platform == "Windows" else "clear")

def display_banner_animation(frames, num_iterations, frame_delay):
    for _ in range(num_iterations):
        clear_terminal()
        for frame in frames:
            print(frame)
            time.sleep(frame_delay)

num_iterations = 1
frame_delay = 0.1 

if current_platform == "Windows":
    display_banner_animation(banner_frames, num_iterations, frame_delay)

else:
    print(termux_banner)
    print(MAGENTA + "++++++---++++++++++++---++++++++++++---++++++++++++---++++++++")
    print(MAGENTA + "")
    print(BLUE + " TELEGRAM PURCHASE LICENSE KEY FROM " + RED + "= https://t.me/Black_Devil_Admin ")
    print(MAGENTA + "")
    print(MAGENTA + "++++++---++++++++++++---++++++++++++---++++++++++++---++++++++")
    
def connection_animation():
    frames = ["/", "\\"]
    for _ in range(2): 
        for frame in frames:
            print(Fore.RED + f"Connecting To Server {frame}", end="\r")
            time.sleep(0.2)

connection_animation()


api_id = "24701272"
api_hash = "ff7c593337a217fc473c30135cf21b3d"
session_name = "black_devil_admin"

def send_message(client, group_entity, message):
    try:
        client.send_message(group_entity, message)
        print(Fore.YELLOW + f"Message sent:")
    except Exception as e:
        print(Fore.RED + f"Failed to send message:")

def select_group(client):
    dialogs = client.get_dialogs()

    print("Available groups:")
    for i, dialog in enumerate(dialogs, start=1):
        print(f"{i}. {dialog.name}")

    selected_index = -1
    while selected_index < 0 or selected_index >= len(dialogs):
        try:
            selected_index = int(input("Select a group by entering its number: ")) - 1
            if 0 <= selected_index < len(dialogs):
                return dialogs[selected_index]
            else:
                print("Invalid selection. Please select a valid group.")
        except ValueError:
            print("Invalid input. Please enter a number.")

mac_address = get_mac_address()

def verify_license(mac_address):
    url = "https://pastebin.com/raw/sSGGmkeu"

    try:
        response = requests.get(url, verify=False)

        if response.status_code == 200:
            keys = response.text.splitlines()

            if mac_address in keys:
                print("License key is valid. Your software is licensed.")
                return True
            else:
                return False
        else:
            print("Failed to retrieve the list of Activation keys from the server.")
            return False
    except requests.exceptions.RequestException as e:
        print("An error occurred while making the request: please check your internet")
        return False

def select_group(client):
    dialogs = client.get_dialogs()

    print("Available groups:")
    group_count = 0

    for dialog in dialogs:
        if dialog.is_group:
            group_count += 1
            print(f"{group_count}. {dialog.name}, ID: {dialog.id}")

    if group_count == 0:
        print("No groups found.")
        return None, None

    selected_index = -1
    while selected_index < 0 or selected_index >= group_count:
        try:
            selected_index = int(input("Select a group by entering its number: ")) - 1
            if 0 <= selected_index < group_count:
                selected_group = [d for d in dialogs if d.is_group][selected_index]
                return selected_group.id, selected_group.name
            else:
                print("Invalid selection. Please select a valid group.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    mac_address = get_mac_address()

    if mac_address and verify_license(mac_address):
        print(f"Your Software is activated: {Fore.GREEN}{mac_address}{RESET}")
        client = TelegramClient(session_name, api_id, api_hash)

        with client:
            try:
                selected_group_id, selected_group_name = select_group(client)

                with open("messages.txt", "r", encoding="utf-8") as file:
                    messages = [line.strip() for line in file.readlines()]

                while True:
                    for message in messages:
                        try:
                            send_message(client, selected_group_id, message)

                            sleep = random.uniform(9.0, 30.0)
                            sleep_time = sleep * 2.1

                            next_message_time = datetime.now() + timedelta(seconds=sleep_time)
                            print(f"Next message will be sent at: {Fore.YELLOW}{next_message_time}{RESET}")

                            time.sleep(sleep_time)

                        except (FloodWaitError, ChatAdminRequiredError) as e:
                            print(f"{Fore.RED}Cannot send message: {str(e)}")
                            print(f"{Fore.RED}You are blocked by the group owner. Exiting...")
                            sys.exit(1)

            except KeyboardInterrupt:
                print(f"{Fore.BLUE}Bot stopped by user (KeyboardInterrupt)")
                sys.exit(0)
            except Exception as e:
                print(f"{Fore.RED}Bot encountered an error: {str(e)}")
    else:
        print(f"{Fore.RED}Activation Code: {mac_address}")
        print(f"{Fore.GREEN}Send This Activation Code TO @Black_Devil_Admin For Activation: ")

if __name__ == "__main__":
    main()
