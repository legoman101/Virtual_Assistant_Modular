import pyttsx3 #for text-to speach
import speech_recognition as sr #for speech-to-text


def printspeak(text): #definition for JARVIS to speak and print what is inputed: printspeak(what you want him to say and print)
    print(text)
    engine.say(text)
    engine.runAndWait()

# Initialize speech 
engine = pyttsx3.init('sapi5')

#set the username
MASTER = '{Name of Master}'

#what voice the text to speech will use
american = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0" #Path to the american voice
british = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0" #Path to the british voice
speakingvoice = british # default speaking voice is british

#set the speaking engine
voices = engine.getProperty('voices')
#set the words per minute rate of speech engine
engine.setProperty('voice', speakingvoice)


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

query = myCommand()

printspeak('User said: ',query)
