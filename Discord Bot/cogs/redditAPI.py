import asyncpraw
import discord
import random
from discord.ext import commands

class MemeLord(commands.Cog):

    def __init__(self,client):
        self.client=client

    @commands.command()
    async def reddit(self,ctx,search='memes'):
        reddit=asyncpraw.Reddit(client_id='uX3s7sv8hM7n0x0kJsjU9g',client_secret='IGhwX4QxXf_0eU3-Rw0hPr7tJxLicw',username='missioneducation_me',password='AbhiDeboRohan',user_agent='missioneducation_me')
        subreddit=await reddit.subreddit(search)
        top=subreddit.top(limit=50)
        sub_list=[]
        async for submission in top:
            sub_list.append(submission)
        random_sub=random.choice(sub_list)
        title=random_sub.title
        url=random_sub.url
        author=random_sub.author

        embed=discord.Embed(title=f'{title}',colour=discord.Colour.red())
        embed.set_image(url=url)
        embed.set_footer(text=f'Posted by {author}')
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(MemeLord(client)) 