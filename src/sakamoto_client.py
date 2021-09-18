# # sakamoto-client.py

# import os
# import discord
# from dotenv import load_dotenv, find_dotenv

# # basic objects
# load_dotenv(find_dotenv()) # load environment variables

# class EnvData:
#     def __init__(self):
#         self._token = os.getenv("DISCORD_BOT_TOKEN")
#         self._remchan = os.getenv("REMINDERS_CHANNEL") # channel to send reminders. %Snowflake

#         # error reporting 
#         self._errid = os.getenv("ERROR_HANDLER")    # who to report to? %Snowflake
#         self._errchan = os.getenv("ERROR_CHANNEL")  # where? %Snowflake

#         # other params
#         self._prefix = os.getenv("CMD_PREFIX")      # prefix for commands to look for
#         self._remwait = os.getenv("REM_WAIT_TIME")   # time in minutes to send reminders
#         self._separator = os.getenv("CMD_SEPARATOR")
#         self._date_format = os.getenv("DATE_FORMAT")

#         return

# env = EnvData() # all the environment parameters

# class Sakamoto:


#     def __init__(self):
#         self.syntax = {
#             "help" : "",
#             "setreminder" : "",
#             "listreminder" : "",
#             "remreminder" : "",
#         }

#         self.construct_syntax()
#         return

#     def invalid_input(self):
#         retstr = "Atleast type properly, brat...\nHere, I\'ll help you out... sigh\n"
#         retstr += self.give_syntax()
#         return retstr

#     def give_syntax(self, input = None):
#         if(input is None or input not in self.syntax):
#             return self.syntax['help']
#         else:
#             return self.syntax[input]
    
#     def construct_syntax(self):
#         # generic help
#         self.syntax["help"] = self.syntax["help"] + "Well first you temme you need something\nType `{}` followed by one of these\n\n".format(env._prefix)
#         self.syntax["help"] = self.syntax["help"] + "`help`\nI'll tell you everything you can do, since you're stupid enough to need that, apparently.\nType a command name after `help` to learn about it in detail.\n\n"
#         self.syntax["help"] = self.syntax["help"] + "`setreminder name desc type date time ref attach`\nI'll remind you about st later, since you're clearly incapable of doing it yourself.\n\n"
#         self.syntax["help"] = self.syntax["help"] + "`listreminder index`\nYou wanna test if I still remember what you told me to? Ofc I do you little brat, try and ask.\nUse it without the index to see what you can ask about, sigh.\n\n"
#         self.syntax["help"] = self.syntax["help"] + "`remreminder index`\nI will gladly forget anything you have ever told me. Just tell me what and get it over with.\n\n"

#         # set reminder
#         self.syntax["setreminder"] = self.syntax["setreminder"] + "`setreminder name desc type date time ref attach`\nI'll send you a message when you've got stuff to do, just tell me about it beforehand\n"
#         self.syntax["setreminder"] = self.syntax["setreminder"] + "`name` - I'll remember what it's basically about\n"
#         self.syntax["setreminder"] = self.syntax["setreminder"] + "`desc` - Yeah yeah I can remember what you need to do\nMake sure you type it without spaces, separate it by `{}`. Like so `Sakamoto-san{}needs{}to{}sleep.`\n".format(env._separator)
#         self.syntax["setreminder"] = self.syntax["setreminder"] + "`type` - Temme if it's a one time deal or if I'm stuck with you for any longer. Tch\n I guess you can tell me whether to remind you `once`, `daily`, or `weekly`.\n"
#         self.syntax["setreminder"] = self.syntax["setreminder"] + "`date` - What day you want it?\nSend it in like so `{}`\n".format(env._date_format)
#         self.syntax["setreminder"] = self.syntax["setreminder"] + "`time` - What time on that day? I'm not gonna count seconds for you or anything, so just send it in 24H format like `730` or `1543`\n"
#         self.syntax["setreminder"] = self.syntax["setreminder"] + "`ref` - Who you want reminded? Send it in like `@role` and I'll call you out later.\n"
#         self.syntax["setreminder"] = self.syntax["setreminder"] + "`attach` - Want me to make a funny face or some shit, you brat? Tch\nA ball of yarn and you can send a GIF link in or st.\n"       
#         self.syntax["setreminder"] = self.syntax["setreminder"] + "\nAnd you make goddamn sure you send all of them and you send all of them just fine or I'm not doing it for you.\n\n"
        
#         # list reminder
#         self.syntax["listreminder"] = self.syntax["listreminder"] + "`listreminder index`\nYou wanna test if I still remember what you told me to? Ofc I do you little brat, try and ask.\nUse it without the index to see what you can ask about, sigh.\n\n"

#         # remove reminder
#         self.syntax["remreminder"] = self.syntax["remreminder"] + "`remreminder index`\nI will gladly forget anything you have ever told me. Just tell me what and get it over with.\n\n"


# class sakamoto_client(discord.Client):

#     # basic interface
#     def __init__(self):
#         self.run(env._token)    # call internal login with env vars
#         self.sakamoto = Sakamoto()
        
#     # redefining event handlers

#     async def on_ready(self):
#         # instructions on login
#         game = discord.Game("with lives")
#         await client.change_presence(status=discord.Status.idle, activity=game)

#         read_rems() # read data, pass error if fail
#         schedule_rem_send() # check every so often and send out reminders

#         return

#     async def on_message(self, message):
#         if message.author == client.user:
#             return
#         if(not message.content.startswith(env._prefix)):
#             return
        
#         msgstr = ""

#         # parse message into args list

#         # check command and call relevant function
#         if(args[0] not in self.sakamoto.syntax):
#             # invalid command
#             msgstr += self.sakamoto.invalid_input()
#             message.channel.send(msgstr)
    
#     # custom error notifier
#     async def send_error(self, error_string):
#         error_string += ' {0}'.format(env._errid)
#         self.get_channel(env._errchan).send(error_string)
#         return