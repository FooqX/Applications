# powerful cleaner, save this locally as .py file and launch it and enjoy
# feel free to pull a request to improve it
from pyperclip import copy
from glob import glob
from os import path, system, getlogin, mkdir, remove
from shutil import rmtree, move
from sys import exit
from time import sleep

from colorama import init, Fore, Style
from pyautogui import keyUp, keyDown, press

system("title Cleaner X")
init(autoreset=True)

print(Fore.LIGHTCYAN_EX + r'''
   ___ _                        __  __
  / __| |___ __ _ _ _  ___ _ _  \ \/ /
 | (__| / -_) _` | ' \/ -_) '_|  >  < 
  \___|_\___\__,_|_||_\___|_|   /_/\_\
────────────────────────────────────────                          
''')

ver = "1.2.1"
currentUser = getlogin()

# Information
print("Cleaner X\nMade by Felierix\n"
      f"Version: {Fore.LIGHTRED_EX}"f'{ver}{Style.RESET_ALL}\n')
print(Fore.LIGHTBLUE_EX + "──────── Traces ────────")
print("[t1]: User temporary files\n"
      "[t2]: Temporary files\n"
      "[t3]: Windows temporary files\n"
      "[t4]: Prefetch files [!]\n"
      "[t5]: Windows update files [!]\n"
      "[t6]: Clear clipboard\n")
print(Fore.LIGHTBLUE_EX + "──────── System ────────")
print("[s1]: Refresh icon cache\n"
      "[s2]: Scan/check disk for errors\n"
      "[s3]: Check system files\n"
      "[s4]: Change IP Address (DHCP server required)\n"
      "[s5]: Restart this computer\n"
      "[s6]: -Feature-removed-\n"
      "[s7]: Boot into advanced startup mode\n"
      "[s8]: Enable 'Ultimate performance' plan\n"
      "[s9]: Refresh taskbar/explorer\n"
      "[s10]: Fix/Restart windows update processes\n"
      "[s11]: Refresh desktop icons\n")
print(Fore.LIGHTBLUE_EX + "──────── Internet Explorer ────────")
print("[ie1]: Temporary files\n")
if path.exists(f"C:\\Users\\{currentUser}\\AppData\\Roaming\\discord"):
    print(Fore.LIGHTMAGENTA_EX + "──────── Discord ────────")
    print("[d1]: Cache files [!]\n"
          "[d2]: Delete BetterDiscord leftover files [!]\n")

# --- Required functions
getPath = {
    "Temp": r"C:\Temp", "WindowsTemp": r"C:\Windows\Temp", "UserTemp": rf"C:\Users\{currentUser}\AppData\Local\Temp",
    "Prefetch": r"C:\Windows\Prefetch", "UpdateFiles": r"C:\Windows\SoftwareDistribution\Download",
    "DiscordCache": rf"C:\Users\{currentUser}\AppData\Roaming\discord\Cache",
    "Downloads": rf"C:\Users\{currentUser}\Downloads", "LocalDesktop": rf"C:\Users\{currentUser}\Desktop",
    "IETemp": rf"C:\Users\{currentUser}\AppData\Local\Microsoft\Windows\INetCache\IE"
}


# -- Delete file/folder
def delete(filepath11321):
    if check_path(filepath11321):
        rmtree(filepath11321, ignore_errors=True)
    else:
        pass


# -- Close application
def close_app():
    input("Press any key to exit the application...")
    exit()


# -- Path checking
def check_path(filepath):
    if path.exists(filepath) or path.isdir(filepath):
        return True
    else:
        return False


# -- Kill process
def kill_process(name):
    try:
        system(f"taskkill /F /IM {name} /T")
    except ProcessLookupError:
        print(Fore.LIGHTRED_EX + "Error encountered while trying to find process")
    except ChildProcessError:
        print(Fore.LIGHTRED_EX + "Error encountered while trying to kill child processes")


# --- Cleaning
print(Fore.LIGHTCYAN_EX + "Press enter to exit")
user_option = " "

while 1:
    user_option = input(">>>> ").lower()

    if user_option == "clean":
        print(Fore.LIGHTYELLOW_EX + "Cleaning junk files...")
        delete(getPath["WindowsTemp"])
        delete(getPath["UserTemp"])
        delete(getPath["Temp"])
        print(Fore.LIGHTYELLOW_EX + "Cleaning clipboard...")
        copy('')
        print(Fore.LIGHTGREEN_EX + "Sucessfully completed!")
    elif user_option == "t4":
        print(Fore.LIGHTYELLOW_EX + "Cleaning prefetch files...")
        delete(getPath["Prefetch"])
        print(Fore.LIGHTGREEN_EX + "Files are successfully cleaned!")
    elif user_option == "t5":
        print(Fore.LIGHTYELLOW_EX + "Attempting to kill windows update process..")
        system("net stop wuauserv")
        sleep(0.2)
        print(Fore.LIGHTYELLOW_EX + "Cleaning files...")
        delete(getPath["UpdateFiles"])
        print(Fore.LIGHTYELLOW_EX + "Starting windows update process..")
        system("net start wuauserv")
        print(Fore.LIGHTGREEN_EX + "Sucessfully completed!")
    elif user_option == "ie1":
        print(Fore.LIGHTYELLOW_EX + "Attempting to kill internet explorer..")
        kill_process("iexplore.exe")
        sleep(0.1)
        delete(getPath["IETemp"])
        print(Fore.LIGHTGREEN_EX + "Sucessfully completed!")
    elif user_option == "d1":
        print(Fore.LIGHTYELLOW_EX + "Preparing...")
        if check_path(rf"C:\Users\{currentUser}\AppData\Roaming\discord"):
            pass
        else:
            print(Fore.LIGHTRED_EX + "Discord isn't detected/installed!")
            close_app()

        print(Fore.LIGHTCYAN_EX + "Are you sure to continue? It will kill discord process [y/n]")
        discord_input = input(">>>> ")
        if discord_input.lower() == "y":
            print(Fore.LIGHTYELLOW_EX + "Killing process...")
            kill_process("Discord.exe")
            print(Fore.LIGHTYELLOW_EX + "Cleaning cache files...")
            delete(getPath["DiscordCache"])
            print(Fore.LIGHTGREEN_EX + "Sucessfully completed!")
        else:
            close_app()
    elif user_option == "d2":
        print(Fore.LIGHTYELLOW_EX + "Preparing...")
        print(Fore.LIGHTYELLOW_EX + "Killing discord...")
        kill_process("Discord.exe")
        print(Fore.LIGHTYELLOW_EX + "Cleaning BD leftovers...")
        isBackup = input("Backup plugins/themes?: ").lower()
        if isBackup.startswith("y"):
            print(Fore.LIGHTYELLOW_EX + f"Creating backup folder in {getPath['Downloads']}...")
            mkdir(getPath["Downloads"] + "\\BETTER_DISCORD_BACKUP")
            print(Fore.LIGHTYELLOW_EX + "Making a backup of all plugins and themes files/settings...")
            move(rf"C:\Users\{currentUser}\AppData\Roaming\BetterDiscord\plugins",
                 getPath["Downloads"] + "\\BETTER_DISCORD_BACKUP")
            move(rf"C:\Users\{currentUser}\AppData\Roaming\BetterDiscord\themes",
                 getPath["Downloads"] + "\\BETTER_DISCORD_BACKUP")
            print(Fore.LIGHTYELLOW_EX + "Verifying files...")
            if check_path(getPath["Downloads"] + "\\BETTER_DISCORD_BACKUP"):
                print(Fore.LIGHTGREEN_EX + "Successfully made a backup in Downloads!")
            else:
                print(Fore.LIGHTRED_EX + "Something went wrong.. Couldn't verify files.")
            print(Fore.LIGHTYELLOW_EX + "Deleting leftovers...")
            delete(rf"C:\Users\{currentUser}\AppData\Roaming\BetterDiscord")
            delete(rf"C:\Users\{currentUser}\AppData\Roaming\BetterDiscord Installer")
            print(Fore.LIGHTGREEN_EX + "Sucessfully completed!")
    elif user_option == "s1":
        print(Fore.LIGHTYELLOW_EX + "Preparing...")
        kill_process("explorer.exe")
        print(Fore.LIGHTYELLOW_EX + "Removing icon cache files...")
        for iconcache in glob(rf"C:\Users\{currentUser}\AppData\Local\Microsoft\WindowsExplorer*"):
            remove(iconcache)
        print(Fore.LIGHTYELLOW_EX + "Finishing up...")
        system("explorer")
        print(Fore.LIGHTGREEN_EX + "Sucessfully completed!"
                                   " Would you want to restart your pc to apply changes? [y/n]")
        restartPC = input(">>>> ").lower()
        if restartPC.startswith("y"):
            system("shutdown /r")
        else:
            print(Fore.LIGHTCYAN_EX + "Okay! But note that you need to restart it now anyways.. :)")
    elif user_option == "s2":
        print(Fore.LIGHTCYAN_EX + "What disk you want to scan? ( Example: C: )?")
        disk = input(">>>> ")
        if disk.endswith(":"):
            print(Fore.LIGHTYELLOW_EX + "Processing...")
            system(f'cmd /k "chkdsk {disk} /F /R"')
            print(Fore.LIGHTCYAN_EX + "Sucessfully completed!")
    elif user_option == "s3":
        print(Fore.LIGHTYELLOW_EX + "Processing...")
        system('cmd /k "sfc /scannow"')
    elif user_option == "s4":
        print(Fore.LIGHTCYAN_EX + "[i] Close every application that can use"
                                  " your internet and press any key to continue")
        input()
        print(Fore.LIGHTYELLOW_EX + "Processing... [1/2]")
        system("ipconfig /release")
        print(Fore.LIGHTYELLOW_EX + "Processing... [2/2]")
        system("ipconfig /renew")
        print(Fore.LIGHTGREEN_EX + "Sucessfully completed!")
    elif user_option == "s5":
        print(Fore.LIGHTYELLOW_EX + "Processing...")
        sleep(3)
        system("shutdown /r")
    elif user_option == "s6":
        print(Fore.LIGHTRED_EX + "[Warning]: This feature is not available")
    elif user_option == "s7":
        print(Fore.LIGHTCYAN_EX + "Save any unsaved work and press any key to continue...")
        input()
        print(Fore.LIGHTYELLOW_EX + "Shutting down and booting into advanced startup...")
        system("shutdown /r /o")
    elif user_option == "s8":
        print(Fore.LIGHTYELLOW_EX + "Processing...")
        system("powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61")
        print(Fore.LIGHTGREEN_EX + "Sucessfully completed!")
        system("powercfg.cpl")
    elif user_option == "s9":
        print(Fore.LIGHTYELLOW_EX + "Refreshing...")
        kill_process("explorer.exe")
        sleep(0.2)
        system("explorer")
        print(Fore.LIGHTGREEN_EX + "Sucessfully completed!")
    elif user_option == "s10":
        print(Fore.LIGHTYELLOW_EX + "Stopping windows update processes...")
        system("net stop wuauserv")
        sleep(0.1)
        system("net stop bits")
        sleep(0.1)
        system("net stop cryptsvc")
        sleep(0.1)
        print(Fore.LIGHTYELLOW_EX + "Finishing up...")
        system("Ren %systemroot%SoftwareDistributionSoftwareDistribution.bak")
        sleep(0.1)
        system("Ren %systemroot%system32catroot2catroot2.bak")
        sleep(0.1)
        print(Fore.LIGHTYELLOW_EX + "Starting windows update processes...")
        system("net start wuauserv")
        sleep(0.1)
        system("net start bits")
        sleep(0.1)
        system("net start cryptsvc")
        print(Fore.LIGHTGREEN_EX + "Sucessfully completed!")
    elif user_option == "s11":
        print(Fore.LIGHTYELLOW_EX + "Refreshing...")
        keyDown("super")
        press("d")
        keyUp("super")
        sleep(0.01)
        press("f5")
        print(Fore.LIGHTGREEN_EX + "Successfully completed!")
    elif len(user_option) <= 0:
        break
    else:
        print(Fore.LIGHTRED_EX + "You selected invalid option! Read the instructions in README.txt")

# Exit
close_app()
