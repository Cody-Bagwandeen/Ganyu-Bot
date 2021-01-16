import discord
from discord.ext import commands
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


client.run('Nzk5Njk2NDE0NTEwMTUzNzg4.YAHVUg.dLo2Kp814dIgQEHC2ccFYY-aa44')
