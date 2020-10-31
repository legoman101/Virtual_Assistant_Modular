import discord
from dotenv import load_dotenv #to get info from .env files
import os
import pyttsx3 # for text-to-speech

engine = pyttsx3.init('sapi5')
def printspeak(text): 
    print(text)
    engine.say(text)
    engine.runAndWait()

load_dotenv()
TOKEN = 'NzE4MDU3ODAyNjMwODIzOTk3.Xtketw.BGJmiTjbTbtTdj3ulM8ejhB4WKY'
client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return    
    await message.channel.send( 'you said: '+ message.content.lower())
    printspeak(message.content.lower())

client.run(TOKEN)