import speech_recognition as sr   
import os
import random
import time 
import win32com.client
from datetime import date
from datetime import datetime
import requests
import webbrowser
from subprocess import call
import feedparser
import pyttsx3
import pyperclip
try:
    import httplib
except:
    import http.client as httplib
import pocketsphinx
from sys import exit
import subprocess
import platform
import psutil
import socket
import sys

engine  = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def tell_date() :
        today = date.today()
        print(today.day,"/",today.month,"/",today.year)
        engine.say(today,'en')
        engine.runAndWait()
        
def tell_time() :
        timenow = time.localtime()
            
        if(timenow[3] > 12):
             hr = timenow[3]-12
             meridium = "PM"
             minute = timenow[4]
             print(hr,":",minute,meridium)
             times = str(hr) + str(minute) + meridium
             engine.say(times,'en')
             engine.runAndWait()
        else:
            hr = timenow[3]
            meridium = "AM"
            minute = timenow[4]
            print(hr,":",minute,meridium)
            times = str(hr) + str(minute) + meridium
            engine.say(times,'en')
            engine.runAndWait()
            
def tell_day() :
        day = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        nowday = datetime.today().weekday()
        print(day[nowday])
        engine.say(day[nowday],'en')
        engine.runAndWait()

def tell_weather() :
        api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
        url = api_address + "Mangalore"
        print("Weather in Mangalore")
        json_data = requests.get(url).json()
        wdata = json_data['weather'][0]['main']
        wdesc = json_data['weather'][0]['description']
        wtemp = json_data['main']['temp']
        print(wtemp-273.15,"C")
        print(wdata)
        print(wdesc)
        talk_word = (wtemp-273.15,"degree celcius with",wdesc)
        engine.say(talk_word,'en')
        engine.runAndWait()

def tell_joke():
        joke = random.choice(("What type of nails do carpenters hate to hammer? , Finger nails","A patient sobs to his doctor, I feel like a pair of curtain, Doctor says, Well, pull yourself together man","A man got hit hard in the head with a can of 7up, he is alright though, it was a soft drink","Why does the giraffe has such a long neck, because its feet smell really bad"))
        print(joke)
        engine.say(joke,'en')
        engine.runAndWait()

def open_browser():
        url = "https://google.com/"
        webbrowser.open(url)

def tell_news():
        f = feedparser.parse("https://timesofindia.indiatimes.com/rssfeedstopstories.cms")
        for newsitem in f['items']:
            subprocess.call(["notify-send", newsitem['title'],newsitem['summary']])
            break;

def speakup():
        file = open('test.txt', 'r')
        line = 'sample'
        while (line != '') :
            line = file. readline()
            print (line)
            engine.say(line,'en')
            engine.runAndWait()
        file. close()

def location():
        locationurl = "https://www.google.co.in/maps/place/"
        print("specify the place")
        engine.say("Specify the place",'en')
        engine.runAndWait()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.5)  
            placeaudio = r.listen(source)
            placename = r.recognize_google(placeaudio)
        webbrowser.open(locationurl + placename)

def search():
        searchurl = "https://www.google.co.in/search?q="
        print("What to search?")
        engine.say("What to search",'en')
        engine.runAndWait()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.5)  
            searchaudio = r.listen(source)
            searchword = r.recognize_google(searchaudio)
        webbrowser.open(searchurl + searchword)

def read():
        print("Reading Text!")
        engine.say(pyperclip.paste())
        engine.runAndWait()

def music():
        song = random.choice(os.listdir("F:\My music"))
        player = "C:\Program Files\Windows Media Player\wmplayer.exe"
        path = os.path.join("F:\My music",song)
        if(path[-3:] == "mp3"):
            subprocess.call([player,path])
        else:
            music()
                
def sys_info():
        print("OS : " + platform.system())
        print("OS version : " + platform.release())
        print("System name : " + platform.node())
        print("Architecture : " + platform.machine())
        print("Processor : " + platform.processor())
        print("Total Memory : " + str(psutil.virtual_memory().total/(1024**3)))
        print("Available Memory : " + str(psutil.virtual_memory().available/(1024**3)))
        print("Used Memory : " + str(psutil.virtual_memory().used/(1024**3)))
        print("Memory Used : " + str((psutil.virtual_memory().used/(1024**3)/psutil.virtual_memory().used/(1024**3))*100))

def shut_down():
        os.system("shutdown /s /t 1");

def re_start():
        os.system("shutdown /r /t 1");


            
            
        


            



HOST = '192.168.43.116'
PORT = 9999

 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


print ('socket created') 

try:
	s.bind((HOST, PORT))
except socket.error as err:
	print ('Bind Failed, Error Code: ' + str(err[0]) + ', Message: ' + err[1])
	sys.exit()
 
print ('Socket Bind Success!')
 
 
s.listen(10)
print ('Socket is now listening')
 
 
while(True):
        conn,  addr  =  s.accept()
        print ('connect with' + addr[0] + ':'+ str(addr[1]))
        buf = conn.recv(64)  
        command=buf.decode("utf-8")
        print(command)
        
        if "stop" in command:
             exit()
                
        elif "time" in command:
            tell_time()
                
        elif  "date" in command:
            tell_date()
        elif "today" in command:
            tell_day()
        elif "weather" in command:
            tell_weather()
        elif "joke"  in command:
            tell_joke()
        elif "Browser"  in command:
            open_browser()
        elif "news"  in command:
            tell_news()
        elif "speak"  in command:
            speakup()
        elif "location"  in command:
            location()
        elif "search"  in command:
            search()
        elif "read" in command:
            read()
        elif "music" in command:
            music()
        elif "system info" in command:
            sys_info()
        elif "shutdown" in command:
            shut_down()
        elif "restart" in command:
            re_start()
        else:
            print("Sorry Sir, Command not in List")
                
    
                
 
        
s.close()


            

conn = httplib.HTTPConnection("www.google.com", timeout=5)
try:
        conn.request("HEAD", "/")
        conn.close()
        flag = True
except:
        conn.close()
        flag = False

engine  = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

command = ""

if(flag == True):

    while(True):
        
        def tell_time() :
            timenow = time.localtime()
            
            if(timenow[3] > 12):
                hr = timenow[3]-12
                meridium = "PM"
                minute = timenow[4]
                print(hr,":",minute,meridium)
                times = str(hr) + str(minute) + meridium
                engine.say(times,'en')
                engine.runAndWait()
            else:
                hr = timenow[3]
                meridium = "AM"
                minute = timenow[4]
                print(hr,":",minute,meridium)
                times = str(hr) + str(minute) + meridium
                engine.say(times,'en')
                engine.runAndWait()
            
            

        def tell_date() :
            today = date.today()
            print(today.day,"/",today.month,"/",today.year)
            engine.say(today,'en')
            engine.runAndWait()
            

        def tell_day() :
            day = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
            nowday = datetime.today().weekday()
            print(day[nowday])
            engine.say(day[nowday],'en')
            engine.runAndWait()

        def tell_weather() :
            api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
            url = api_address + "Mangalore"
            print("Weather in Mangalore")
            json_data = requests.get(url).json()
            wdata = json_data['weather'][0]['main']
            wdesc = json_data['weather'][0]['description']
            wtemp = json_data['main']['temp']
            print(wtemp-273.15,"C")
            print(wdata)
            print(wdesc)
            talk_word = (wtemp-273.15,"degree celcius with",wdesc)
            engine.say(talk_word,'en')
            engine.runAndWait()


        def tell_joke():
            joke = random.choice(("What type of nails do carpenters hate to hammer? , Finger nails","A patient sobs to his doctor, I feel like a pair of curtain, Doctor says, Well, pull yourself together man","A man got hit hard in the head with a can of 7up, he is alright though, it was a soft drink","Why does the giraffe has such a long neck, because its feet smell really bad"))
            print(joke)
            engine.say(joke,'en')
            engine.runAndWait()

        def open_browser():
            url = "https://google.com/"
            webbrowser.open(url)

        def tell_news():
            f = feedparser.parse("https://timesofindia.indiatimes.com/rssfeedstopstories.cms")
            for newsitem in f['items']:
                call(["notify-send", newsitem['title'],newsitem['summary']])
                break;

        def speakup():
            file = open('test.txt', 'r')
            line = 'sample'
            while (line != '') :
                line = file. readline()
                print (line)
                engine.say(line,'en')
                engine.runAndWait()
            file. close()

        def location():
            locationurl = "https://www.google.co.in/maps/place/"
            print("specify the place")
            engine.say("Specify the place",'en')
            engine.runAndWait()
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.5)  
                placeaudio = r.listen(source)
                placename = r.recognize_google(placeaudio)
            webbrowser.open(locationurl + placename)

        def search():
            searchurl = "https://www.google.co.in/search?source=hp&ei=WXSlWqHpJYKYvQT9npWQBw&q="
            print("What to search?")
            engine.say("What to search",'en')
            engine.runAndWait()
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.5)  
                searchaudio = r.listen(source)
                searchword = r.recognize_google(searchaudio)
            webbrowser.open(searchurl + searchword)

        def read():
            print("Reading Text!")
            engine.say(pyperclip.paste())
            engine.runAndWait()

        def music():
            song = random.choice(os.listdir("F:\My music"))
            player = "C:\Program Files\Windows Media Player\wmplayer.exe"
            path = os.path.join("F:\My music",song)
            if(path[-3:] == "mp3"):
                subprocess.call([player,path])
            else:
                music()
                
        def sys_info():
            print("OS : " + platform.system())
            print("OS version : " + platform.release())
            print("System name : " + platform.node())
            print("Architecture : " + platform.machine())
            print("Processor : " + platform.processor())
            print("Total Memory : " + str(psutil.virtual_memory().total/(1024**3)))
            print("Available Memory : " + str(psutil.virtual_memory().available/(1024**3)))
            print("Used Memory : " + str(psutil.virtual_memory().used/(1024**3)))
            print("Memory Used : " + str((psutil.virtual_memory().used/(1024**3)/psutil.virtual_memory().used/(1024**3))*100))

        def shut_down():
            os.system("shutdown /s /t 1");

        def re_start():
            os.system("shutdown /r /t 1");

            
            
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            
            print("Please wait. Calibrating microphone...")  
           # listen for 1 seconds and create the ambient noise energy level  
            r.adjust_for_ambient_noise(source, duration=0.5)  
            print("Say something!")
            audio = r.listen(source)
            
           
         # recognize speech using Google API
        try:
            command =  r.recognize_google(audio)
            print("You said "+ command)
            engine.say(command,'en')
            engine.runAndWait()

            if "stop" in command:
                exit()
            elif "time" in command:
                tell_time()
            elif  "date" in command:
                tell_date()
            elif "today" in command:
                tell_day()
            elif "weather" in command:
                tell_weather()
            elif "joke"  in command:
                tell_joke()
            elif "Browser"  in command:
                open_browser()
            elif "news"  in command:
                tell_news()
            elif "speak"  in command:
                speakup()
            elif "location"  in command:
                location()
            elif "search"  in command:
                search()
            elif "read" in command:
                read()
            elif "music" in command:
                music()
            elif "system info" in command:
                sys_info()
            elif "shutdown" in command:
                shut_down()
            elif "restart" in command:
                re_start()
            else:
                print("Sorry Sir, Command not in List")
                engine.say("Sorry Sir, Command not in List",'en')
                engine.runAndWait()
                
        except sr.UnknownValueError:  
           print("Could not understand audio")
           engine.say("Sorry Sir",'en')
           engine.runAndWait()
        except sr.RequestError as e:  
           print("error; {0}".format(e))

else:
    
    print("Switching to Offline mode, Internet Not Available")
    engine.say("Switching to Offline mode",'en')
    engine.runAndWait()
        
    while(command != "Stop" or "stop"):
        
        def tell_time() :
            timenow = time.localtime()
            
            if(timenow[3] > 12):
                    hour = timenow[3]-12
                    meridium = "PM"
            else:
                    meridium = "AM"
            minute = timenow[4]
            print(hour ,":",minute,meridium)
            telltime = str(hour) + str(minute) + meridium
            engine.say(telltime,'en')
            engine.runAndWait()
            

        def tell_date() :
            today = date.today()
            print(today.day,"/",today.month,"/",today.year)
            engine.say(today,'en')
            engine.runAndWait()
            

        def tell_day() :
            day = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
            nowday = datetime.today().weekday()
            print(day[nowday])
            engine.say(day[nowday],'en')
            engine.runAndWait()


        def tell_joke():
            joke = random.choice(("Akshay is handsome !!","Anvitha is intelligent !!","Jayasooryan is a good boy :p ","Arjun code well !!"))
            print(joke)
            engine.say(joke,'en')
            engine.runAndWait()

        def speakup():
            file = open('test.txt', 'r')
            line = 'sample'
            while (line != '') :
                line = file. readline()
                print (line)
                #speak.Speak(line)
                engine.say(line,'en')
                engine.runAndWait()
            file. close()

        def read():
            print("Reading Text!")
            engine.say(pyperclip.paste())
            engine.runAndWait()


            
            
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            
            print("Please wait. Calibrating microphone...")  
           # listen for 1 seconds and create the ambient noise energy level  
            r.adjust_for_ambient_noise(source, duration=1)  
            print("Say something!")  
            audio = r.listen(source)  
           
         # recognize speech using Google API
        try:
            command =  r.recognize_sphinx(audio) 
            print("You said "+ command)
            engine.say(command,'en')
            engine.runAndWait()

            if "stop" in command:
                exit()
                
            elif "time" in command:
                tell_time()
                
            elif  "date" in command:
                tell_date()
                
            elif "today" in command:
                tell_day()
                
            elif "weather" in command:
                print("Sorry Sir, Internet is not available")
                engine.say("Sorry Sir, Internet is not available",'en')
                engine.runAndWait()
                
            elif "joke"  in command:
                tell_joke()
                
            elif "Browser"  in command:
                print("Sorry Sir, Internet is not available")
                engine.say("Sorry Sir, Internet is not available",'en')
                engine.runAndWait()
                
            elif "news"  in command:
                print("Sorry Sir, Internet is not available")
                engine.say("Sorry Sir, Internet is not available",'en')
                engine.runAndWait()
                
            elif "speak"  in command:
                speakup()
                
            elif "location"  in command:
                print("Sorry Sir, Internet is not available")
                engine.say("Sorry Sir, Internet is not available",'en')
                engine.runAndWait()
                
            elif "search"  in command:
                print("Sorry Sir, Internet is not available")
                engine.say("Sorry Sir, Internet is not available",'en')
                engine.runAndWait()
                
            elif "read" in command:
                read()
                
        except sr.UnknownValueError:  
           print("Could not understand audio")
           engine.say("Sorry Sir",'en')
           engine.runAndWait()
           
        except sr.RequestError as e:  
          print("error; {0}".format(e))
