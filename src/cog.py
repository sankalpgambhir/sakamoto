# cog.py
import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
import random

sassy = [
    "Don't make me do your petty work, kid."
]

def get_rand_sassy():
    return sassy[random.randint(0, len(sassy)-1)]

class Slash(commands.Cog):
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
            thumb = "https://i.imgur.com/NusQZZR.png"
        else:
            coin = "Tails"
            thumb = "https://i.imgur.com/IkJzBOX.png"

        embed = discord.Embed(description=get_rand_sassy(), title=coin)
        embed.set_thumbnail(url=thumb)
        await ctx.send(embeds=[embed])

    @cog_ext.cog_slash(
        name="roll-dice",
        description='get a dice roll',
        guild_ids=[568123114349920256],
        options=[]
        )
    async def _rolldice(self, ctx: SlashContext, dummy=None):
        embed = discord.Embed(description=get_rand_sassy(), title=str(random.randint(1, 6)))
        embed.set_thumbnail(url="https://i.imgur.com/AYCmeEa.jpg")
        await ctx.send(embeds=[embed])

def setup(bot):
    bot.add_cog(Slash(bot))
    bot.add_cog(Gamba(bot))