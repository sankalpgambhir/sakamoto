# remind.py
# reminders module for Sakamoto
import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
import random
import pandas
import string

from base_sakamoto import *

class Reminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(
        name="setreminder",
        description='set a reminder',
        guild_ids=[568123114349920256],
        options=[
            # add choices here
        ]
        )
    async def _setreminder(self, ctx: SlashContext, emote=None):
        # set a reminder
        # queue it
        # send details
        await ctx.send("UNDEF")