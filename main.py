import speech_recognition as sr
from gtts import gTTS
from pygame import mixer # Load the required library
import os

mixer.init()
r=sr.Recognizer()

with sr.Microphone() as source:
    print ("wait")
    r.adjust_for_ambient_noise(source)
    i=0
    while True:
        i=i+1
        print(i)
        print("say")
        audio = r.listen(source)
        print ("listen complete")

        sps=''
        try:
            print ("trying recog")
            sps=r.recognize_google(audio_data=audio,language="bn-BN")
            print("recognition complete")
            print(sps)
            if (sps=="কেমন আছো"):
                print("Ami valo asi")
                tts = gTTS(text="আমি ভালো আছি । আপনি কেমন আছেন?", lang='bn')
                print("TTs complete")
            elif (sps=="ভালো"):
                print("Good")
                tts = gTTS(text="শুনে খুশি হলাম।", lang='bn')
                print("TTs complete")
            else:
                print("Not Recognized")
                tts = gTTS(text="ঠিক বুঝলাম না।", lang='bn')
                print("TTs complete")
            try:
                tts.save("test.mp3")
            except:
                print("can't save")
            print("saved")
    
            mixer.music.load('test.mp3')
            mixer.music.play()
            while(mixer.music.get_busy()):
                pass
            mixer.music.load('test2.mp3')
            print("end")
        except:
            pass
