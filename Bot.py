import discord

from discord.ext import commands

from discord.ext.commands import Bot

Bot = commands.Bot(command_prefix= '!')

@Bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send('Дарова')

Bot.run('NjQ0MjI2MjQ1NzcyNzA1Nzkz.Xh0G1g.O45AvW5_Ssy-dDZnXvi0vI4dd5s')
