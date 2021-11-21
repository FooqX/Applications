from colorama import init, Fore
from os import system

from pyperclip import copy

system("title Enrus Encrypt")
init(autoreset=True)

print("Enrus Encrypt\nVersion: 1.0.0\n")

output = ""
chars = {
    "q": "й",
    "w": "ц",
    "e": "у",
    "r": "к",
    "t": "е",
    "y": "н",
    "u": "г",
    "i": "ш",
    "o": "щ",
    "p": "з",
    "a": "ф",
    "s": "ы",
    "d": "в",
    "f": "а",
    "g": "п",
    "h": "р",
    "j": "о",
    "k": "л",
    "l": "д",
    "z": "я",
    "x": "ч",
    "c": "с",
    "v": "м",
    "b": "и",
    "n": "т",
    "m": "ь",
    ",": "б",
    ".": "ю",
    "1": "!",
    "2": '"',
    "3": "№",
    "4": ";",
    "5": "%",
    "6": "ж",
    "7": "?",
    "8": "*",
    "9": "(",
    "0": ")",
}

while True:
    print(f"{Fore.LIGHTMAGENTA_EX}[Options]\n{Fore.LIGHTMAGENTA_EX}(1){Fore.WHITE}: Encrypt\n{Fore.LIGHTMAGENTA_EX}(2){Fore.WHITE}: Decrypt\n")
    print(Fore.LIGHTBLUE_EX + "Select one of the options:")
    option = input("~> ")
    if option == "1":
        print(Fore.LIGHTBLUE_EX + "\nEnter your text you want to encrypt:")
        string = list(input("~> ").lower())

        print(Fore.LIGHTCYAN_EX + "\nReplacing...")
        for index, item in enumerate(string):
            for key, value in chars.items():
                if item == key:
                    string[index] = value

        print(Fore.LIGHTCYAN_EX + "Finishing...")
        output = "".join(string)
    elif option == "2":
        print(Fore.LIGHTBLUE_EX + "\nEnter your enrus encrypted string:")
        string = list(input("~> ").lower())

        print(Fore.LIGHTCYAN_EX + "\nGetting characters...")
        invertedchars = dict((y, x) for x, y in chars.items())
        print(Fore.LIGHTCYAN_EX + "Replacing...")
        for index, item in enumerate(string):
            for key, value in invertedchars.items():
                if item == key:
                    string[index] = value

        print(Fore.LIGHTCYAN_EX + "Finishing...")
        output = "".join(string)

    if len(output) >= 200:
        print(Fore.LIGHTYELLOW_EX + "[!] The output is too long to show!")
    else:
        print(Fore.LIGHTGREEN_EX + "\nOutput: " + output)

    print(Fore.LIGHTBLUE_EX + "Would you like to copy the output to clipboard? [y/n]")

    if input("~> ").lower().startswith("y"):
        copy(output)
        print("Output is successfully copied!")
    else:
        pass
