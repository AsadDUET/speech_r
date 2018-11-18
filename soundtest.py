# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 18:04:10 2018

@author: asado
"""

import urllib3
from pydub import AudioSegment
from pydub.playback import play


mp3file = urllib3.urlopen("http://www.bensound.org/bensound-music/bensound-dubstep.mp3")
with open('./test.mp3','wb') as output:
  output.write(mp3file.read())

song = AudioSegment.from_mp3("./test.mp3")
play(song)