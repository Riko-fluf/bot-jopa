import discord

import os

from discord.ext import commands

from discord.ext.commands import Bot

Bot = commands.Bot(command_prefix= '!')

@Bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send('Дарова')

from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


client.run(token)
