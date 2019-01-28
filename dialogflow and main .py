import speech_recognition as sr
from gtts import gTTS
from pygame import mixer
import os
import os.path
import sys
import datetime
import json
from mtranslate import translate
import apiai
import threading
import random
import time
import servo

# CLIENT_ACCESS_TOKEN = '67d03b977e32456d89d1e4e84613cac5'#bangla
CLIENT_ACCESS_TOKEN = 'dde3d7f999434732a56d9887b7c43d09'#robot
#CLIENT_ACCESS_TOKEN = '332da3ed83324895993de3f7f7ca5f91'#asad
#CLIENT_ACCESS_TOKEN ='1a62a0de8e1a42bdb544334977437567 '#joke
thinking=0
mixer.init()
r=sr.Recognizer()
r.energy_threshold = 1000

def dialog(text):
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
    request = ai.text_request()
    request.session_id = "<robot>"
    request.query = text
    response = request.getresponse()
    a=str(response.read(), 'utf-8')
    b=json.loads(a)
    print(b)
    return (b["result"]["fulfillment"]["messages"][0]["speech"])#["textToSpeech"])

def random_sound():
    time.sleep(1)
    random_sounds=["a","b"]
    i=random.randint(0,len(random_sounds)-1)
    try:
        mixer.music.load("sound/"+str(random_sounds[i])+".mp3")
        mixer.music.play()
        while(mixer.music.get_busy()):
            pass
        mixer.music.load("test2.mp3")
    except:
        print("random sound error")
        pass

def conversation():
    while True:
        try:
            
            print("\n\nsay")
            servo.listening_led()
            a = datetime.datetime.now()
            try:
             audio = r.listen(source=source)#,timeout=0.5,phrase_time_limit=5)
            except KeyboardInterrupt:
                raise
            except:
                break
            b = datetime.datetime.now()
            print("listentime: ",b-a)
            c=datetime.datetime.now()
            sps=''
            servo.processing_led()
    ##        time_pass_thread=threading.Thread(name="time_pass_thread",target=servo.slow_motion())
    ##        time_pass_thread.start()
            #try:
            print ("trying recog")
            a = datetime.datetime.now()
            sps=r.recognize_google(audio_data=audio,language="bn-BN")
            b = datetime.datetime.now()
            print("recognize time: ",b-a)
            a = datetime.datetime.now()
            sps=translate(sps)
            b = datetime.datetime.now()
            print("translate time: ",b-a)
            print(sps)

            a = datetime.datetime.now()
            spsr=dialog(sps)
            # spsb=translate(spsr,'bn')
            b = datetime.datetime.now()
            print("dialogflow time: ",b-a)
    ##            time_pass_thread.join()
            if(spsr=="jokes"):
                mixer.music.load("sound/jokes_"+str(random.randint(1,2))+".mp3")
            else:
                try: # Load local
                    a = datetime.datetime.now()
                    mixer.music.load("sound/"+spsr+".mp3")
                    b = datetime.datetime.now()
                    print("local load time: ",b-a)
                except: # load from gtts
                    a = datetime.datetime.now()
                    tts = gTTS(text=spsr, lang='bn')
                    b = datetime.datetime.now()
                    print("TTS time: ",b-a)

                    try: # save with variable name
                        a = datetime.datetime.now()
                        tts.save("sound/"+spsr+".mp3")
                        b = datetime.datetime.now()
                        print("Saveing time: ",b-a)
                        a = datetime.datetime.now()
                        mixer.music.load("sound/"+spsr+".mp3")
                        b = datetime.datetime.now()
                        print("load time: ",b-a)
                    except:
                        try: # save using test name
                            a = datetime.datetime.now()
                            tts.save("test.mp3")
                            b = datetime.datetime.now()
                            print("Saveing time: ",b-a)
                            a = datetime.datetime.now()
                            mixer.music.load("test.mp3")
                            b = datetime.datetime.now()
                            print("load time: ",b-a)
                        except:
                            print("can't save")

            d = datetime.datetime.now()
            print("total time: ",d-c)

            mixer.music.play()

            # print(translate(spsr,'bn'))
            while(mixer.music.get_busy()):
                    servo.talking()
            mixer.music.load("test2.mp3")
            print("end")
        except KeyboardInterrupt:
            raise
        except:
            print("main loop error")
            pass

while True:
    with sr.Microphone() as source:
        try:
            print ("wait")
            r.adjust_for_ambient_noise(source=source,duration=1)
        #        r.operation_timeout = 10

            # detector = r.snowboy_wait_for_hot_word("./","mr.pmdl",source)#"mr.pmdl",
            # detector.start(conversation)
            conversation()
        except KeyboardInterrupt:
            raise
