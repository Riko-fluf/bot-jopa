import discord

from discord.ext import commands

from discord.ext.commands import Bot

import os


Bot = commands.Bot(command_prefix= '!')

@Bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send('Дарова')

token = os.environ.get('Bot Token')

Bot.run(str(token))
