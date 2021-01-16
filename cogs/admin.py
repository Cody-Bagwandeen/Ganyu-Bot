import discord
from discord.ext import commands

class Admin(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    #clears messages
    async def clear(self,ctx,amount : int):
        if amount == 0:
            return
        await ctx.channel.purge(limit = (amount + 1))

    @commands.command()
    #kicks users from server
    async def kick(self,ctx, member : discord.Member,*, reason = None):
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention}')

    @commands.command()
    #bans users from server
    async def ban(self,ctx, member : discord.Member,*, reason = None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')

    @commands.command()
    #unbans banned users from server
    async def unban(self,ctx,*,member):
        banned_users = await ctx.guild.bans() #banned users of the server
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if(user.name, user.discriminator) == (member_name,member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

    @commands.Cog.listener()
    #prints message when user joins server
    async def on_member_join(self,member):
        print(f'{member} has joined the server')

    @commands.Cog.listener()
    #pints message when user leaves server
    async def on_member_remove(self,member):
        print(f'{member} has left the server.')


def setup(client):
    client.add_cog(Admin(client))
