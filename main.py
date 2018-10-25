import speech_recognition as sr
from gtts import gTTS
from pygame import mixer # Load the required library
import os

mixer.init()
r=sr.Recognizer()

with sr.Microphone() as source:
    print ("Say Something")
    audio = r.listen(source)
    print ("0")

    sps=''
    sps=r.recognize_google(audio_data=audio,language="bn-BN")
    print("1")
    print(sps)
    if (sps=="কেমন আছো"):
        print("Ami valo asi")
        tts = gTTS(text="আমি ভালো আছি । আপনি কেমন আছেন?", lang='bn')
        print("1")
        try:
            tts.save("test.mp3")
        except:
            print("can't save")
        print("3")
        
        mixer.music.load('test.mp3')
        mixer.music.play()
        while(mixer.music.get_busy()):
            pass
        mixer.music.load('test2.mp3')
        print("done")






