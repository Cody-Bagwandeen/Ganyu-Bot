import discord
from discord.ext import commands
import os
from random import choice
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.' , intents = intents)

#Hello command
@client.command()
async def hello(ctx):
    await ctx.send('Hello!') # responds hello to user

#Ping command, replies pong and bot latency in ms
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.event
async def on_ready():
    print('Cocogoat has arrived.')


#load command
@client.command()
async def load(ctx,extension):
    client.load_extension(f'cogs.{extension}')

#unload command
@client.command()
async def unload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')

#loop to load all extensions when the bot starts up
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('Nzk5Njk2NDE0NTEwMTUzNzg4.YAHVUg.dLo2Kp814dIgQEHC2ccFYY-aa44')
