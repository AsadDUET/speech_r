
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
import VoiceUsingChrome
# CLIENT_ACCESS_TOKEN = '67d03b977e32456d89d1e4e84613cac5'#bangla
CLIENT_ACCESS_TOKEN = 'dde3d7f999434732a56d9887b7c43d09'#robot
#CLIENT_ACCESS_TOKEN = '332da3ed83324895993de3f7f7ca5f91'#asad
#CLIENT_ACCESS_TOKEN ='1a62a0de8e1a42bdb544334977437567 '#joke
thinking=0
mixer.init()
response_json =''
def dialog(text):
    global response_json
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
    request = ai.text_request()
    request.session_id = "<robot>"
    request.query = text
    response = request.getresponse()
    a=str(response.read(), 'utf-8')
    response_json =json.loads(a)
    print(response_json)
    print(response_json['result']['metadata']['intentName'])
    return (response_json["result"]["fulfillment"]["messages"][0]["speech"])#["textToSpeech"])

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
    global response_json
    while True:
        try:
            servo.listening_led()
            c=datetime.datetime.now()
            sps=None
            while (sps==None):
                sps=VoiceUsingChrome.voice_from_chrome()
            print(sps)
            servo.processing_led()

            a = datetime.datetime.now()
            spsr=dialog(sps)
            b = datetime.datetime.now()
            print("dialogflow time: ",b-a)
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

            while(mixer.music.get_busy()):
                    servo.talking()
            mixer.music.load("test2.mp3")
            
            if(response_json['result']['metadata']['intentName']=='look'):
                time.sleep(.5)
                if(response_json['result']['parameters']['look_direction']=='up'):
                    servo.up()
                elif(response_json['result']['parameters']['look_direction']=='left'):
                    servo.left_turn()
                elif(response_json['result']['parameters']['look_direction']=='right'):
                    servo.right_turn()
                elif(response_json['result']['parameters']['look_direction']=='front'):
                    servo.mid()
            print("end")
        except KeyboardInterrupt:
            raise
        except:
            print("main loop error")
            pass

while True:
        try:
            conversation()
        except KeyboardInterrupt:
            raise
