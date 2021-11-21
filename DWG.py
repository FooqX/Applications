from os import system, path
from colorama import Fore, init
from random import choice, randint

system("title Discord Webhooks Generator")
init(autoreset=True)

print(Fore.RED + "\r\n             ______        ______ \r\n            |  _ \\ \\      / / ___|\r\n            | | | \\ \\ /\\ / / |  _ \r\n            | |_| |\\ V  V /| |_| |\r\n            |____/  \\_/\\_/  \\____|\r\n~===============~ DWG v1.0.4 ~===============~\r\n\r\n")

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

def random_token():
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_"
    return ''.join(choice(chars) for _ in range(randint(67, 68)))

def random_number():
    chars = "0123456789"
    return ''.join(choice(chars) for _ in range(18))

if path.exists("webhooks.txt"):
    print(Fore.LIGHTYELLOW_EX + "Cleaning up old webhooks...")
    with open("webhooks.txt", "w") as f:
        f.write("")

for i in range(webhook_count):
    print(f"Generating webhooks... | {i}/{webhook_count}", end="\r")
    with open("webhooks.txt", "a") as f:
        f.write(f"\nhttps://discord.com/api/webhooks/{random_number()}/{random_token()}")

print(Fore.LIGHTGREEN_EX + f"Successfully generated {webhook_count} webhooks!")
input(Fore.LIGHTBLACK_EX + "Press any key to terminate the program..." + Fore.WHITE)
