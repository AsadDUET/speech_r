# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 00:29:00 2018

@author: Asad
"""
from pygame import mixer
mixer.init()
mixer.music.load('test.mp3')
mixer.music.play()