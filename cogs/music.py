import discord
from discord.ext import commands

class music(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command()
    async def join(self,ctx):
        if ctx.message.author.voice:
            channel = ctx.author.voice.channel
            await channel.connect()
        else :
            await ctx.send('You are not in a voice channel.')

def setup(client):
    client.add_cog(music(client))
