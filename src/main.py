# Sakamoto

import os
import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from dotenv import load_dotenv, find_dotenv
import cog

# basic objects

class EnvData:
    def __init__(self):
        self._token = os.getenv("DISCORD_BOT_TOKEN")

        # error reporting 
        self._errid = int(os.getenv("ERROR_HANDLER"))    # who to report to? %Snowflake
        self._errchan = int(os.getenv("ERROR_CHANNEL"))  # where? %Snowflake

        return

if __name__ == '__main__':
    # load environment variables
    load_dotenv(find_dotenv())
    env = EnvData()

    # setup bot
    
    client = commands.Bot(command_prefix='$', intents=discord.Intents.default())
    slash = SlashCommand(client, sync_commands=True, override_type=True)

    cog.setup(client)

    # login
    client.run(env._token)