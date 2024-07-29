import os 
import subprocess
import json
import ctypes
try:
    import pystyle
    import emailrep
    import itertools
    import phonenumbers
    import colored
    import colorama
    import discord
except ModuleNotFoundError:
    os.system("pip install pystyle")
    os.system("pip install emailrep")
    os.system("pip install itertools")
    os.system("pip install phonenumbers")
    os.system("pip install colored")
    os.system("pip install colorama")
    os.system("pip install discord")
    os.system("pip install discord.py-self")
from colored import fg
from pystyle import Write, System, Colors, Colorate, Anime
from colorama import *
os.system("cls")

def execute_script(script_name):
    script_path = os.path.join('utils', script_name)
    subprocess.run(['python', script_path], check=True)

ascci_art = f"""
                    ╒═══════════════•═══════════════╕                                 quu..__
                    |          Discord Tools        |                                  $$$b  `---.__
                    | 01 > Token Nuker              |                                   "$$b        `--.                          ___.---uuudP
                    | 02 > Token MassDm             |╒═══════════════•═══════════════╕   `$$b           `.__.------.__     __.---'      $$$$"   
                    | 03 > Token Checker            || Dev: Piak                     |     "$b          -'            `-.-'            $$$"              .'|        
                    | 04 > Nitro Tools              || Version: 1                    |       ".                                       d$"             _.'  |          
                    | 05 > Server Nuker             || Discord: discord.gg/fa7Z4Hd8gF|         `.   /                              ..."             .'     |    
                    | 06 > Server Information       |╘═══════════════•═══════════════╛           `./                           ..::-'            _.'       |
                    | 07 > Server Cloner            |                                             /                         .:::-'            .-'         .'
                    | 08 > Auto Login               |                                            :                          ::''\          _.'            |    
                    | 09 > Clear DM                 |                                           .' .-.             .-.           `.      .'               |
                    | 10 > Email Info               |                                           : /'$$|           .@"$\           `.   .'              _.-'
                    ╘══════════════•════════════════╛                                          .'|$u$$|          |$$,$$|           |  <            _.-'
                                                                                               | `:$$:'          :$$$$$:           `.  `.       .-'
                                              ██████╗ ██╗ █████╗ ██╗  ██╗                      :                  `"--'             |    `-.     |
                                              ██╔══██╗██║██╔══██╗██║ ██╔╝                     :##.       ==             .###.       `.      `.    `|
                                              ██████╔╝██║███████║█████╔╝                      |##:                      :###:        |        >     >
                                              ██╔═══╝ ██║██╔══██║██╔═██╗                      |#'     `..'`..'          `###'        x:      /     /        
                                              ██║     ██║██║  ██║██║  ██╗                      \                                   xXX|     /    ./
                                              ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   add : _piak_        \                                xXXX'|    /   ./
                                                                                                /`-.                                  `.  /   /
                                                                                               :    `-  ...........,                   | /  .'
                                                                                               |         ``:::::::'       .            |<    `.
                                                                                               |             ```          |           x| \ `.:``.
                                                                                               |                         .'    /'   xXX|  `:`M`M':.
                                                                                               |    |                    ;    /:' xXXX'|  -'MMMMM:'
                                                                                              `.  .'                   :    /:'       |-'MMMM.-'
                                                                                                |  |                   .'   /'        .'MMM.-'
                                                                                                `'`'                   :  ,'          |MMM<
                                                                                                  |                     `'            |tbap|
                                                                                                   \                                  :MM.-'
                                                                                                    \                 |              .''
                                                                                                     \.               `.            /
                                                                                                      /     .:::::::.. :           /
                                                                                                     |     .:::::::::::`.         /
                                                                                                     |   .:::------------\       /
                                                                                                    /   .''               >::'  /
                                                                                                    `',:                 :    .'
                                                                                                                         `:.:' """
def setTitle(title):
    username = os.getlogin()
    new_title = f"{title} - {username}"
    os.system(f"title {new_title}")

def setFullScreen():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd != 0:
        SW_MAXIMIZE = 3
        ctypes.windll.user32.ShowWindow(hwnd, SW_MAXIMIZE)

def main():
    setFullScreen()
    setTitle("PiakTool V1")
    print(Colorate.Horizontal(Colors.yellow_to_red, ascci_art))
    while True:
        choice = input(Colorate.Horizontal(Colors.yellow_to_red, "Choose an option:  "))
        
        if choice == '01':
            execute_script('account_nuker.py')
        elif choice == '1':
            execute_script('account_nuker.py')
        elif choice == '02':
            execute_script('token_massdm.py')
        elif choice == '2':
            execute_script('token_massdm.py')
        elif choice == '03':
            execute_script('token_checker.py')
        elif choice == '3':
            execute_script('token_checker.py')
        elif choice == '04':
            execute_script('nitro_gen.py')
        elif choice == '4':
            execute_script('nitro_gen.py')
        elif choice == '05':
            execute_script('server_nuker.py')
        elif choice == '5':
            execute_script('server_nuker.py')
        elif choice == '06':
            execute_script('server_info.py')
        elif choice == '6':
            execute_script('server_info.py')
        elif choice == '07':
            execute_script('server_cloner.py')
        elif choice == '7':
            execute_script('server_cloner.py')
        elif choice == '08':
            execute_script('auto_login.py')
        elif choice == '8':
            execute_script('auto_login.py')
        elif choice == '09':
            execute_script('clear_dm.py')
        elif choice == '9':
            execute_script('clear_dm.py')
        elif choice == '10':
            execute_script('email_info.py')
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()