# Virtual assistant
This is a collection of Dicord bots

Each one does a different role:
 ```Joshs-Laptop.py``` = runs commands for on Josh's-Laptop.
 ```Flynns-Laptop.py``` = runs commands for on Flynn's-Laptop.
 ```Server.py``` = runs the commands that aren't attached to a device.
 ```Host.py``` = takes a voice input and turns it into the commands to be put onto the server.

To run:

Go to : https://realpython.com/how-to-make-a-discord-bot-python/
And follow the instructions on how to make a bot
you need to create 4 bots: (if you want to make these a bit nicer, then you can use the images in the ```Additional Parts``` folder to attach to your bots.)
- Flynn's Laptop
- Josh's Laptop
- Host
- Server

Get the four ID Tokens and put them into a file named ```.env```
The format of this is:
```
# .env

#Discord
DISCORDMANAGER_TOKEN = *#*
DISCORDHOST_TOKEN = *#*
DISCORDJOSHLAPTOP_TOKEN = *#*
DISCORDFLYNNLAPTOP_TOKEN = *#*
DISCORDSERVER_TOKEN = *#*
DISCORD_GUILD = *#*

#Other
wolframappid = *#*

#email
Your_Username = *#*
Codingemail = *#*
Normalemail = *#*
Your_Password = *#*

#Paths
songs_dir = \\*\\*\\*\\*\\*\\Music # for music playing
ChromePath = C:/*/*/*/*/chrome.exe %s
VsCodePath = \\*\\*\\*\\*\\*\\Visual Studio Code.lnk
PythonPath = \\*\\*\\*\\*\\*\\IDLE (Python 3.8 32-bit).lnk
SpotifyPath = \\*\\*\\*\\*\\*\\Spotify.lnk
AndroidStudioPath = \\*\\*\\*\\*\\*\\Android Studio.lnk



```

Run: ```pip install -r requirements.txt``` to pip install everything you need.
Run: ```server.py``` and then go to your discord guild/server and type ```//start all``` to start all of the bots or,  ```//start [bot name]``` for certain bots.
OR: run them all at the same time from the command line or straight from the python shell.

NOTE: when running the ```Wiimote-typing.py``` script you need to use the command ```python Wiimote-typing.py``` and not ```python3```