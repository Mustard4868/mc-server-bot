import os
import discord
from discord import app_commands
from discord.ext import commands

import socket


guild = discord.Object(id=1174703741287530538)

def check_channel(channel):
    if channel == 1186325109556920432: return True

def check_connection() -> False:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if sock.connect_ex(("127.0.0.1", 25565)) == 0:
        return True


class botCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        if check_channel(ctx.channel.id):
            await ctx.send("Hello World!")

    @commands.command()
    async def status(self, ctx):
        if check_connection(): msg = "Server is online."
        else: msg = "Server is offline."
        await ctx.send(msg)

    @commands.command()
    async def start(self, ctx):
        pass

async def setup(bot):
    await bot.add_cog(botCommands(bot))