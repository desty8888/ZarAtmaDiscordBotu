import discord
import random
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('!zarat'):
        random.randint(1, 6)
        await message.channel.send(random.randint(1, 6))

client.run("TOKEN")