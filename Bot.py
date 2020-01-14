import discord

import os

from discord.ext import commands

from discord.ext.commands import Bot

Bot = commands.Bot(command_prefix= '!')

@Bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send('Дарова')

token = os.environ.get('BOT_TOKEN')

bot.run(str(token))
