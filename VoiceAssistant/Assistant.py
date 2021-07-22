import speech_recognition as sr
import pyttsx3       # for siri to respond
import pywhatkit        # to search google, use youtube
import datetime
import wikipedia
import pyjokes

listener=sr.Recognizer()
engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
         with sr.Microphone() as source:
             listener.adjust_for_ambient_noise(source, duration=1)
             print("Listening.....")
             voice=listener.listen(source)
             command=listener.recognize_google(voice)       # speech to text conversion using google API
             command=command.lower()
             if 'alexa' in command:
                 command=command.replace('alexa','')


    except Exception as e:
         print("error : {}".format(e))
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing '+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("Current time is "+time)
    elif 'date' in command:
        today=datetime.date.today()
        print(today)
        talk("Today's date is "+ str(today))
    elif 'tell me about' in command:
        know=command.replace('tell me about','')
        info=wikipedia.summary(know,2)
        print(info)
        talk(info)
    elif 'joke' in command:
        laugh=pyjokes.get_joke()
        print(laugh)
        talk(laugh)
    elif 'invented you' in command:
        print("Venkatesh R Pai")
        talk("Venkatesh R Pai")
    elif 'my birthday' in command:
        print("May 31 2000")
        talk("May 31 2000")
    else:
        talk("I am not programmed for this. Please use available commands")
while True:
    run_alexa()

