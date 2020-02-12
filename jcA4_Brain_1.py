# Imports
import discord
import asyncio
import time
import datetime
import json
import jinko_brain
from jinko_brain import Brain
from testing import Jinko

# Globals

knownusers = {}
client = discord.Client()
channels = ("commands", "general", "erp", "lewds", "dangerous-content")
currentstorage = "storage.txt"

jinko = Jinko(Brain('ego.json', 'concepts.json', 'people.json','things.json','language.json','past_messages.json'))

# main
@client.event
async def on_message(message):
    #header = str(message)
    #print(header)
    body = str(message.content)
    source_msg_server = message.channel.guild
    author = message.author
    #print(body)#turn off printing debug
    if(message.author != client.user):# if message author is not jinko
        author = message.author.name
        cleancontent = message.clean_content.split(' ')
        server = message.channel.guild.name
        channel = message.channel.name
        timestamp = f"{message.created_at.year}, {message.created_at.month}, {message.created_at.day}, {message.created_at.hour}, {message.created_at.minute}, {message.created_at.second}"
        jinko.remember({"author":author,"content":message.clean_content,"server":server,"channel":channel,"timeUTC":timestamp})
        response = jinko.processMessage(author, cleancontent)
        if response != "":
            await message.channel.send(response)
        #save_message({"author":author,"content":cleancontent,"server":server,"channel":channel,"timeUTC":timestamp})
        #await message.channel.send(reply[0]) # send reply, will go to the same channel the message was sent

print("starting jinko-chan version 0.1")
print("hello master~")
print("i love you so muchhh~<3")
client.run(token)