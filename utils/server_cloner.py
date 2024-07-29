import os
import discord
from discord.ext import commands
import asyncio
import colored
import pystyle
from colorama import init, Fore
from colored import fg
from pystyle import Write, System, Colors, Colorate, Anime

# Initialisation de Colorama
init()

# Efface l'écran en fonction du système d'exploitation
os.system("cls" if os.name == 'nt' else 'clear')

# Demande du token et du préfixe à l'utilisateur
token = input(Colorate.Horizontal(Colors.yellow_to_red, '[>] TOKEN: '))
prefix = input(Colorate.Horizontal(Colors.yellow_to_red, '[>] PREFIX: '))

# Création du client avec le préfixe et les intentions
intents = discord.Intents.all()
client = commands.Bot(command_prefix=prefix, case_insensitive=True, intents=intents, self_bot=True)

# Supprimer la commande d'aide par défaut
client.remove_command('help')

@client.event
async def on_ready():
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
        |##:                      :###:        |        >     > ██████╗ ██╗ █████╗ ██╗  ██╗
        |#'     `..'`..'          `###'        x:      /     /  ██╔══██╗██║██╔══██╗██║ ██╔╝
         \                                   xXX|     /    ./   ██████╔╝██║███████║█████╔╝ 
          \                                xXXX'|    /   ./     ██╔═══╝ ██║██╔══██║██╔═██╗  
          /`-.                                  `.  /   /       ██║     ██║██║  ██║██║  ██╗ 
         :    `-  ...........,                   | /  .'        ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ 
         |         ``:::::::'       .            |<    `.       ███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗
         |             ```          |           x| \ `.:``.     ██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗ 
         |                         .'    /'   xXX|  `:`M`M':.   ███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝ 
         |    |                    ;    /:' xXXX'|  -'MMMMM:'   ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗
         `.  .'                   :    /:'       |-'MMMM.-'     ███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║ 
          |  |                   .'   /'        .'MMM.-'        ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝ 
          `'`'                   :  ,'          |MMM<            ██████╗██╗      ██████╗ ███╗   ██╗███████╗██████╗
            |                     `'            |tbap|          ██╔════╝██║     ██╔═══██╗████╗  ██║██╔════╝██╔══██╗
             \                                  :MM.-'          ██║     ██║     ██║   ██║██╔██╗ ██║█████╗  ██████╔╝
              \                 |              .''              ██║     ██║     ██║   ██║██║╚██╗██║██╔══╝  ██╔══██╗
               \.               `.            /                 ╚██████╗███████╗╚██████╔╝██║ ╚████║███████╗██║  ██║
                /     .:::::::.. :           /                   ╚═════╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
               |     .:::::::::::`.         /
               |   .:::------------\       /
              /   .''               >::'  /
              `',:                 :    .'
                                   `:.:' """))
    print('------')
    print('{}\n[>] {} Selfbot running... {}'.format(Fore.RESET, Fore.LIGHTYELLOW_EX, Fore.RESET))
    print('{}\n[>] {} Command:{} {}copyserver source_guild_id target_guild_id\n'.format(Fore.RESET, Fore.LIGHTYELLOW_EX, Fore.RESET, prefix))
    print('     - Logged in as ' + client.user.name)
    print('     - User ID: ' + str(client.user.id))
    print('\n------\n')

@client.command()
async def copyserver(ctx, source_guild_id: int, target_guild_id: int):
    await ctx.message.delete()

    # Trouver le serveur source
    source_guild = discord.utils.get(client.guilds, id=source_guild_id)
    if not source_guild:
        print(f"Erreur : Impossible de trouver le serveur source avec l'ID {source_guild_id}.")
        return

    # Trouver le serveur cible
    target_guild = discord.utils.get(client.guilds, id=target_guild_id)
    if not target_guild:
        print(f"Erreur : Impossible de trouver le serveur cible avec l'ID {target_guild_id}.")
        return

    # Supprimer tous les canaux existants dans le serveur cible
    for c in target_guild.channels:
        try:
            await c.delete()
        except Exception as e:
            print(f"Erreur lors de la suppression du canal {c.name} : {e}")

    # Copier les catégories et les canaux du serveur source vers le serveur cible
    for cate in source_guild.categories:
        try:
            # Créer la catégorie dans le serveur cible
            new_category = await target_guild.create_category(f"{cate.name}")

            # Copier les canaux dans la catégorie
            for chann in cate.channels:
                if isinstance(chann, discord.VoiceChannel):
                    await new_category.create_voice_channel(f"{chann.name}", bitrate=chann.bitrate, user_limit=chann.user_limit)
                elif isinstance(chann, discord.TextChannel):
                    await new_category.create_text_channel(f"{chann.name}", topic=chann.topic, nsfw=chann.nsfw)
        except Exception as e:
            print(f"Erreur lors de la copie de la catégorie {cate.name} : {e}")

    # Copier les salons hors catégories
    for chann in source_guild.channels:
        if isinstance(chann, discord.VoiceChannel):
            if chann.category is None:
                await target_guild.create_voice_channel(f"{chann.name}", bitrate=chann.bitrate, user_limit=chann.user_limit)
        elif isinstance(chann, discord.TextChannel):
            if chann.category is None:
                await target_guild.create_text_channel(f"{chann.name}", topic=chann.topic, nsfw=chann.nsfw)

    # Copier les rôles du serveur source vers le serveur cible
    for role in source_guild.roles[::-1]:
        if role.name != "@everyone":
            try:
                await target_guild.create_role(name=role.name, color=role.color, permissions=role.permissions, hoist=role.hoist, mentionable=role.mentionable)
                print(f"Rôle créé : {role.name}")
            except Exception as e:
                print(f"Erreur lors de la création du rôle {role.name} : {e}")

    # Indiquer la fin de la copie dans la console
    print("Copie du serveur terminée !")

# Lancer le bot
client.run(token, bot=False)