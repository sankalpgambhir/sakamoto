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
        remref,
        remattach
    ){
        this.id = remid;
        this.name = remname;
        this.desc = remdesc;
        this.type = remtype;
        this.date = remdate;
        this.ref = remref;
        this.attach = remattach;
    }

};

// parameters
// how are our commands formatted?
const __prefix = '\\uwu';
const __separator = '_';
const __date_format = 'yyyy/mm/dd';

var inputs = ['help', 'setreminder'];

var __remintminutes = 0.5;
var __reminterval = __remintminutes * 60 * 1000;
const __day_interval = 24 * 60 * 60 * 1000;
const __week_interval = 7 * __day_interval;

var rems = [];

function isInt(value) {
    return !isNaN(value) && 
           parseInt(Number(value)) == value && 
           !isNaN(parseInt(value, 10));
}

function get_rem_string(rem) {
    var str = `Oi, ${rem.ref},\n**${rem.name}**\n*${rem.desc}*\n${rem.attach}`;
    return str;
}

function write_rems(){
    var back = fs.readFileSync('rems.json');
    var remstowrite = JSON.stringify(rems);
    fs.writeFileSync('remsback.json', back);
    fs.writeFileSync('rems.json', remstowrite);
    fs.writeFileSync('remsback.json', remstowrite);
}

function read_rems() {
    var back = fs.readFileSync('remsback.json');
    var fresh = fs.readFileSync('rems.json'); 
    if(back === fresh){
        console.log('Stored data OK!');
    }
    else{
        console.error('Stored data backup mismatch!')
    }
    msgstr = `Stored data & backup mismatch! Check reminders manually, ${process.env.ERROR_HANDLER}`;
    client.channels.cache.get(`${process.env.ERROR_CHANNEL}`).send(msgstr);

    rems = JSON.parse(fresh);
    for(r in rems){
        if (isString(rems[r].date)){
            rems[r].date = Date.parse(rems[r].date);
        }
    }
}

function give_syntax(command) {
    var str = "";
    switch(command){
        case 'help':
            str = str + "Well first you temme you need something\nType `" + `${__prefix}` + "`followed by one of these\n\n";

            str = str + "`help`\nI'll tell you everything you can do, since you're stupid enough to need that, apparently.\nType a command name after `help` to learn about it in detail.\n\n";
            str = str + "`setreminder name desc type date time ref attach`\nI'll remind you about st later, since you're clearly incapable of doing it yourself.\n\n";
            str = str + "`listreminder index`\nYou wanna test if I still remember what you told me to? Ofc I do you little brat, try and ask.\nUse it without the index to see what you can ask about, sigh.\n\n";
            str = str + "`remreminder index`\nI will gladly forget anything you have ever told me. Just tell me what and get it over with.\n\n";

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

        case 'listreminder':
            str = str + "`listreminder index`\nYou wanna test if I still remember what you told me to? Ofc I do you little brat, try and ask.\nUse it without the index to see what you can ask about, sigh.\n\n";
            break;

        case 'remreminder':
            str = str + "`remreminder index`\nI will gladly forget anything you have ever told me. Just tell me what and get it over with.\n\n";
            break;
    }
    return str;
}

function parse_reminder(id, args) {
    args[0].split(__separator).join(' ');
    args[1].split(__separator).join(' ');
    if(!(args[2] === 'once' || args[2] === 'daily' || args[2] === 'weekly')){
        console.log("Invalid reminder type passed!");
        return 2;
    }
    date_vec = args[3].split('/');
    if(date_vec.length != 3){
        console.log("Invalid date passed!");
        return 3;
    }
    else if(isNaN(date_vec[0]) || isNaN(date_vec[1]) || isNaN(date_vec[2])){
        console.log("Invalid date passed!");
        return 3;
    }
    if(isNaN(args[4] || args[4] < 0 || args[4] > 2359 || args[4]%100 > 59)){
        console.log("Invalid time passed!");
    }

    time_vec = [Math.floor(args[4]/100), args[4] % 100];

    date = new Date(date_vec[0], date_vec[1] - 1, date_vec[2], time_vec[0], time_vec[1]);

    rem = new Reminder(id, args[0], args[1], args[2], date, args[5], args[6]);

    rems.push(rem);

    return 0;

}

function show_reminder_by_index(remid) {
    str = "";
    item = rems[remid];
    str = str + "ID : `" + `${item.id}` + "`\n"
    str = str + "Name : `" + `${item.name}` + "`\n";
    str = str + "Description : `" + `${item.desc}` + "`\n";
    str = str + "Remind : `" + `${item.type}` + "`\n";
    str = str + "Next reminder : `" + `${(new Date(item.date)).toString()}` + "`\n";
    str = str + "Refers : `" + `${item.ref}` + "`\n";
    str = str + "Attaches : \n" + `${item.attach}` + "\n";
    return str;
}

function show_succinct_reminder_by_index(remid) {
    str = "";
    item = rems[remid];
    str = str + "Name : `" + `${item.name}` + "`\n";
    str = str + "Description : `" + `${item.desc}` + "`\n";
    str = str + "Refers : `" + `${item.ref}` + "`\n";
    return str;
}

async function schedule_send_rems() {
    setInterval(async function() {
        console.log("Checking and sending reminders...");
        curr_time = Date.now();
        console.log(`Curr time : ${curr_time.toString()}`);
        var changed = false;
        // go through reminders to see if any have passed
        for(r in rems){
            console.log(`Rem ${r} time : ${rems[r].date}`);
            if(rems[r].date < curr_time){
                console.log(`Found reminder ${r}...`);
                // send the reminder
                send_rem(rems[r]);
                changed = true;
                
                // delay this reminder to next time or delete
                if(rems[r].type === 'once'){
                    // delete
                    rems.splice(r, 1);
                    r = r - 1;
                    continue;
                 }
                else if(rems[r].type === 'daily'){
                    while(rems[r].date < curr_time){
                        rems[r].date = rems[r].date + __day_interval;
                    }
                }
                else if(rems[r].type === 'weekly'){
                    while(rems[r].date < curr_time){
                        rems[r].date = rems[r].date + __week_interval;
                    }
                }
            }
            else{
                console.log(`Ignored reminder ${r}...`);
            }
        }
        if(changed){
            write_rems();
        }

      }, __reminterval);
}

function send_rem(r) {
    msgstr = get_rem_string(r);
    client.channels.cache.get(`${process.env.REMINDERS_CHANNEL}`).send(msgstr);
    return;
}

function rem_reminder(index) {
    rems.splice(index, 1);
    return;
}

const Discord = require('discord.js');
const { strict, strictEqual } = require('assert');
const { time } = require('console');
const { isString } = require('util');
const client = new Discord.Client();


client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
  client.user.setActivity('the world fall apart', { type: 'WATCHING' });
  read_rems();
  schedule_send_rems();
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
                    if(inputs.includes(args[0])){
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
                    msgstr = 'Told you to type them properly, didn\'t I, brat?\n';
                    msgstr = msgstr + give_syntax('help');
                    msg.channel.send(msgstr);
                    break;
                }

                if(parse_reminder(msg.id, args) != 0){
                    msgstr = 'Told you to type them properly, didn\'t I, brat?\n';
                    msgstr = msgstr + give_syntax('help');
                    msg.channel.send(msgstr);
                    break;
                }

                msgstr = "I've set your reminder for you... now shoo, lemme sleep.\n\n";
                msgstr = msgstr + show_reminder_by_index(rems.length - 1);
                msg.channel.send(msgstr);
                console.log(`Length: ${rems.length}`);
                write_rems();
                break;

            case 'listreminder':
                if(args.length == 0){
                    // list all succinctly
                    msgstr = 'Temme the index if you wanna know about any of em in detail\n\n\n';
                    
                    for(var i in rems){
                        msgstr = msgstr + `${i}. ` + show_succinct_reminder_by_index(i) + "\n\n";
                    }
                    msg.channel.send(msgstr);
                    break;
                }
                if(!(isInt(args[0])) || args[0] < 0 || args[0] >= rems.length){
                    // Invalid index
                    msgstr = "Dunno what reminder you\'re talking about, kid.\nLemme sleep if you're just messing around.";
                    msg.channel.send(msgstr);
                    break;
                }

                msgstr = 'Here ya go, kid\n\n';
                msgstr = msgstr + show_reminder_by_index(args[0]);
                msg.channel.send(msgstr);
                break;

            case 'remreminder':
                if(args.length == 0){
                    msgstr = "Deleted nothing, created black hole.\n-_-\nDon't mess with me, kid. Specify what you want to delete.";
                    msg.channel.send(msgstr);
                    break;
                }
                if(!(isInt(args[0])) || args[0] < 0 || args[0] >= rems.length){
                    // Invalid index
                    msgstr = "Deleted nothing, created black hole.\n-_-\nDon't mess with me, kid. Specify a valid index.";
                    msg.channel.send(msgstr);
                    break;
                }
                msgstr = "Deleting reminder:\n\n";
                msgstr = msgstr + show_reminder_by_index(args[0]);
                msg.channel.send(msgstr);
                rem_reminder(args[0]);
                write_rems();
                break;


            default:
                console.log(`Invalid command ${_cmd}.`);
                msgstr = 'Atleast type properly, brat...\nHere, I\'ll help you out... sigh\n';
                msgstr = msgstr + give_syntax('help');
                msg.channel.send(msgstr);
        }
    }
});

client.login(process.env.DISCORD_BOT_TOKEN);