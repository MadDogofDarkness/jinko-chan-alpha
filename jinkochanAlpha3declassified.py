from importlib import reload
import discord
import asyncio
import time
import json
from random import randint
from jinkospeech import phraseresponses
from jinkospeech import intentions
from jinkospeech import simple_phrases

class Memory():
    def __init__(self, text, author, server, channel, timendate):
        self.text = text
        self.author = author
        self.server = server
        self.channel = channel
        self.timendate = timendate

    def jsonify(self):
        data = "{" + str(self.text) + "," + str(self.author) + "," + str(self.server) + "," + str(self.channel) + "," + str(self.timendate) + "}"
        return data

token = '' # your discord app token
#id = # your app ID if needed
knownusers = {} # not implemented at this time
client = discord.Client()
chen = False
count = 5
channels = ("commands", "general", "erp", "lewds", "dangerous-content") # list of channels to post in, not really used, posts everywhere in the server

def vectorintention(intention):
    #ideally will determine the vector of the intention, which intention has more matches
    intent_tally = {}
    for intent in intention:
        intent_tally[intent] = 1
    print(intent_tally)


def findintention(message_data):
    #gets the response from phraseresponses dict in jinkospeech
    words = message_data.split(' ')
    phrase = "hm?"
    for word in words:
        if word in phraseresponses:
            response = intentions.get(phraseresponses.get(word))
            choice = randint(0, len(response) - 1)
            phrase = response[choice]
    return phrase

def simple_response(message_data, author, count):
    if message_data in simple_phrases:
        if message_data == "who am i" or message_data == "who am i?" or message_data == "what is my name" or message_data == "what is my name?":
            if author in knownusers:
                return str(simple_phrases.get(message_data)) + author, count
            else:
                return "i don't know you yet! say jinko so i can know your name :3", count
        elif message_data == "how are you" or message_data == "how are you?":
            choice = randint(0,3)
            resp = simple_phrases.get(message_data)
            return resp[choice], count
        else:
            return simple_phrases.get(message_data), count
    else:
        c = count
        if c >= 0:
            response = findintention(message_data)
            c = 0
            return(response, c)
        else:
            c = count + 1
            return("", c)

cunt = 0 # temporary frequency limit on responses
@client.event
async def on_message(message):
    #header = str(message)
    #print(header)
    global cunt
    body = str(message.content)
    replied = False
    msg_location = message.channel.guild
    author = message.author
    mem = Memory(body.lower(), message.author.name, message.channel.guild, message.channel.name, message.created_at) # make a memory
    memory = json.dumps(mem.jsonify()) # convert to json
    f = open('storage.txt', 'a')
    f.write(memory + "\r") # write memory to storage
    f.close()
    #print(body)#turn off printing debug
    if(message.author != client.user):# if message author is not jinko
        intent = findintention(body.lower()) # get intention
        reply = simple_response(body.lower(), message.author.name, cunt) # get response
        cunt = reply[1]
        #print(cunt)
        if reply[0] != "":
            await message.channel.send(reply[0]) # send reply, will go to the same channel the message was sent


print("starting jinko-chan version 0.0")
print("hello master~")
print("i love you so muchhh~<3")
client.run(token)


