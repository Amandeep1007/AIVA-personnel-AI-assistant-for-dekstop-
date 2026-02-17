import sounddevice as sd
import numpy as np
import speech_recognition as sr
from scipy.io.wavfile import write

def listen_wake_word():
    r = sr.Recognizer()

    while True:
        print("Waiting for wake word: hey AIVA")

        fs = 16000
        seconds = 3

        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        sd.wait()

        audio_data = np.int16(recording * 32767)
        write("wake.wav", fs, audio_data)

        with sr.AudioFile("wake.wav") as source:
            audio = r.record(source)

        try:
            text = r.recognize_google(audio).lower()
            print("Heard:", text)

            if "hey AIVA" in text:
                return

        except:
            pass

