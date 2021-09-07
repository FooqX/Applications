## THIS REMOVES WINDOWS DEFENDER LEFTOVERS.
## How to use:
## Download winaero tweaker, go to tools category, find "run as trustedinstaller", and select this .py file
## if it does not work, compile this to .exe and try it again
## -- YOU MUST DISABLE WINDOWS DEFENDER SO IT'S NOT RUNNING IN BACKGROUND, YOU CAN USE WIN 10 TWEAKER TO DO IT OR OTHER TOOLS OR MANUALLY
###### ------- Fully working compiled exe file download here: 

from os import path
from shutil import rmtree
from sys import exit

from colorama import init, Fore

init()


# Path checking
def check_path(folderPath1):
    if path.isdir(folderPath1) or path.exists(folderPath1):
        return True
    else:
        return False


def delete(folderPath):
    if check_path(folderPath):
        rmtree(folderPath, ignore_errors=True)
    else:
        print(Fore.LIGHTRED_EX + "{!}" + Fore.WHITE + " Invalid path: " + folderPath)


print(Fore.LIGHTYELLOW_EX + "{!}" + Fore.WHITE + " Removing leftovers...")

delete(r"C:\Program Files\Windows Defender")
delete(r"C:\Program Files\Windows Defender Advanced Threat Protection")
delete(r"C:\Program Files (x86)\Windows Defender")
delete(r"C:\ProgramData\Microsoft\Windows Defender")
delete(r"C:\ProgramData\Microsoft\Windows Defender Advanced Threat Protection")
delete(r"C:\ProgramData\Microsoft\Windows Defender")

print(Fore.LIGHTGREEN_EX + "{!}" + Fore.WHITE + " Completed!")
input("Press any key to exit the application...")
exit()
