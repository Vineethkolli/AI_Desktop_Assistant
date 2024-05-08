import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine. setProperty( name: 'rate', rate-70)
    engine.say(text)
    engine.runAndWait()
