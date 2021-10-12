# gamba.py
# probabilistic methods module for Sakamoto
import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
import random
import pandas
import string

from base_sakamoto import *

class Gamba(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(
        name="flip-coin",
        description='get a coin flip',
        guild_ids=[568123114349920256],
        options=[]
        )
    async def _flipcoin(self, ctx: SlashContext, dummy=None):
        if random.randint(0,1) == 0:
            coin = "Heads"
            thumb = image['heads']
        else:
            coin = "Tails"
            thumb = image['tails']

        embed = discord.Embed(description=get_rand_sassy(), title=coin)
        embed.set_thumbnail(url=thumb)
        await ctx.send(embeds=[embed])

    @cog_ext.cog_slash(
        name="roll-dice",
        description='get an n-dice roll',
        guild_ids=[568123114349920256],
        options=[
            create_option(
                name="dsize",
                description="dice size (default: 6)",
                required=False,
                option_type=4
            )
            ]
        )
    async def _rolldice(self, ctx: SlashContext, dsize=6):
        if dsize < 1:
            dsize = 6
        embed = discord.Embed(description=('on dice with {} face(s).\n{}'.format(dsize, get_rand_sassy())), title=str(random.randint(1, dsize)))
        embed.set_thumbnail(url=image['lick'])
        await ctx.send(embeds=[embed])