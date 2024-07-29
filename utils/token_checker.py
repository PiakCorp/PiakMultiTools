import requests
import time
import os
import pystyle
import colorama
import colored
from colored import fg
from pystyle import Write, System, Colors, Colorate, Anime
from colorama import *

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def set_title(title):
    if os.name == 'nt':
        os.system(f'title {title}')
    else:
        sys.stdout.write(f'\33]0;{title}\a')
        sys.stdout.flush()

ascci = f"""
██████╗ ██╗ █████╗ ██╗  ██╗
██╔══██╗██║██╔══██╗██║ ██╔╝
██████╔╝██║███████║█████╔╝  Token Checker
██╔═══╝ ██║██╔══██║██╔═██╗ 
██║     ██║██║  ██║██║  ██╗"""

def main():
    clear()
    print(Colorate.Horizontal(Colors.yellow_to_red, ascci))
    file_path = input(Colorate.Horizontal(Colors.yellow_to_red, "Enter the file path : "))
    
    if not file_path:
        print(Colorate.Horizontal(Colors.red_to_white, "! No file path provided."))
        return

    donetokenlist = load_tokens(file_path)
    if not donetokenlist:
        print(Colorate.Horizontal(Colors.red_to_white, "! No tokens loaded."))
        return

    check_and_display_results(donetokenlist)


def load_tokens(file_path):
    loaded_amount = 0
    donetokenlist = []
    try:
        with open(file_path, "r") as checklist:
            tokenlist = checklist.readlines()
        for token in tokenlist:
            donetokenlist.append(token.strip())
            loaded_amount += 1
        print(f"\n+ {loaded_amount} Tokens Loaded")
        input("Press ENTER to start")
        return donetokenlist
    except FileNotFoundError:
        print(Colorate.Horizontal(Colors.red_to_white, "! File not found"))
        input( "Press ENTER to exit")
        return []

def check_and_display_results(donetokenlist):
    clear()
    valid_tokens = []
    invalid_tokens = []
    invite_code = "cQ7xRv3S5x"

    for token in donetokenlist:
        while True:
            try:
                r1 = requests.post('https://discord.com/api/v9/auth/login', headers={"Authorization": token})
                if r1.status_code != 200:
                    if r1.status_code == 429:
                        print(Colorate.Horizontal(Colors.red_to_white, '! Rate limited...'))
                        time.sleep(5)
                        continue
                    elif r1.status_code == 401:
                        print(f"! Invalid: {token}")
                        invalid_tokens.append(token)
                        break
                    else:
                        print( f"! Unknown error: {token} (Status Code: {r1.status_code})")
                        invalid_tokens.append(token)
                        break
                else:
                    break
            
            except requests.exceptions.RequestException as e:
                print(f"! Request error: {e}")
                invalid_tokens.append(token)
                break
        
        if r1.status_code == 200:
            while True:
                try:
                    r = requests.get('https://discord.com/api/v9/users/@me', headers={"Authorization": token})
                    if r.status_code != 200:
                        if r.status_code == 429:
                            print('! Rate limited...')
                            time.sleep(5)
                            continue
                        elif r.status_code == 401:
                            print(f"! Verification required: {token}")
                            invalid_tokens.append(token)
                            break
                        else:
                            print(f"! Unknown error: {token} (Status Code: {r.status_code})")
                            invalid_tokens.append(token)
                            break
                    else:
                        print(f"! Valid: {token}")
                        valid_tokens.append(token)
                        break
                
                except requests.exceptions.RequestException as e:
                    print(f"! Request error: {e}")
                    invalid_tokens.append(token)
                    break

    print(f"\n\n+ Results:\n")
    
    if valid_tokens:
        print(Colorate.Horizontal(Colors.green_to_white, "Valid tokens:"))
        for token in valid_tokens:
            print(f"  + {token}")
    
    if invalid_tokens:
        print(Colorate.Horizontal(Colors.red_to_white, "\nInvalid tokens:"))
        for token in invalid_tokens:
            print(f"  ! {token}")

    input("\n\n Press ENTER to exit")
    main()

if __name__ == "__main__":
    main()
