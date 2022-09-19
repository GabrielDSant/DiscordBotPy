# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'\n{client.user} is connected to the following guild:\n'   )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Ping'):
        await message.reply(content="Pong")


client.run(TOKEN)