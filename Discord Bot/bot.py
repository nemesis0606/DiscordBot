import discord
import os
from discord.ext import commands
from discord.ext.commands.core import command

f=open('token.txt','rt')
token=f.read()
f.close()
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client=commands.Bot(command_prefix='$',intents=intents)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

for filename in os.listdir('./src'):
    if filename.endswith('.py'):
        client.load_extension(f'src.{filename[:-3]}')

@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandNotFound):
        await ctx.send('❌Oops! Invalid command. Please type $help.')
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send('❗Beeeeeep! Enter valid arguments please.')
    if isinstance(error,commands.MissingPermissions):
        await ctx.send('❌Oops! You do not have permission!')

client.run(token)