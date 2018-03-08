import speech_recognition as sr
r=sr.Recognizer()

with sr.Microphone() as source:
    print ("Say Something")
    audio = r.listen(source)

try:
    print(r.recognize_google(audio_data=audio,language="bn-BN"))
except:
    pass
