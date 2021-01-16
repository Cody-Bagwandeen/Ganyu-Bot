import discord
from discord.ext import commands
from random import choice
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.' , intents = intents)

@client.event
async def on_ready():
    print('Cocogoat has arrived') # prints this messsage when the bot is ready

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.') # prints that the user has joined the server

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.') # prints that the user hsa left the server

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms') # replies to user command with pong and displays the bots latency in ms

@client.command()
async def hello(ctx):
    await ctx.send('Hello!') # responds hello to user

@client.command()
async def quote(ctx):
    responses = ['It\'s so nice to de-stress.',  #quotes taken from wiki
                 'If you lie on the grass, you can feel the heartbeat of the world.',
                 'Oh, the sun\'s out. When did that happen?',
                 'Ah, I love the smell of Glaze Lilies.',
                 'Ah, the air is just right.',
                 'Um so, yeah, uh, I was, uh... I was wondering what your opinion is on my work so far? Would you say I\'m... more of a Common Chest or more of a Luxurious Chest? I—It\'s fine. I—I can, uh... I can take it.',
                 'Ugh... I need a nap. If there aren\'t any urgent matters, I\'ll excuse myself...',
                 'May Rex Lapis watch over you. May your dreams be peaceful and sweet.',
                 'With authority over a thousand comes responsibility to a thousand.',
                 'My hobby... I would say my job. What?',
                 'Thank you for always making time to chat with me.',
                 'Power? ...Now there\'s a key performance indicator I haven\'t needed in a long time.',
                 'Could we maybe... find a peaceful resolution instead...? Never mind, doesn\'t matter...',
                 'I suppose this is the new way of life, then. I\'m not going to complain. I\'ll try to embrace it.',
                 '"Drink only spring water, eat only whole grains," that\'s my motto.',
                 'Only when days be darker than the darkest night, may a qilin be compelled to fight.',
                 'Next on the agenda...',
                 'Glaze over!']
    await ctx.send(f'{choice(responses)}') # choices a random quote and sends that quote as a message

@client.command()
async def clear(ctx,amount = 5): #default amount of lines to clear set to 5
    if amount == 0 :
        return
    await ctx.channel.purge(limit = (amount + 1)) # clears the amount of lines specified and removes the line with the command

@client.command()
async def kick(ctx, member : discord.Member, *, reason = None): # member is the user that is being kicked, reads in the member as a Member object
    await member.kick(reason=reason)

client.run('Nzk5Njk2NDE0NTEwMTUzNzg4.YAHVUg.dLo2Kp814dIgQEHC2ccFYY-aa44')
