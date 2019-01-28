# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 03:15:27 2019

@author: asado
"""

from selenium import webdriver
import time
chrome_path='/usr/lib/chromium-browser/chromedriver'
options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument("--use-fake-ui-for-media-stream")
driver = webdriver.Chrome(chrome_path,options=options)
driver.get("https://translate.google.com/#view=home&op=translate&sl=bn&tl=en")
           
driver.find_element_by_id("gt-speech").click()
time.sleep(2)
print("Speak now")
text=''
text2=''
def voice_from_chrome():
    global text
    global text2
    if (driver.find_element_by_id("gt-speech").get_attribute('aria-label')=="Turn off voice input"):
        print(driver.find_element_by_id("gt-speech").get_attribute('aria-label')+'if')
        time.sleep(.4)
        if (driver.find_element_by_id("gt-speech").get_attribute('aria-label')=="Turn off voice input"):
            text=driver.find_element_by_class_name("text-dummy").get_attribute('innerHTML')
            time.sleep(.4)
        if (driver.find_element_by_id("gt-speech").get_attribute('aria-label')=="Turn off voice input"):
            text2=driver.find_element_by_class_name("text-dummy").get_attribute('innerHTML')
            time.sleep(.4)
        if(text==text2):
            if(text!=''):
                print(text2)
                driver.find_element_by_id("gt-speech").click()
                print('off clicked')
                return driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/span[1]/span").get_attribute('innerHTML')
                time.sleep(.5)
                
                
    else:
        print(driver.find_element_by_id("gt-speech").get_attribute('aria-label')+'else')
        if (driver.find_element_by_id("gt-speech").get_attribute('aria-label')=="Turn on voice input"):
            driver.find_element_by_id("gt-speech").click()
        print('on clicked')
        text=text2=''
if __name__=="__main__":
    while True:
        sps=None
        while (sps==None):
            sps=voice_from_chrome()
    
    
