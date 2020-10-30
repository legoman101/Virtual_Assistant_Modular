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
import speech_recognition as s_r
import pyaudio

load_dotenv()


TOKEN = os.getenv('DISCORDHOST_TOKEN') #token for the Host Bot
client = discord.Client() #set the client
query = "" #query = nothing


#speech
engine = pyttsx3.init('sapi5')

def printspeak(text): 
    print(text)
    engine.say(text)
    engine.runAndWait()

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
            r = s_r.Recognizer()
            my_mic = s_r.Microphone(device_index=1) #my device index is 1, you have to put your device index
            with my_mic as source:
                #printspeak("Listening...")
                await message.channel.send('Listening...')
                r.adjust_for_ambient_noise(source) #reduce noise
                audio = r.listen(source) #take voice input from the microphone
            voiceinput = (r.recognize_google(audio)) #voiceinput = myCommand()
            await message.channel.send('//'+voiceinput)
            if 'abort' in voiceinput:
                await message.channel.send('//almightykill')

        if '//bot4end' in query or '//bot4abort' in query or '//bot4kill' in query or '//almightykill' in query or '//almighty kill' in query:
            await message.channel.send( 'Ending Bot')
            await client.close()

client.run(TOKEN) #runs the bot