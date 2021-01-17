import discord
from discord.ext import commands, tasks
import os
import youtube_dl
from itertools import cycle
intents = discord.Intents.all()
client = commands.Bot(command_prefix = '.' , intents = intents)

#Hello command
@client.command()
async def hello(ctx):
    await ctx.send('Hello!') # responds hello to user

#Ping command, replies pong and bot latency in ms
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

#on_ready prints a message when the bot is ready, changes status when bot is on
@client.event
async def on_ready():
    change_status.start()
    await client.change_presence(status=discord.Status.online, activity = discord.Game('Working Overtime'))
    print('Cocogoat has arrived.')

#change status as a background task
status = cycle(['Farming Cryo Regisvine','Farming Mora','Farming Diligence Books'])

@tasks.loop(seconds = 10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

#load command
@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx,extension):
    client.load_extension(f'cogs.{extension}')

#unload command
@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')

#reload command
@client.command()
@commands.has_permissions(administrator=True)
async def reload(ctx,extension):
    client.reload_extension(f'cogs.{extension}')

#error handing for invalid commands
@client.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command.')
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please use all required arguements.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You do not have permission to use that command.')
    if isinstance(error, commands.ExtensionNotFound):
        await ctx.send('Invalid extension.')

#loop to load all extensions when the bot starts up
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}') # removes the .py when trying to load the file since its checked for

client.run('Nzk5Njk2NDE0NTEwMTUzNzg4.YAHVUg.le1Wzb6q2k_FLRRookVtKCuQMVU')
