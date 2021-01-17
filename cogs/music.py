import discord
from discord.ext import commands
import youtube_dl
song_queue = []


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
        else :
            await ctx.send('You are not in a voice channel.')

    ## TODO:  fix the exception where if you turn off the bot while its in a vc, then turn it back on then leave won't work
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
    async def pause(self,ctx):
        try:
            ctx.guild.voice_client.pause()
        except AttributeError:
            await ctx.send('Not currently playing.')

    @commands.command()
    async def resume(self,ctx):
        try:
            ctx.guild.voice_client.resume()
        except AttributeError:
            await ctx.send('Not currently paused.')

    @commands.command()
    async def stop(self,ctx):
        try:
            ctx.guild.voice_client.stop()
        except AttributeError:
            await ctx.send('Not currently paused.')

    @commands.command()
    async def state(self,ctx):
        await ctx.send(f'{ctx.message.author.voice}')

    @commands.command()
    async def queue(self,ctx,url):

        global song_queue
        song_queue.append(url)
        await ctx.send(f'{url} added to queue')
        print(f'{song_queue}')

    @commands.command()
    async def show_queue(self,ctx):
        global song_queue
        await ctx.send(f'{song_queue}')

def setup(client):
    client.add_cog(music(client))
