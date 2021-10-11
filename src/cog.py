# cog.py
import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
import random
import pandas
import string

sassy = [
    "Don't make me do your petty work, kid."
]

def get_rand_sassy():
    return sassy[random.randint(0, len(sassy)-1)]

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
        embed.set_thumbnail(url="https://i.imgur.com/AYCmeEa.jpg")
        await ctx.send(embeds=[embed])

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
        name="emote",
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
    async def _emote(self, ctx: SlashContext, which=""):
        # send emote

        emotelink = next((x[1] for x in emotelist if x[0] == which.lower()), None)

        if emotelink is not None:
            await ctx.send(emotelink)
        else:
            pass

    @cog_ext.cog_slash(
        name="autoemote",
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
    async def _autoemote(self, ctx: SlashContext, dummy = '', *args, **kwargs):
        # send emote

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

def setup(bot):
    bot.add_cog(Test(bot))
    bot.add_cog(Gamba(bot))
    bot.add_cog(Emote(bot))
    bot.add_cog(Reminder(bot))