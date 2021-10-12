# emote.py
# emote/gif module for Sakamoto
import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
import random
import pandas
import string

from base_sakamoto import *

# read emotes and construct list
emotelist = pandas.read_csv('emoji.csv', sep='\t').values
emotelist = [[x[0].lower(), x[1]] for x in emotelist]
emotelist.sort(key=lambda x: x[0])
# construct choices for autofill
choice = {}
for l in string.ascii_lowercase[:-1]:
    choice[l] = create_option(
                name=l,
                description=l,
                required=True,
                option_type=3,
                choices=[t[0] for t in emotelist if t[0][0] == l]
            )
    choice[l].update({'value' : 'TEST'})

class Emote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(
        name="manualemote",
        description='send custom emotes',
        guild_ids=[568123114349920256],
        options=[
            create_option(
                name="which",
                description="which emote to send",
                required=True,
                option_type=3
            )
        ]
        )
    async def _manualemote(self, ctx: SlashContext, which=""):
        # send emote

        emotelink = None

        emotelink = next((x[1] for x in emotelist if x[0] == which.lower()), None)

        if emotelink is not None:
            await ctx.send(emotelink)
        else:
            pass

    @cog_ext.cog_slash(
        name="emote",
        description='send custom emotes',
        guild_ids=[568123114349920256],
        options=[
            # create a group for each letter
            create_option(
                name=l,
                description=l,
                required=False,
                option_type=3,
                choices=[t[0] for t in emotelist if t[0][0] == l]
            )
            for l in string.ascii_lowercase[:-1]
        ]
        )
    async def _emote(self, ctx: SlashContext, dummy = '', *args, **kwargs):
        # send emote

        emotelink = None

        for l in kwargs.values():
            emotelink = next((x[1] for x in emotelist if x[0] == l.lower()), None)
            if emotelink is not None:
                break

        if emotelink is not None:
            await ctx.send(emotelink)
        else:
            pass
    
    @cog_ext.cog_slash(
        name="listemote",
        description='list all custom emotes',
        guild_ids=[568123114349920256],
        options=[]
        )
    async def _listemote(self, ctx: SlashContext, dummy = None):
        # send emote

        res = discord.Embed(title='Emote list', description=get_rand_sassy())

        s = [e[0] for e in emotelist]

        res.add_field(name = 'Emotes', value = ' '.join(s))

        await ctx.send(embeds=[res])