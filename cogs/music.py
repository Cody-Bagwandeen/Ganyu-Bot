import discord
from discord.ext import commands
import youtube_dl

class music(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command()
    async def join(self,ctx):
        if ctx.message.author.voice:
            channel = ctx.message.author.voice.channel
            try:
                if ctx.guild.voice_client.is_connected():
                    await ctx.guild.voice_client.move_to(channel)
            except AttributeError:
                await channel.connect()

    ## TODO:  fix the exception where if you turn off the bot while its in a vc, then leave won't work
    @commands.command()
    async def leave(self,ctx):
        try:
            if ctx.guild.voice_client.channel == ctx.message.author.voice.channel:
                await ctx.guild.voice_client.disconnect()
            else:
                await ctx.send('You are not in the same voice channel.')
        except AttributeError:
            await ctx.send('Not currently connected to a voice channel.')

    @commands.command()
    async def state(self,ctx):
        await ctx.send(f'{ctx.message.author.voice}')

def setup(client):
    client.add_cog(music(client))
