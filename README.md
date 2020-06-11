# Virtual assistant
This is a collection of Dicord bots

Each one does a different role:
 ```Josh's-Laptop.py``` = runs commands for on Josh's-Laptop.
 ```Flynn's-Laptop.py``` = runs commands for on Flynn's-Laptop.
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

DISCORDMANAGER_TOKEN = '*'
DISCORDHOST_TOKEN = '*'
DISCORDJOSHLAPTOP_TOKEN = '*'
DISCORDFLYNNLAPTOP_TOKEN = '*'
DISCORDSERVER_TOKEN = '*'
DISCORD_GUILD = '*'

```

Get the app tokens for Gmail, Wolfram, and the Accounts for your email. and put them into a file named ```Passes.py```
The format of this is:
```

#Passes.py
#Passwords:
wolframappid = '*'
Your_Username = '*'
Codingemail = '*'
Normalemail = '*'
our_Password = '*'

songs_dir = '//*//*//*'

```

Run: ```pip install -r requirements.txt``` to pip install everything you need.
Run: ```server.py|Josh's-Laptop.py|Flynn's-Laptop.py``` to start the bots.
Alternitively: ```server.py``` and then go to your discord guild/server and type ```//start Flynn's-Laptop``` and ```//start Flynn's-Laptop```