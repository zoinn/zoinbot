import discord
from discord.ext import commands
from discord.ext.commands import bot
from youtubesearchpython import VideosSearch
import os
import requests
import json

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$play'):
        newSearch = message.content
        videosSearch = VideosSearch(newSearch.replace('$play', ''), limit=1)

        await message.channel.send('Searching...')
        print(videosSearch.result())
        #await message.channel.send(videosSearch.result())
        await bot.join_voice_channel(channel)

#client.run(os.environ.get('TOKEN'))
client.run('')