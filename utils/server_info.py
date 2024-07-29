import requests
import os
import colored
import pystyle
from colored import *
from pystyle import *

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def setTitle(title):
    print(f"Setting title to: {title}")


def main():
    print("Piak Tools")

def serverlookup():
    setTitle("Server Lookup")
    clear()
    print(Colorate.Horizontal(Colors.yellow_to_red, """
quu..__
 $$$b  `---.__
  "$$b        `--.                          ___.---uuudP
   `$$b           `.__.------.__     __.---'      $$$$"              .
     "$b          -'            `-.-'            $$$"              .'|
       ".                                       d$"             _.'  |
         `.   /                              ..."             .'     |
           `./                           ..::-'            _.'       |
            /                         .:::-'            .-'         .'
           :                          ::''\          _.'            |
          .' .-.             .-.           `.      .'               |
          : /'$$|           .@"$\           `.   .'              _.-'
         .'|$u$$|          |$$,$$|           |  <            _.-'
         | `:$$:'          :$$$$$:           `.  `.       .-'
         :                  `"--'             |    `-.     |
        :##.       ==             .###.       `.      `.    `|
        |##:                      :###:        |        >     > Server Info
        |#'     `..'`..'          `###'        x:      /     /
         \                                   xXX|     /    ./
          \                                xXXX'|    /   ./
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
                                   `:.:' """))
    print(Colorate.Horizontal(Colors.green_to_white, """You can find: \n\n"""))
    print(Colorate.Horizontal(Colors.green_to_white, """Invite Link           Inviter Username      Guild Banner        Guild Splash\n"""))
    print(Colorate.Horizontal(Colors.green_to_white, """Channel Name          Inviter ID            Guild Description    Guild Features\n"""))
    print(Colorate.Horizontal(Colors.green_to_white, """Channel ID            Guild Name            Custom Invite Link\n"""))
    print(Colorate.Horizontal(Colors.green_to_white, """Expiration Date       Guild ID              Verification Level\n\n\n\n"""))
    print(Colorate.Horizontal(Colors.green_to_white, "Insert end part of link of discord server link: "))
    invitelink = input(Colorate.Horizontal(Colors.red_to_white, "Invite link: "))
    clear()
    try:
        if "discord.gg" in invitelink:
            code = invitelink.split('/')[-1]
        else:
            code = invitelink
        res = requests.get(f"https://discord.com/api/v9/invites/{code}")
        if res.status_code == 200:
            res_json = res.json()

            print(f"""\nInvitation Information:""")
            print(f""" Invite Link: {f'https://discord.gg/{res_json["code"]}'}""")
            print(f"""Channel: {res_json["channel"]["name"]} ({res_json["channel"]["id"]})""")
            print(f"""Expiration Date: {res_json["expires_at"]}\n""")

            print(f"""Inviter Information:""")
            print(f""" Username: {f'{res_json["inviter"]["username"]}#{res_json["inviter"]["discriminator"]}'}""")
            print(f"""User ID: {res_json["inviter"]["id"]}\n""")

            print(f"""Server Information:""")
            print(f"""Name: {res_json["guild"]["name"]}""")
            print(f"""Server ID: {res_json["guild"]["id"]}""")
            print(f"""Banner: {res_json["guild"]["banner"]}""")
            print(f"""Description: {res_json["guild"]["description"]}""")
            print(f"""Custom Invite Link: {res_json["guild"]["vanity_url_code"]}""")
            print(f"""Verification Level: {res_json["guild"]["verification_level"]}""")
            print(f"""Splash: {res_json["guild"]["splash"]}""")
            print(f"""Features: {res_json["guild"]["features"]}""")
        else:
            input(Colorate.Horizontal(Colors.red_to_black, """An error occurred while sending request"""))
            main()
    except Exception as e:
        print(f"Error: {e}")
        input(f"Press ENTER to exit")
        main()
    
    input(f"""Press ENTER to exit""")
    main()

serverlookup()

if __name__ == "__main__":
    main()
