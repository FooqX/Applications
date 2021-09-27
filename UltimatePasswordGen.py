# Generates highly strong password, feel free to pull request to improve something
# Made for python 3
# Works just by saving this as .py in your computer and launching it (everything locally)
from os import system
from random import choice
from sys import exit
from typing import Callable, Union, Any

import pyparsing
from colorama import init, Fore
from pyperclip import copy

system("title Ultimate Strength Password Generator")
init(autoreset=True)


# Needed functions
def close_app():
    input("Press any key to exit the application...")
    exit()


def get_random_unicode(length: int, op: str) -> str:
    get_char: Callable[[int], str] = pyparsing.unichr

    # Range format: (from, to), (from, to) etc
    # Site: https://jrgraphix.net/r/Unicode/
    if op == "2":
        include_ranges: list[Union[tuple[int, int], Any]] = [(0x0021, 0x007E), (0x00A1, 0x00FF), (0x0100, 0x017F),
                                                             (0x0180, 0x024F), (0x0250, 0x02AF), (0x03A3, 0x03FF),
                                                             (0x0400, 0x04FF), (0x0500, 0x052F), (0x061E, 0x06FF),
                                                             (0x0900, 0x097F), (0x1400, 0x167F), (0x1681, 0x169C),
                                                             (0x16A0, 0x16F0), (0x2330, 0x23CF), (0x25A0, 0x25FF),
                                                             (0x2900, 0x297F), (0x31A0, 0x31B7), (0x3220, 0x32FF), ]
        unicodes: list[str] = [get_char(code_point) for current_range in include_ranges for code_point in
                               range(current_range[0], current_range[1] + 1)]
    else:
        include_ranges: list[Union[tuple[int, int], Any]] = [(0x0021, 0x007E), ]
        unicodes: list[str] = [get_char(code_point) for current_range in include_ranges for code_point in
                               range(current_range[0], current_range[1] + 1)]
    return ''.join(choice(unicodes) for _ in range(length))


# Start
print(Fore.LIGHTYELLOW_EX + r'''
                                     
,--. ,--. ,---.  ,------.  ,----.    
|  | |  |'   .-' |  .--. ''  .-./    
|  | |  |`.  `-. |  '--' ||  | .---. 
'  '-'  '.-'    ||  | --' '  '--'  | 
 `-----' `-----' `--'      `------'  
                                     
──────────────────────────────────────
''')
print("Felierix's Ultimate Strength Password Generator\nVersion: 1.0.0\n")
print(f"{Fore.MAGENTA}Password Strength Options{Fore.WHITE}\n"
      "[1]: Basic Latin Letters (ex abc123!@#$)\n"
      f"[2]: Ultimate Strength Combination\n\n{Fore.LIGHTCYAN_EX}Enter your option")

option = input("~> ")
print(Fore.LIGHTCYAN_EX + "\nEnter your length of the password")
pass_length = 20
try:
    pass_length = int(input("~> "))
except ValueError as err:
    print(Fore.LIGHTRED_EX + "Error: ", err)

if option == "1":
    print(Fore.LIGHTYELLOW_EX + "Generating password... (Please wait)")
    password = get_random_unicode(pass_length, " ")
    print(Fore.LIGHTYELLOW_EX + "Copying to clipboard...")
    copy(password)
    print(Fore.LIGHTGREEN_EX + "The operation completed successfully!")
elif option == "2":
    print(Fore.LIGHTYELLOW_EX + "Generating password... (Please wait)")
    password = get_random_unicode(pass_length, "2")
    print(Fore.LIGHTYELLOW_EX + "Copying to clipboard...")
    copy(password)
    print(Fore.LIGHTGREEN_EX + "The operation completed successfully!")
close_app()
