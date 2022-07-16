#Import dependencies
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
from random import randint
from zope.interface import Interface, implements, implementer

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#Declare class User to set up CARA using username, password, id and security code
class User:
        def __init__(self,username,password,cara_id,security_code):
                self.security_code=security_code
                self.password=password
                self.username=username
                self.cara_id=cara_id

#Declare CaraApp to enable voice input
class CaraApp:
    def enableVoiceInput(self):
    
        query=SoundSystem.takeCommand(self)
        return query.lower()
    
#Declare UserInterface to initialize voice input
class UserInterface:
    def wishMe(self):
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
                SoundSystem.speak(self,"Good Morning!")
        elif hour>=12 and hour<18:
                SoundSystem.speak(self,"Good Afternoon!")   
        else:
                SoundSystem.speak(self,"Good Evening!")  
        SoundSystem.speak(self,"I am Cara. Please tell me how may I help you")  

#Declare WebServer for web search related queries    
class WebServer:

        def search_web(self,query):
            if 'wikipedia' in query:
                SoundSystem.speak(self,'Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                SoundSystem.speak(self,"According to Wikipedia")
                print(results)
                SoundSystem.speak(self,results)

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open stack overflow' in query:
                webbrowser.open("stackoverflow.com")  

            elif 'open geeksforgeeks' in query:
                webbrowser.open("geeksforgeeks.org") 
        
            elif 'open facebook' in query:
                webbrowser.open("facebook.com") 

            elif 'open twitter' in query:
                webbrowser.open("twitter.com") 

        def sendEmail(self,to, content):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login('youremail@gmail.com', 'your-password')
            server.sendmail('youremail@gmail.com', to, content)
            server.close()

        def map_queries(self,query):
                x=query.split()
                location = x[1]
                print(location)
                webbrowser.open("https://www.google.nl/maps/place/" + location)

        def orderfood(self,query):
                webbrowser.open("swiggy.com")
                
#Declare SoundSystem to take commands from user and recognize
class SoundSystem:

        def takeCommand(self):

            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 1
                audio = r.listen(source)

            try:
                print("Recognizing...")    
                query = r.recognize_google(audio, language='en-in')
                print(f"User said: {query}\n")

            except Exception as e:   
                print("Say that again please...")  
                return "None"

            return query
 
        def speak(self,audio):
            engine.say(audio)
            engine.runAndWait()
            
#Declare Operation to set up cara device and reset function
class Operation:
        cara_id=0
        security_code=0

        def setDevice(self,cara_id,security_code):
            self.security_code=int(security_code)
            self.cara_id=int(cara_id)
            print("The device is set up")
        
        def resetDevice(self,cara_id,security_code):
            cara_id=0
            security_code=0
            print("The device is resetted")

#Declare PlayMedia to play music and video
class PlayMedia(Operation):
        def playMusic(self,query):
            music_dir = r"C:\Users\Kannan-PC\Videos\example.mp3"
            songs = os.listdir(music_dir)   
            os.startfile(os.path.join(music_dir, songs[randint(0,30)]))

        def playVideo(self,query):
            video_dir=r"C:\Users\Kannan-PC\Music\example.mp4"
            os.startfile(video_dir)
            
#Create interface Home Automation
class Home_Automation(Interface):
    def __init__(self,device_id,state):
        self.device_id=device_id
        self.state=state

    def enable_device(self,device_id):
        pass

    def disable_device(self,device_id):
        pass
    
#Implement from Home Automation - Device Control - to enable and disable devices
@implementer(Home_Automation)
class Device_Control:
    def __init__(self,device_id,state):
        self.device_id=device_id
        self.state=state

    def enable_device(self,device_id):
        self.state="ON"
        SoundSystem.speak(self,"Switched On")

    def disable_device(self,device_id):
        self.state="OFF"
        SoundSystem.speak(self,"Switched Off")
        
#Implement from Home Automation - Security_System - to enable and disable security system
@implementer(Home_Automation)
class Security_System:
    def __init__(self,device_id,state):
        self.device_id=device_id
        self.state=state

    def enable_device(self,device_id):
        self.state="ON"
        SoundSystem.speak(self,"Switched On")


    def disable_device(self,device_id):
        self.state="OFF"
        SoundSystem.speak(self,"Switched Off")
        
#Implement from Device Control -TV - change  channel , volume
class TV(Device_Control):
    volume=23
    def change_channel(self,channel_no):
        self.channel_no=channel_no
        SoundSystem.speak(self,"Changing channel")

    def change_volume(self,inc,dec):
        if inc==1:
            self.volume=self.volume+1
        else:
            self.volume=self.volume-1
        
        SoundSystem.speak(self,"Changing volume")
        
    def enable_device(self,device_id):
        self.state="ON"
        SoundSystem.speak(self,"Switched On")


    def disable_device(self,device_id):
        self.state="OFF"
        SoundSystem.speak(self,"Switched Off")

#Implement from Device Control -AC - change  mode , temperature
class AC(Device_Control):
    def changetemp(self,temp):
        self.temp=temp
        SoundSystem.speak(self,"Temperature changed to "+ temp)

    def changemode(self,mode):
        self.mode=mode
        SoundSystem.speak(self,"Mode changed to"+ mode)
    
    def enable_device(self,device_id):
        self.state="ON"
        SoundSystem.speak(self,"Switched on")
    
    def disable_device(self,device_id):
        self.state="OFF"
        SoundSystem.speak(self,"Switched off")

#Implement from Security_System - Fire_Alarm : to monitor, check water level
class Fire_Alarm(Security_System):
    waterlevel_ts=1800
    def checkwaterlevel(self,waterlevel):
        if int(waterlevel) < self.waterlevel_ts:
            SoundSystem.speak(self,"Fill water")
    def monitor(self,temp):
        pass
    def makecall(self,station_no):
        pass
    def spriklewater(self):
        pass
    
#Implement from Fire_Alarm - Emergency - sprinke water
class Emergency(Fire_Alarm):
    def makecall(self,station_no):
        SoundSystem.speak(self,"Make a call to the station.Calling two two two four five one nine seven")

    def spriklewater(self):
        SoundSystem.speak(self,"Sprinkling water")
        
#Implement from Fire_Alarm -Conventional - monitor
class Conventional(Fire_Alarm):
    def monitor(self,temp):
        if int(temp)>30 :
            Emergency.makecall(self,2345112)
            Emergency.spriklewater(self)
            
#Implement from Security_System  - Camera_Control -capture and delete image
class Camera_Control(Security_System):
    def img_capture(self):
        SoundSystem.speak(self,"Capturing")
    def img_delete(self):
        SoundSystem.speak(self,"Deleting")


if __name__ == "__main__":
    while True:
        print( " 1.Setup device \n 2.Create Account \n 3.Input Voice \n 4.Reset Device \n 5.Exit \n" )
        g=input(" Enter your choice ")
       
        if int(g)==1:
        
            secu_code=input("Enter security code \n")
            cara_id=input("Enter cara id \n")
            op=Operation()
            op.setDevice(cara_id,secu_code)    

        elif int(g)==2:
    
            username=input("Enter username \t ")
            password=input("Enter password \t")
            secu_code=input("Enter security code \n")
            cara_id=input("Enter cara id \n")
            u1=User(username,password,secu_code,cara_id)
            print("Account created")

        elif int(g)==3:
            ui=UserInterface()
            ui.wishMe()
            cp=CaraApp()
            ss= SoundSystem()
            ws=WebServer()
            pm=PlayMedia()
            tv1=TV(34,"OFF")
            ac1=AC(43,"OFF")
            con=Conventional(12,"ON")
            fa=Fire_Alarm(12,"ON")
            img=Camera_Control(56,"ON")
            query=cp.enableVoiceInput()
       
            if 'google' in query or  'wikipedia' in query or 'stack overflow' in query  or 'facebook' in query or 'youtube' or 'twitter' or 'geeksforgeeks' in query:
                ws.search_web(query)

            if 'email to jayashree ' in query:
                try:
                    ss.speak("What should I say?")
                    content = ss.takeCommand()
                    to = "jayashreenaveenanj12345@gmail.com"    
                    ws.sendEmail(to, content)
                    ss.speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    ss.speak("Sorry. I am not able to send this email")

            if "order food" in query:
                ws.orderfood(query)

            if 'location' in query:
                ws.map_queries(query)

            if  "play music" in query:
                pm.playMusic(query)
            
            if "play video" in query:
                pm.playVideo(query)
            
            if 'hello' in query or 'hi' in query:
                ss.speak("Hello")
            
            if 'bye' in query:
                ss.speak("Bye, Have a good day")

            if "how are you" in query:
                stMsg = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am doing good']
                ss.speak(random.choice(stMsg))

            if "what is your name" in query:
                ss.speak("I am Cara")
                
            if "open notepad" in query:
                notepad=r"C:\Program Files\windows nt\accessories\wordpad.exe"
                os.startfile(notepad)

            if "switch on tv" in query:
                tv1.enable_device(34)

            if "switch off tv" in query:
                tv1.disable_device(34)

            if "increase volume" in query:
                tv1.change_volume(1,0)

            if "decrease volume" in query:
                tv1.change_volume(0,1)

            if "switch on ac" in query:
                ac1.enable_device(43)
            
            if "switch off ac" in query:
                ac1.disable_device(43)

            if "change mode" in query:
                mode=input("Enter mode")
                ac1.changemode(mode)
            
            if "change temperature" in query:
                temp=input("Enter temperature")
                ac1.changetemp(temp)

            if "monitor" in query:
                temp=input("Get the current temp")
                con.monitor(temp)

            if "check water level" in query:
                water=input("Get the water level")
                fa.checkwaterlevel(water)

            if "take image" in query:
                img.img_capture()

            if "delete image" in query:
                img.img_delete()
            
    
        elif int(g)==4:
            secu_code=input("Enter security code \n")
            cara_id=input("Enter cara id \n")
            op=Operation()
            op.resetDevice(cara_id,secu_code)
        
        elif int(g)==5:
            exit()