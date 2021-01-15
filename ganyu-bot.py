import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Cocogoat has arrived')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(".hello"):
        await message.channel.send("Hello!")

client.run('Nzk5Njk2NDE0NTEwMTUzNzg4.YAHVUg.dLo2Kp814dIgQEHC2ccFYY-aa44')
