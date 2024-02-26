import discord
from discord.ext import commands

import os

class serverShutdown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    while True:
        # Check the amount of players on the server, this should probably be done in the commandline using the /list command.
        # If the amount of players is 0, for x minutes then shut down the server.
        # This function should run conditionally, if the server is online.
        pass