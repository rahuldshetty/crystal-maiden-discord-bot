import os

import discord
from dotenv import load_dotenv

from bot import reply

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

async def bot_reply(message: discord.Message):
    # Remove mentions/ids etc.
    text = message.clean_content
    text = discord.utils.remove_markdown(text)

    # Get reply from bot
    response = await reply(text)

    await message.channel.send(f"{message.author.mention} {response}")


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")

@client.event
async def on_error(event, *args, **kwargs):
    if event == 'on_message':
        print(f'Unhandled message: {args[0]}\n')
    else:
        raise

@client.event
async def on_message(message:discord.Message):
    if client.user in message.mentions:
        await bot_reply(message)
    
    print(f'Message from {message.author}: {message.content}')



if __name__ == "__main__":
    client.run(TOKEN)