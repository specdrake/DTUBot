import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import os
from os import system
import random
import csv

client = commands.Bot(command_prefix = ".")
client.remove_command('help')
TOKEN = open('tok', 'r').read().strip()
GUILD = "A1"
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=".help"))
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
            f'{client.user} is connected to :\n'
            f'{guild.name}(id: {guild.id})'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ['yes', 'no', 'maybe', 'probably', 'probably not']
    await ctx.send(f'Question : {question}\nAnswer: {random.choice(responses)}')    


@client.command()
@has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
     await ctx.channel.purge(limit=amount)


@client.command()
async def news(ctx, x=5):
    os.system("python3 scr.py")
    nt = open('tlnk.txt', 'r').read()
    if not nt:
        me = await client.get_user_info('MY_SNOWFLAKE_ID')
        await client.send_message(me, "Something went wrong with .news")
        await ctx.send("Sorry! Something went wrong")
    lt = nt.split('\n\n')
    for i in range(x):
        await ctx.send(f'{i+1}) {lt[i]}')

@client.command()
async def mnews(ctx, x=5):
    os.system("python3 scr.py")
    nm = open('mlnk.txt', 'r').read()
    if not nm:
        me = await client.get_user_info('MY_SNOWFLAKE_ID')
        await client.send_message(me, "Something went wrong with .news")
        await ctx.send("Sorry! Something went wrong")
    lm = nm.split('\n\n')
    for i in range(x):
        await ctx.send(f'{i+1}) {lm[i]}')

@client.command() 
async def search(ctx, *, name):
    reader = csv.reader(open('data.csv', 'r'), delimiter=',')
    cnt = 0
    tmr = False
    for row in reader:
        if any(row):
            if name.lower() in row[3].lower():
                cnt += 1
                if cnt == 1:
                    await ctx.send(f'Here you go:\n')
                await ctx.send(f'{cnt}) {row[1]}\t{row[2]}\t{row[3]}\t{row[4]}')
                if cnt == 10:
                    tmr = True
                    break

    await ctx.send(f'Found {cnt} results!!!')
    if tmr == True:
        await ctx.send("Uploading more in a file")
        ofile = open('tmr.txt', 'w')
        for row in reader:
            if any(row):
                if name.lower() in row[3].lower():
                    cnt += 1
                    ofile.write(f'{cnt}) {row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\n')
        ofile.close()
        await ctx.send(file=discord.File('tmr.txt'))
        
   
@client.command()
async def map(ctx):
    await ctx.send("Map coming up right away!")
    await ctx.send(file=discord.File('map.jpg'))


@client.command()
@has_permissions(administrator=True) 
async def kick(ctx, member : discord.Member, *, reason=None):
     await member.kick(reason=reason)
     await ctx.send("Kicked")

@client.command()
async def wiki(ctx, *, query):
    query = query.strip().replace(' ', '%20')
    await ctx.send(f'https://en.wikipedia.org/wiki/{query}')

@client.command()
async def ub(ctx, *, query):
    query = query.strip().replace(' ', '%20')
    await ctx.send(f'https://www.urbandictionary.com/define.php?term={query}')
@client.command()
async def gs(ctx, *, query):
    query = query.strip().replace(' ', '%20')
    await ctx.send(f'https://www.google.com/search?q={query}')
@client.command()
async def help(ctx, *, com=None):
    if com == None:
        await ctx.send(f'``Hello`` {ctx.message.author.mention}!! Here are some things you can do: **Usage: .<command>**')
        await ctx.send("```8ball : play magic 8ball\n"
                        +"clear : clear messages\n"
                        +"help : shows this help message\n"
                        +"kick : kick a user\n"
                        +"map : shows DTU map\n"
                        +"news: latest updates from http://www.dtu.ac.in\n"
                        +"mnews: more updates\n"
                        +"ping : pong!\n"
                        +"search : searches a user in 2k19 database\n"
                        +"wiki <query> : shows wikipedia page for query\n"
                        +"ub <query> : shows urban dictionary page for query\n"
                        +"gs <query> : shows google search link for query\n"
                        +"Type .help <command> for more usage info```")
    else:
        if com.lower() == '8ball':
            await ctx.send("``.8ball <Question> : play magic 8 ball``")
        if com.lower() == 'clear':
            await ctx.send("``.clear <x> : clears x no. of messages.(Default:5)``")
        if com.lower() == 'help':
            await ctx.send("``.help | .help <command> : displays general help or help for a specific command``")
        if com.lower() == 'kick':
            await ctx.send("``.kick <mention user> : kicks the specified user(Can only be used by Administrator)``")
        if com.lower() == 'map':
            await ctx.send("``.map : shows DTU map``")
        if com.lower() == 'news':
            await ctx.send("``.news <x> : shows x recent updates from http://www.dtu.ac.in (Default:5)``") 
        if com.lower() == 'mnews':
            await ctx.send("``.mnews <x> : shows more updates (see: .help news)``")
        if com.lower() == 'ping':
            await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
        if com.lower() == 'wiki':
            await ctx.send("``.wiki <query> : shows wikipedia page for query``")
        if com.lower() == 'ub':
            await ctx.send("``ub <query> : shows urban dictionary page for query``")
        if com.lower() == 'gs':
            await ctx.send("``gs <query> : shows google search link for query``")
        if com.lower() == 'search':
            await ctx.send("``.search <name> : searches for a student in the 2k19 BTech batch``")

client.run(TOKEN)
