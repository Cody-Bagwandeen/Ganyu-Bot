import discord
from discord.ext import commands
from random import choice

class quotes(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command()
    async def quote(self,ctx):
        responses = ['It\'s so nice to de-stress.',  #quotes taken from wiki
                     'If you lie on the grass, you can feel the heartbeat of the world.',
                     'Oh, the sun\'s out. When did that happen?',
                     'Ah, I love the smell of Glaze Lilies.',
                     'Ah, the air is just right.',
                     'Um so, yeah, uh, I was, uh... I was wondering what your opinion is on my work so far? Would you say I\'m... more of a Common Chest or more of a Luxurious Chest? I—It\'s fine. I—I can, uh... I can take it.',
                     'Ugh... I need a nap. If there aren\'t any urgent matters, I\'ll excuse myself...',
                     'May Rex Lapis watch over you. May your dreams be peaceful and sweet.',
                     'With authority over a thousand comes responsibility to a thousand.',
                     'My hobby... I would say my job. What?',
                     'Thank you for always making time to chat with me.',
                     'Power? ...Now there\'s a key performance indicator I haven\'t needed in a long time.',
                     'Could we maybe... find a peaceful resolution instead...? Never mind, doesn\'t matter...',
                     'I suppose this is the new way of life, then. I\'m not going to complain. I\'ll try to embrace it.',
                     '"Drink only spring water, eat only whole grains," that\'s my motto.',
                     'Only when days be darker than the darkest night, may a qilin be compelled to fight.',
                     'Next on the agenda...',
                     'Glaze over!']
        await ctx.send(f'{choice(responses)}') # choices a random quote and sends that quote as a message

def setup(client):
    client.add_cog(quotes(client))
