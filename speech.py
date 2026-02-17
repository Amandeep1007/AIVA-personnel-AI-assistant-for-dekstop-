import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
current_voice = 0

def set_voice(mode):
    global current_voice
    if mode == "male":
        current_voice = 0
    elif mode == "female" and len(voices) > 1:
        current_voice = 1
    elif mode == "robot":
        engine.setProperty("rate", 130)

def speak(text):
    engine.setProperty("voice", voices[current_voice].id)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        return r.recognize_google(audio).lower()
    except:
        return ""

