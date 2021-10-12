# sakamoto
A relatively-general-purpose Discord bot

To host the bot, add a `.env` file with the format

```
DISCORD_BOT_TOKEN=<your bot token>
ERROR_HANDLER=<id to tag for error messages>
ERROR_CHANNEL=<channel id to send error messages to>

```


For emote functionality, add your own `emoji.csv` file in `src/` with the format

```
name \t link
emote \t embed_link
.
.
.
```