import discord
import os
import kaggle
import requests
from discord.ext import commands

class KaggleAPI(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.command()
    async def list(self,ctx):
        await ctx.send(os.system('kaggle competitions list'))


def setup(client):
    client.add_cog(KaggleAPI(client)) 
