import os
import discord
import colorama
from discord.ext import commands
from colorama import init, Fore
import pystyle
import colored
from colored import fg
from pystyle import Write, System, Colors, Colorate, Anime

# Initialisation de Colorama
init()

# Efface l'écran en fonction du système d'exploitation
os.system("cls" if os.name == 'nt' else 'clear')

# Demande du token à l'utilisateur
token = input(Colorate.Horizontal(Colors.yellow_to_red, '[>] TOKEN: '))
message = input(Colorate.Horizontal(Colors.yellow_to_red, '[>] MESSAGE: '))

# Création du client avec les intentions nécessaires
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="+", case_insensitive=True, intents=intents, self_bot=True)

@client.event
async def on_ready():
    import pystyle
    import colored
    from colored import fg
    from pystyle import Write, System, Colors, Colorate, Anime
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
        |##:                      :###:        |        >     > Mass DM
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
    for friend in client.user.friends:
        try:
            await friend.send(message)
            print(Colorate.Horizontal(Colors.green_to_white,"Message envoyé à" + f"{friend.name}"))
        except Exception as e:
            print(Colorate.Horizontal(Colors.red_to_white,"Erreur lors de l'envoi du message à" f"{friend.name}: {e}"))

    print("Message envoyé à tous les amis!")

# Lancer le bot
client.run(token, bot=False)