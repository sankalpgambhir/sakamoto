require('dotenv').config();

/* CODE FOR SERVER HOSTING

const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => res.send('Hello Brats!'));

app.listen(port, () => console
                    .log(`Sakamoto-san listening at http://localhost:${port}`));

*/

var fs = require('fs'); // store reminder data

class Reminder{
    constructor(
        remid,
        remname,
        remdesc,
        remtype,
        remdate,
        remtime,
        remattach
    ){
        this.id = remid;
        this.name = remname;
        this.desc = remdesc;
        this.type = remtype;
        this.date = remdate;
        this.time = remtime;
        this.ref = remref;
        this.attach = remattach;
    }

    getremstring() {
        var str = "Oi, ${this.ref},\n**${this.name}**\n*${this.desc}*\n${this.attach}";
        return str;
    }

};

// how are our commands formatted?
const __prefix = 'uwu';
const __separator = '_';
const __date_format = 'dd/mm/yyyy';

var inputs = ['setreminder'];

function give_syntax(command) {
    var str = "";
    switch(command){
        case 'help':
            str = str + "Well first you temme you need something\nType `" + `${__prefix}` + "`followed by one of these\n\n";

            str = str + "`help`\nI'll tell you everything you can do, since you're stupid enough to need that, apparently.\n\n";
            str = str + "`setreminder name desc type date time ref attach`\nI'll remind you about st later, since you're clearly incapable of doing it yourself.\n\n";

            break;
        case 'setreminder':
            str = str + "`setreminder name desc type date time ref attach`\nI'll send you a message when you've got stuff to do, just tell me about it beforehand\n";
            str = str + "`name` - I'll remember what it's basically about\n";
            str = str + "`desc` - Yeah yeah I can remember what you need to do\nMake sure you type it without spaces, separate it by " + `${__separator}` + ". Like so `" + `Sakamoto-san${__separator}needs${__separator}to${__separator}sleep.` + "`\n";
            str = str + "`type` - Temme if it's a one time deal or if I'm stuck with you for any longer. Tch\n I guess you can tell me whether to remind you `once`, `daily`, or `weekly`.\n";
            str = str + "`date` - What day you want it?\nSend it in like so `" + `${__date_format}` + "`\n";
            str = str + "`time` - What time on that day? I'm not gonna count seconds for you or anything, so just send it in 24H format like `730` or `1543`\n";
            str = str + "`ref` - Who you want reminded? Send it in like `@role` and I'll call you out later.\n";
            str = str + "`attach` - Want me to make a funny face or some shit, you brat? Tch\nA ball of yarn and you can send a GIF link in or st.\n";       
            str = str + "\nAnd you make goddamn sure you send all of them and you send all of them just fine or I'm not doing it for you.\n\n";
            break;     
    }
    return str;
}

const Discord = require('discord.js');
const { strict, strictEqual } = require('assert');
const client = new Discord.Client();


client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
  client.user.setActivity('the world fall apart', { type: 'WATCHING' });
});


client.on('message', async (msg) => {
    if (msg.author.bot) return;
    if (msg.content === 'Sakamoto!') {
    msg.reply('let me sleep, brat');
    }
    if (msg.content.startsWith(__prefix)){
        const [_cmd, ... args] = msg.content
                        .trim()
                        .substring(__prefix.length)
                        .split(/\s+/);

        // check for commands
        var msgstr = "";
        switch(_cmd){
            case 'help':
                if(args.length == 0){
                    msgstr = msgstr + 'Can\'t do anything without my help can you? Fine... I\'ll help you out\n';
                    msgstr = msgstr + give_syntax('help');
                }
                else{
                    console.log(args[0]);
                    if(args[0] in inputs){
                        msgstr = msgstr + "\* yawns \* here ya go\n\n";
                        msgstr = msgstr + give_syntax(args[0]);
                    }
                    else{
                        msgstr = msgstr + "Dunno what you need help with, kid."
                    }
                }
                msg.channel.send(msgstr);
                break;

            case 'setreminder':
                if(args.length != 7){
                    msgstr = 'Atleast type properly, brat...\nHere, I\'ll help you out... sigh\n';
                    msgstr = msgstr + give_syntax('reminder');
                    msg.channel.send(msgstr);
                    break;
                }

            default:
                console.log('Invalid command ${__cmd}.');
                msgstr = 'Atleast type properly, brat...\nHere, I\'ll help you out... sigh\n';
                msgstr = msgstr + give_syntax('help');
                msg.channel.send(msgstr);
        }
    }
});

client.login(process.env.DISCORD_BOT_TOKEN);