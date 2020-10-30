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

songs_dir = os.getenv('songs_dir')
wolframappid = os.getenv('wolframappid')

load_dotenv()

TOKEN = os.getenv('DISCORDSERVER_TOKEN') #token for the server Bot
client = discord.Client() #set the client
query = "" #query = nothing

#speech
engine = pyttsx3.init('sapi5')

MASTER = 'Josh'

#wolfram setup
wolframclient = wolframalpha.Client(wolframappid)

def printspeak(text): 
    print(text)
    engine.say(text)
    engine.runAndWait()

def gotowebpage(text):
    chrome_path = os.getenv('Chrome Path')
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
        if 'server' in query: #any commands aimed at the server bot
            query = query.replace("server", "")
            #Misicalious commands
            if 'hello' in query:
                await message.channel.send('Hello👋')
        
            elif 'greet' in query:
                currentH = int(datetime.datetime.now().hour)
                if currentH >= 0 and currentH < 12:
                    await message.channel.send('Good Morning!')

                if currentH >= 12 and currentH < 18:
                    await message.channel.send('Good Afternoon!')

                if currentH >= 18 and currentH !=0:
                    await message.channel.send('Good Evening!')
            
            elif 'the time' in query or 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                await message.channel.send(f"{MASTER} the time is {strTime}")

            elif 'your info' in query:
                await message.channel.send("My name is Jarvis, your digital assistant")

            elif 'my info' in query:
                await message.channel.send("Your name is " +MASTER)

            elif "what\'s up" in query or 'how are you' in query:
                stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
                await message.channel.send(random.choice(stMsgs))           
           
            elif 'happy birthday' in message.content.lower():
                await message.channel.send('Happy Birthday! 🎈🎉')
                
           # end of miscilanious commands

            #starting other bots        
        
        if message.content.startswith('//start'):
            query = query.replace("//start", "")
            if 'joshslaptopbot' in query:
                os.system('python Joshs-Laptop.py')
                #await message.channel.send('Joshs-Laptop.py has started. Bot now active.')

            if 'hostbot' in query:
                os.system('python host.py')
                #await message.channel.send('host.py has started. Bot now active.')

            ''' #commented this bit out as only one bot is being used for testing.
            if 'flynnslaptopbot' in query:
                os.system('python Flynns-Laptop.py')
                #await message.channel.send('Flynns-Laptop.py has started. Bot now active.')
            '''

            if 'all' in query:
                os.system('python Joshs-Laptop.py')
                os.system('python host.py')
                #os.system('python Flynns-Laptop.py')
                #await message.channel.send('Flynns-Laptop.py & Joshs-Laptop.py & host.py have started. Bots are now active.')

        if '//bot1end' in query or '//bot1abort' in query or '//bot1kill' in query or '//almightykill' in query or '//almighty kill' in query:
            await message.channel.send( 'Ending Bot')
            await client.close()
                
        if message.content.startswith('//help'):
            query = query.replace("//help", " ")

            if 'all' in query:
                await message.channel.send('$//takecommand - will take your voice input')
                await message.channel.send('$//jlaptop will mean you are interfacing with the laptop set of code {type //help jlaptop for more help}')
                await message.channel.send('$//flaptop will mean you are interfacing with the laptop set of code {type //help flaptop for more help}')
                await message.channel.send('$//server will mean you are interfacing with the server set of code {type //help server for more help}')
                await message.channel.send('$//bot{1/2/3}end, //bot{1/2/3}kill or //bot{1/2/3}abort will close the discord bot -[bot1 = server, bot2 = JLaptop, bot3 = FLaptop] {WARNING: this will mean that you will have to reload the bot with the code}')
                await message.channel.send('$//say will make my laptop say what ever you type after')
                await message.channel.send('$//help will list all of the commands (this list)')
                await message.channel.send('$//almightykill will close all of the bots- {WARNING: this will mean that you will have to reload the bot with the code}')

            if 'server' in query:
                await message.channel.send('$//server hello - says hello back')
                await message.channel.send('$//server greet - says good morning/afternoon/evening depending on the time')
                await message.channel.send('$//server time - sends the current time')
                await message.channel.send('$//server your info - will return information about the virtual assistant')
                await message.channel.send('$//server my info - will returninformation about the user')
                await message.channel.send('$//server what\'s up - will return how the virtual assistant is feeling today')
                await message.channel.send('$//server how are you - will return how the virtual assistant is feeling today')
                await message.channel.send('$//bot1end, //bot1kill, //bot1abort - will end the program for the server bot')
                await message.channel.send('$//start {joshslaptopbot/flynnslaptopbot/managerbot/hostbot} - will start the python script for the appropriate bot [WARNING: make sure you keep the python tab OPEN]')
                await message.channel.send('$//clear {x amount of messages} - deletes x amount of messages')
                
            if 'josh laptop' in query or 'josh\'s laptop' in query:
                
                #misc
                await message.channel.send('$//bot2end, //bot2end, //bot2end - will end the program for the laptop bot')
                
                #search
                await message.channel.send('$//josh\'s laptop gotowebpage {the webpage you want to go to}- this will open the webpage on MY laptop')
                await message.channel.send('$//josh\'s laptop google search {search } - will return the first URL from a google search of that thing')
                await message.channel.send('$//josh\'s laptop search {search } - will return the first URL from a google search of that thing')
                await message.channel.send('$//josh\'s laptop wolfram {search } - will search wolfram fro that thing (currently not working)')
                await message.channel.send('$//josh\'s laptop wikipedia {search} - will search wikipedia for that thing and return the first 2 lines of the wikipedia page')
                
                #music
                await message.channel.send('$//josh\'s laptop play music - will play music from a pre-determined folder')
                await message.channel.send('$//josh\'s laptop press play - will press the play/pause media button')
                await message.channel.send('$//josh\'s laptop press pause - will press the play/pause media button')
                await message.channel.send('$//josh\'s laptop play random music - will play random music in shuffle from a pre-determined folder')
                
                #email
                await message.channel.send('$//josh\'s laptop email {recipient(me/coding)} {content}')

                #open
                await message.channel.send('$//josh\'s laptop open youtube - opens youtube')
                await message.channel.send('$//josh\'s laptop open gmail - opens gmail')
                await message.channel.send('$//josh\'s laptop open github - opens github')
                await message.channel.send('$//josh\'s laptop open google - opens google')
                await message.channel.send('$//josh\'s laptop open stack overflow - opens stackoverflow')
                await message.channel.send('$//josh\'s laptop open disney+ - opens disney+')
                await message.channel.send('$//josh\'s laptop open vscode - opens Visual Studio Code')
                await message.channel.send('$//josh\'s laptop open python - opens python')
                await message.channel.send('$//josh\'s laptop open android studio - opens android studio')
                await message.channel.send('$//josh\'s laptop open spotify - opens spotify')
                await message.channel.send('$//josh\'s laptop open api reference - opens the Discord.py API reference')
                await message.channel.send('$//josh\'s laptop open discord dev portal - opens the Discord bot development portal')
        
            ''' #commented this bit out as only one bot is being used for testing.
            if 'flynn laptop' in query or 'flynn\'s laptop' in query:
                
                #misc
                await message.channel.send('$//bot3end, //bot3end, //bot3end - will end the program for the laptop bot')
                
                #search
                await message.channel.send('$//flynn\'s laptop gotowebpage {the webpage you want to go to}- this will open the webpage on MY laptop')
                await message.channel.send('$//flynn\'s laptop google search {search } - will return the first URL from a google search of that thing')
                await message.channel.send('$//flynn\'s laptop search {search } - will return the first URL from a google search of that thing')
                await message.channel.send('$//flynn\'s laptop wolfram {search } - will search wolfram fro that thing (currently not working)')
                await message.channel.send('$//flynn\'s laptop wikipedia {search} - will search wikipedia for that thing and return the first 2 lines of the wikipedia page')
                
                #music
                await message.channel.send('$//flynn\'s laptop play music - will play music from a pre-determined folder')
                await message.channel.send('$//flynn\'s laptop press play - will press the play/pause media button')
                await message.channel.send('$//flynn\'s laptop press pause - will press the play/pause media button')
                await message.channel.send('$//flynn\'s laptop play random music - will play random music in shuffle from a pre-determined folder')
                
                #email
                await message.channel.send('$//flynn\'s laptop email {recipient(me/coding)} {content}')

                #open
                await message.channel.send('$//flynn\'s laptop open youtube - opens youtube')
                await message.channel.send('$//flynn\'s laptop open gmail - opens gmail')
                await message.channel.send('$//flynn\'s laptop open github - opens github')
                await message.channel.send('$//flynn\'s laptop open google - opens google')
                await message.channel.send('$//flynn\'s laptop open stack overflow - opens stackoverflow')
                await message.channel.send('$//flynn\'s laptop open vscode - opens Visual Studio Code')
                await message.channel.send('$//flynn\'s laptop open python - opens python')
                await message.channel.send('$//flynn\'s laptop open spotify - opens spotify')
        '''

        if message.content.startswith('//return'):
            query = query.replace("return ", "")
            await message.channel.send(query)

        if message.content.startswith('//todolist'):
            await message.channel.send('Change it so that rather than using the Wiimote-typing.py script you use a button attached to a pi, with the sccripts running off of the pi.')
            await message.channel.send('Get wolfram working')
            await message.channel.send('Fix the //start function for the hostbot')
            await message.channel.send('Create a clear function')

        if message.content.startswith('//clear'):
            await message.channel.send('Clearing messages...')
            await message.delete()
            

client.run(TOKEN) #runs the bot