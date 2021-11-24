from os import system, path, getlogin
from colorama import Fore, init
from random import choice, randint

system("title Discord Webhooks Generator")
init(autoreset=True)

ver = 'v1.0.7 stable'
print(Fore.RED + f"\r\n             ______        ______ \r\n            |  _ \\ \\      / / ___|\r\n            | | | \\ \\ /\\ / / |  _ \r\n            | |_| |\\ V  V /| |_| |\r\n            |____/  \\_/\\_/  \\____|\r\n~===============~ DWG {ver} ~===============~\r\n\r\n")

print(Fore.CYAN + "Enter the amount of webhooks you want to generate:")
webhook_count = 0
while True:
    passed = True
    try:
        webhook_count = int(input("~> "))
    except ValueError:
        passed = False
        print(Fore.LIGHTRED_EX + "Please enter a valid number of webhooks!")
    else:
        if webhook_count == 0 or webhook_count <= 0:
            passed = False
            print(Fore.LIGHTRED_EX + "Please enter a valid number of webhooks!")

    if passed:
        break

high_performance = False
if webhook_count >= 100000:
    print(Fore.CYAN + "\nYou're trying to generate big amount of webhooks! Do you want to activate high performance mode? [y/n]")
    if input("~> ").lower() == "y":
        high_performance = True

def random_token():
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_"
    return ''.join(choice(chars) for _ in range(randint(67, 68)))

def random_number():
    chars = "0123456789"
    return ''.join(choice(chars) for _ in range(18))

if path.exists(f"C:/Users/{getlogin()}/Downloads/webhooks.txt"):
    print(Fore.LIGHTYELLOW_EX + "\nCleaning up old webhooks...")
    open(f"C:/Users/{getlogin()}/Downloads/webhooks.txt", "w").write("")
    print(Fore.LIGHTGREEN_EX + "Successfully cleaned up old webhooks!")

if high_performance:
    with open(f"C:/Users/{getlogin()}/Downloads/webhooks.txt", "a") as f:
        for i in range(webhook_count):
            f.write(f"\nhttps://discord.com/api/webhooks/{random_number()}/{random_token()}")
            print(f"Generating webhooks... | {round(i / webhook_count * 100)}%", end="\r")
else:
    with open(f"C:/Users/{getlogin()}/Downloads/webhooks.txt", "a") as f:
        for i in range(webhook_count):
            f.write(f"\nhttps://discord.com/api/webhooks/{random_number()}/{random_token()}")
            print(f"Generating webhooks... | {round(i / webhook_count * 100)}% ({i}/{webhook_count})", end="\r")

print(Fore.LIGHTGREEN_EX + f"Successfully generated {webhook_count} webhooks in your downloads folder!")
print(Fore.CYAN + "\nDo you want to open the webhooks.txt file? [y/n]")
if input("~> ").lower() == "y":
    system(f"start C:/Users/{getlogin()}/Downloads/webhooks.txt")
input(Fore.LIGHTBLACK_EX + "\nPress any key to terminate the program..." + Fore.RESET)
