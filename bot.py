import discord

import os

from discord.ext import commands

from discord.ext.commands import Bot

Bot = commands.Bot(command_prefix= '**')

@Bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send('Дарова Ебаня Жопа в работе')

token = os.environ.get('token')

Bot.run(token)
