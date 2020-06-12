import speech_recognition as s_r
import pyttsx3 # for text-to-speech


#speech
engine = pyttsx3.init('sapi5')

def printspeak(text): 
    print(text)
    engine.say(text)
    engine.runAndWait()

def myCommand():
    r = s_r.Recognizer()
    my_mic = s_r.Microphone(device_index=1) #my device index is 1, you have to put your device index
    with my_mic as source:
        printspeak("Say now!!!!")
        r.adjust_for_ambient_noise(source) #reduce noise
        audio = r.listen(source) #take voice input from the microphone
    #printspeak(r.recognize_google(audio)) #to print voice into text
    query = (r.recognize_google(audio))
    return query

query = myCommand()
printspeak(query)