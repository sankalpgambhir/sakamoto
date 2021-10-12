# test.py
# testing/random module for Sakamoto
import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
import random
import pandas
import string

from base_sakamoto import *

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(
        name="test",
        description='just a test',
        guild_ids=[568123114349920256],
        options=[
            create_option(
                name="integ",
                description="pick an integer, any integer!",
                required=True,
                option_type=4
            )
        ]
        )
    async def _test(self, ctx: SlashContext, integ:int):
        embed = discord.Embed(title=("Is your integer " + str(integ) + "?"))
        await ctx.send(content="test", embeds=[embed])

    @cog_ext.cog_slash(
        name="bofa",
        description="what's that status",
        guild_ids=[568123114349920256],
        options=[]
        )
    async def _test(self, ctx: SlashContext, dummy=''):
        await ctx.send(content="take bofa deez nuts in yo mouth")