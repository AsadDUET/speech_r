# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 11:08:29 2018

@author: asado
"""

import speech_recognition as sr
from gtts import gTTS
from pygame import mixer # Load the required library
import os
import os.path
import sys
import datetime
import json
from mtranslate import translate

import threading
import datetime
import time

mixer.init()

def count():
    for x in range(20):
        print(x)
        time.sleep(.2)


#t=threading.Thread(name="count",target=count)
#t.start()
a = datetime.datetime.now()
tts = gTTS(text=translate("25th of December তারিখে  আপনার Dhaka যাওয়ার 5  টি সিট বুকিং সম্পন্ন হয়েছে, ধন্যবাদ",'bn'), lang='bn')
print(translate("25th of December তারিখে  আপনার Dhaka যাওয়ার 5  টি সিট বুকিং সম্পন্ন হয়েছে, ধন্যবাদ",'bn'))
b = datetime.datetime.now()
print("TTS time: ",b-a)

try:
    a = datetime.datetime.now()
    tts.save("test.mp3")
    b = datetime.datetime.now()
    print("Saveing time: ",b-a)
except:
    print("can't save")
print(type(tts ))

mixer.music.load("test.mp3")
mixer.music.play()
for x in range(20):
        print(x)
        time.sleep(.2)
while(mixer.music.get_busy()):
    pass
mixer.music.load("test2.mp3")
print("end")