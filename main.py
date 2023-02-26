import discord
import os
from dotenv import load_dotenv #needed for os to work
import requests
import json

load_dotenv() 
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event #when message is recieved
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event #when bot makes message
async def on_message(message):
    if message.author == client.user: #if the author of the message comes from the bit
        return #do nothing

    author = message.author.name
    #introduction note
    if message.content.lower().startswith('hi art bot'): #test
        await message.channel.send(f'Hello, {author}! You certainly look friend-shaped today')

client.run(os.getenv('TOKEN')) 
 
#bot features i want:
#output spn gif function
#exorcism prayer