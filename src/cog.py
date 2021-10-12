# cog.py
import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
import random
import pandas
import string

# mini classes
from base_sakamoto import *
import gamba
import emote
import remind
import test

def setup(bot):
    bot.add_cog(test.Test(bot))
    bot.add_cog(gamba.Gamba(bot))
    bot.add_cog(emote.Emote(bot))
    bot.add_cog(remind.Reminder(bot))