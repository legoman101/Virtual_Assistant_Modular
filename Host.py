import discord
import asyncio
from dotenv import load_dotenv
import pyttsx3 # for text-to-speech
import random # to pick random
import webbrowser #for opening web pages
import datetime #to find the date+time
import wolframalpha # to do maths
import os # to open programs
import sys # to use the system
import time #so you can wait
from googlesearch import search  # to search google for things
import speech_recognition as sr

load_dotenv()


TOKEN = os.getenv('DISCORDHOST_TOKEN') #token for the Host Bot
client = discord.Client() #set the client
query = "" #query = nothing


#speech
engine = pyttsx3.init('sapi5')

MASTER = 'Master'

def printspeak(text): 
    print(text)
    engine.say(text)
    engine.runAndWait()

def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:
        printspeak("Listening...")
        #r.pause_threshold =  1
        audio = r.listen(source) #listen for input
    try:
        query = r.recognize(audio) #query = the words from the recording
        print('User: ' + query + '\n') # print User said: (and then the words from the recording)
        
    except Exception as e: #If it cant understand it, then it will ask for a typed input.
        printspeak(f'Sorry {MASTER} I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    query = message.content.lower() # saves query as the message
    if message.content.startswith('//'):
        if '//takecommand' in query:
            voiceinput = myCommand()
            await message.channel.send('I got: ' +voiceinput)

        if '//bot4end' in query or '//bot4abort' in query or '//bot4kill' in query or '//almightykill' in query:
            await message.channel.send( 'Ending Bot')
            await client.close()

client.run(TOKEN) #runs the bot