import discord
from discord.ext import commands

class Admin(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command()
    async def clear(self,ctx,amount = 5):
        if amount == 0:
            return
        await ctx.channel.purge(limit = (amount +1))

def setup(client):
    client.add_cog(Admin(client))
