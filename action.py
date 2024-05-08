import datetime
import speak
import webbrowser
import weather
import os
def Action(send) _:
    data_btn = send. lower()
    if "what is your name" in data_btn :
        speak.speak("my name is virtual Assistant")
        return "my name is virtual Assistant"
        
    elif "hello" in data_btn or "hye" in data_btn_or "hay" in data_btn:
        speak. speak("Hey sir, How i can help you !")
        return "Hey sir, How i can help you !"

    elif "how are you" in data_btn :
        speak.speak("I am doing great these days sir")
        return "I am doing great these days sir"

    elif "thanku" in data_btn or "thank" in data_btn:
        speak.speak("its my pleasure sir to stay with you")
        return "its my pleasure sir to stay with you"

    elif "good morning" in data_btn:
        speak.speak("Good morning sir, i think you might need some help")
        return "Good morning sir, i think you might need some help"

    elif "time now" in data_btn:
        current_time = datetime.datetime.now()

def Action(send) :
        webbrowser. open("https://gaana.com/")
        speak. speak("gaana.com is now ready for you, enjoy your music")
        return "gaana.com is now ready for you, enjoy your music"
    
    elif 'open google' in data_btn or 'google' in data_btn:
        url = 'https://google.com/'
        webbrowser. get().open(url)
        speak.speak("google open")
        return "google open"
    
    elif 'youtube' in data_btn or "open youtube" in_data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak. speak("YouTube open")
        return "YouTube open"
        
    elif 'weather' in data_btn _:
        ans = weather .Weather ()
        speak. speak (ans)
        return ans
        
    elif 'music from my laptop' in data_btn:
        url = 'D:\\music'
        songs = os.listdir(url)
        os.startfile(os.path. join(url, songs[0]))
        speak.speak("songs playing ... ")
        return "songs playing ... "
    elif "srm" in data_btn or "open srm" in data_btn:
        url = "https://www.srmist.edu.in/"
        webbrowser.get().open(url)
        speak.speak("SRM Institute of Science and Technology - One of India's Best Ranked Universities")
        return "Opened SRM Web .. "
    
    elif "ranjith" in data_btn or "ranjith instagram" in data_btn:
        url = "https://www.instagram.com/ ranjith .n /"
        webbrowser.get().open(url)
        speak.speak("Ranjith .... Do you mean Topper of SRM RANJITH")
        return "Opened ranjith insta."
    elif "priyanka" in data_btn or "priyanka mam" in data_btn:
        webbrowser.get().open("https://www.srmist.edu.in/faculty/dr-priyanka-r/")
        speak.speak("Dr. Priyanka R, Assistant Professor in SRM, 5 years of teaching experience")
        return "Opened profile in srm web"
    else _:
        speak.speak(_"i'm able to understand!")
        return "i'm able to understand!"
