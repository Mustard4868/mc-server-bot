import os
import discord
from discord.ext import commands

import threading
import socket
import time

from dotenv import load_dotenv
load_dotenv()

import botcommands

guild = discord.Object(id=1174703741287530538)

class minecraft_bot(commands.Bot):
    def __init__(self, *, intents: discord.Intents) -> None:
        super().__init__(command_prefix=">>", intents=intents)

    async def setup_hook(self) -> None:
        print(f"Loading extensions...")
        await self.load_extension("botcommands")
        print("Completed!")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = minecraft_bot(intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})\n...")

@bot.command()
async def synccommands(ctx):
    if ctx.author.id == 437317956159012875:
        await bot.tree.sync()
        await bot.tree.sync(guild=guild)
        bot.tree.copy_global_to(guild=guild)
        print(f"Commands synced by: {ctx.author}.")

@bot.command()
async def clearcommands(ctx):
    if ctx.author.id == 437317956159012875:
        bot.tree.clear_commands(guild=guild)
        synccommands(ctx)
        print(f"Commands cleared by: {ctx.author}.")

def start_bot():
    bot.run(os.getenv("TOKEN"))

async def change_status(connection):
    offline = '(activity=discord.Activity(name="SERVER OFFLINE",type=discord.ActivityType.watching),status=discord.Status.dnd)'
    online = '(activity=discord.Activity(name="SERVER ONLINE",type=discord.ActivityType.watching),status=discord.Status.online)'
    if connection == True: status = online
    else: status = offline
    await bot.change_presence(status)

def status_tracker(period):
    while True:
        print("Still alive?")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        change_status(sock.connect_ex(("127.0.0.1", 25565)) == 0)
        time.sleep(period)
        
bot_thread = threading.Thread(target=start_bot())
status_thread = threading.Thread(target=status_tracker(1))

if __name__ == "__main__":
    status_thread.start()
    bot_thread.start()