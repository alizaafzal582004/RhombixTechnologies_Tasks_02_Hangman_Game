import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# Initialize recognizer and engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Make assistant speak
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Take command from microphone
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "assistant" in command:   # wake word
                command = command.replace("assistant", "")
                print(command)
    except:
        command = ""
    return command

# Run assistant
def run_assistant():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("Playing " + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk("The time is " + time)
    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 1)
        talk(info)
    elif "joke" in command:
        talk(pyjokes.get_joke())
    else:
        talk("Sorry, I didn’t understand. Can you repeat?")

# Keep running
while True:
    run_assistant()
