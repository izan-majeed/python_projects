import speech_recognition as sr 
import pyfiglet

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    data = r.record(source, duration=2)  
    text = r.recognize_google(data)
    result = pyfiglet.figlet_format(text)
    print(result)
