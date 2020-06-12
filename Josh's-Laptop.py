import discord
import asyncio
from dotenv import load_dotenv #to get everything from the .env
import pyttsx3 # for text-to-speech
import webbrowser #for opening web pages
import smtplib #for emailing
import random # to pick random
import speech_recognition as sr #for speech-to-text
import wikipedia #to look stuff up
import datetime #to find the date+time
import wolframalpha # to do maths
import os # to open programs
import sys # to use the system
import time #so you can wait
import keyboard #to register a keypress
from pynput.keyboard import Key, Controller #to use the media keys
import pynput
from googlesearch import search  # to search google for things


load_dotenv()

#setup pynput
pynputkeyboard = Controller()

TOKEN = os.getenv('DISCORDJOSHLAPTOP_TOKEN') #token for the Laptop Bot
client = discord.Client() #set the client
query = "" #query = nothing

#speech
engine = pyttsx3.init('sapi5')

MASTER = 'Josh'

#wolfram setup
wolframappid = os.getenv('wolframappid')
wolframclient = wolframalpha.Client(wolframappid)

def lowkey(text): #press a lower case key, or a key without shift added
    pynputkeyboard.press(text)
    pynputkeyboard.release(text)

def printspeak(text): 
    print(text)
    engine.say(text)
    engine.runAndWait()

def gotowebpage(text):
    chrome_path = os.getenv('chrome_path') #chrome path from the .env
    webbrowser.get(chrome_path).open(text)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    query = message.content.lower() # saves query as the message
    if message.content.startswith('//'):
        if '//jlaptop' in query or '//jcomputer' in query:
            query = query.replace('//jlaptop', '')
            query = query.replace('//jcomputer', '')

#search commands
            if 'go to web page' in query or 'gotowebpage' in query:
                query = query.replace("go to web page", "")
                query = query.replace("gotowebpage", "")
                await message.channel.send("Opening " +query)
                gotowebpage(query)

            elif 'search google' in query or 'search' in query:
                query = query.replace("search", "")
                query = query.replace("google", "")
                thingtosearch  = query
                await message.channel.send('This will return the first item URL')
                await message.channel.send(".")

                for j in search(thingtosearch, tld='co.uk', num=10, stop=1, pause=2):
                    await message.channel.send(j)

            elif 'wolfram' in query or 'wolf ram' in query or 'wolf' in query or 'ram' in query:
                try:
                    query = query
                    res = wolframclient.query(query)
                    wolframresults = next(res.results).text
                    await message.channel.send('WOLFRAM-ALPHA says - ')
                    await message.channel.send('Got it.')
                    await message.channel.send(wolframresults)  

                except:
                    webbrowser.open('www.google.com')
            
            elif 'wikipedia' in query:
                await message.channel.send("Searching wikipedia...")
                query = query.replace("wikipedia", "")
                wikipediaresults = wikipedia.summary(query, sentences =2)
                await message.channel.send(wikipediaresults)
# end of search commands
#
#music commands
            elif 'play music' in query: #play music from the music folder in your personal onedrive
                songs_dir = os.getenv('songs_dir')
                songs = os.listdir(songs_dir)
                await message.channel.send(songs)
                os.startfile(os.path.join(songs_dir, songs[0]))

            elif 'press play' in query or 'press pause' in query: #press the media play/pause button
                await message.channel.send("Pressing media key...")
                lowkey(Key.media_play_pause)

            elif 'play random music' in query or 'random music' in query: #play random music from your music folder in your personal onedrive
                music_folder = os.getenv('songs_dir')
                music = ['applause', 'laughing', 'keyboard', 'bomb', 'camera']
                random_music = music_folder + random.choice(music) + '.mp3'
                os.system(random_music)
                    
                await message.channel.send('Okay, here is your music! Enjoy!')
#end of music commands
#
#email commands
            elif 'email' in query:

                Your_Username = os.getenv('Your_Username')
                Codingemail = os.getenv('Codingemail')
                Normalemail = os.getenv('Normalemail')
                Your_Password = os.getenv('Your_Password')

                query = query.replace("email", "")
                recipient = query

                if 'me' in recipient: #if you want to send an email to yourself
                    try:
                        await message.channel.send('What should I say? ')
                        query = query.replace("me", "")
                        server = smtplib.SMTP('smtp.gmail.com', 587)# use the gmail server
                        server.ehlo()
                        server.starttls()
                        server.login(Your_Username, Your_Password) #use your credentials
                        server.sendmail(Your_Username, Normalemail, query) #send email with the voice recording as content, and send it to yourself
                        server.close()
                        await message.channel.send('Email sent!')

                    except:
                        await message.channel.send(f'Sorry {MASTER} I am unable to send your message at this moment!')

                elif 'code' in recipient or 'coding' in recipient: #if you want to send an email to your coding account
                    try:
                        await message.channel.send('What should I say? ')
                        query = query.replace("code", "")
                        query = query.replace("coding", "")

                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.ehlo()
                        server.starttls()
                        server.login(Your_Username, Your_Password)
                        server.sendmail(Your_Username, Codingemail, query) #send email with the voice recording as content, and send it to your coding email address
                        server.close()
                        await message.channel.send('Email sent!')

                    except:
                        await message.channel.send(f'Sorry {MASTER} I am unable to send your message at this moment!') #error message
#end of email commands
#
#All of the open commands, (Programs and Folders)

            elif 'open youtube' in query: #open youtube
                await message.channel.send('Opening youtube...')
                gotowebpage('www.youtube.com')

            elif 'open apireference' in query or 'api reference' in query:
                await message.channel.send('Opening Discord.py API refrence...')
                gotowebpage('https://discordpy.readthedocs.io/en/latest/api.html?highlight=discord.message#')

            elif 'open discord dev portal' in query or 'open discorddevportal' in query:
                await message.channel.send('Opening Discord Development Portal...')
                gotowebpage('https://discord.com/developers/applications/718527530935779438/bot')

            elif 'open gmail' in query: #open gmail
                await message.channel.send('Opening Gmail...')
                gotowebpage('www.gmail.com')

            elif 'open github' in query or 'open git hub' in query:
                await message.channel.send('Opening GitHub...')
                gotowebpage('github.com')

            elif 'open google' in query: #open google
                await message.channel.send('Opening Google...')
                gotowebpage('www.google.co.uk')

            elif 'open stackoverflow' in query: #open stack overflow
                await message.channel.send('Opening Stack Overflow...')
                gotowebpage("stackoverflow.com")
                
            elif 'open visual studio' in query or 'start visual studio' in query or 'vscode' in query: #open visual studio
                await message.channel.send("Opening Visual studio Code...")
                VsCodePath = os.getenv('VsCodePath')
                os.startfile(VsCodePath)
                
            elif 'open python' in query or 'start python' in query: #open Python IDLE 3
                await message.channel.send('Opening Python IDLE... ')
                PythonPath = os.getenv('PythonPath')
                os.startfile(PythonPath)

            elif 'open android studio' in query or 'android studio' in query or 'start android studio' in query: # open android studio
                await message.channel.send("Opening Android Studio...")
                AndroidStudioPath = os.getenv('AndroidStudioPath')
                os.startfile(AndroidStudioPath)

            elif 'open spotify' in query or 'start spotify' in query: #open spotify
                await message.channel.send("Opening Spotify...")           
                SpotifyPath = os.getenv('SpotifyPath')
                os.startfile(SpotifyPath)
#end of open commands.
#
        if '//bot2end' in query or '//bot2abort' in query or '//bot2kill' in query or '//almightykill' in query:
            await message.channel.send( 'Ending Bot')
            await client.close()

        if '//say' in query:
            query = query.replace("//say", "")
            printspeak(query)

        if '//takecommand' in query:
            await message.channel.send('//host takecommand')



client.run(TOKEN) #runs the bot