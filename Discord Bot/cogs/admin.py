import discord
from discord.ext import commands,tasks
from discord.ext.commands.core import command
from itertools import cycle

status=cycle(['Data Science','Machine Learning','Artificial Intelligence','IoT','Cyber Security'])

class Admin(commands.Cog):

    def __init__(self,client):
        self.client=client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot taiyaar hai bhai')

    @tasks.loop(seconds=10)
    async def change_status(self):
        await self.client.change_presence(activity=discord.Game(next(status)))

    @commands.command()
    async def altstatuson(self,cxt):
        self.change_status.start()

    @commands.command()
    async def altstatusoff(self,cxt):
        self.change_status.stop()

    @commands.Cog.listener()
    async def on_member_join(self,member):
        print(f'{member} has hopped into the server!')

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        print(f'{member} has abandoned the server!')

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(title="Latency",description=f'Pong! In {round(self.client.latency*1000)} ms.',color=discord.Colour.blue())
        embed.set_footer(text="Information requested by: {}".format(ctx.author.display_name))
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def wipe(self,ctx, amount=2):
        await ctx.channel.purge(limit=amount)

    @commands.command()
    async def knockout(self,ctx, member:discord.Member,*,reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention} from the server')

    @commands.command()
    async def ban(self,ctx, member:discord.Member,*,reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention} from the server')

    @commands.command()
    async def unban(self,ctx,*,member):
        banned_users=await ctx.guild.bans()
        member_name, member_tag=member.split('#')

        for ban_entry in banned_users:
            user=ban_entry.user
    
        if(user.name,user.discriminator)==(member_name,member_tag):
            await ctx.guild.unban(user)
            await ctx.send(f'You are welcome {user.mention}!')
            return 

    @commands.command()
    async def load(self,ctx,extension):
        commands.load_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} is loaded')

    @commands.command()
    async def unload(self,ctx,extension):
        commands.unload_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} is unloaded')

    @commands.command()
    async def dev(self,ctx):
        await ctx.send('I have been developed by Abhirup (PhoeniX#8360), Debjyoti (NoobieDeb#6564) and Rohan (neMesis [SEA]#8318) for S4DS')

def setup(client):
    client.add_cog(Admin(client))