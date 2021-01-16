import discord
from discord.ext import commands
from random import choice
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.' , intents = intents)

@client.event
async def on_ready():
    print('Cocogoat has arrived')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def hello(ctx):
    await ctx.send('Hello!')

@client.command()
async def quote(ctx):
    responses = ['It\'s so nice to de-stress.',
                 'If you lie on the grass, you can feel the heartbeat of the world.',
                 'Oh, the sun\'s out. When did that happen?',
                 'Ah, I love the smell of Glaze Lilies.',
                 'Ugh... I need a nap. If there aren\'t any urgent matters, I\'ll excuse myself...',
                 'May Rex Lapis watch over you. May your dreams be peaceful and sweet.',
                 'With authority over a thousand comes responsibility to a thousand.',
                 'My hobby... I would say my job. What?',
                 '"Drink only spring water, eat only whole grains," that\'s my motto.',
                 'Only when days be darker than the darkest night, may a qilin be compelled to fight.',
                 'Next on the agenda...',
                 'Glaze over!']
    await ctx.send(f'{choice(responses)}')


client.run('Nzk5Njk2NDE0NTEwMTUzNzg4.YAHVUg.dLo2Kp814dIgQEHC2ccFYY-aa44')
