from tkinter import *
import pyttsx3
import datetime
import time
from datetime import date
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from Private import private
root=Tk()
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    global scvalue
    r = sr.Recognizer()
    with sr.Microphone() as source:
        scvalue.set('Listening...')
        screen.update()
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        scvalue.set('Recognizing...')
        screen.update()
        query = r.recognize_google(audio, language='en-in')
        scvalue.set(f'{query}\n')
        screen.update()
        time.sleep(3)

    except Exception as e:
        scvalue.set('Say that again please..')
        screen.update()
        time.sleep(2)
        return 'None'
    return query


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morining!')
    elif hour >= 12 and hour <= 15:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')
    speak('Sir, Your desktop assistant is at your service. Please tell me how may I help you')


def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(private.eid,private.password)
    server.sendmail(private.eid,to,content)
    server.close()


def desktopasisstant(event):
    wish()
    while True:
        conscent=''
        query = takeCommand().lower()
        email_dict={'faisal':'faisaliqbal669@gmail.com','dhruv':'dhruv.hbk@gmail.com','hemant':'hemantsharma.1947@gmail.com','nishant':'nkm2277@gmail.com','yash':'yashc845@gmail.com'}
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        
        elif 'open facebook' in query:
            webbrowser.open('facebook.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir = 'F:\\songs\\hindi\\mood'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H hours %M minutes %S seconds')
            speak(f'Sir, the time is{strTime}')

        elif 'the date' in query:
            today=date.today()
            strDate=today.strftime("%B %d %Y")
            speak(f'Sir, todays date is{strDate}')

        elif 'open code' in query:
            codepath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'send email to' in query:
            query=query.replace('send email to ','')
            recepient=email_dict.get(query)
            try:
                speak('what should I say?')
                content=takeCommand()
                scvalue.set(content)
                screen.update
                speak('should I send this?')
                conscent=takeCommand()
                while 'no' in conscent:
                    speak('then what should I say?')
                    content=takeCommand()
                    scvalue.set(content)
                    screen.update
                    speak('should I send this?')
                    conscent=takeCommand()
                    if 'yes' in conscent:
                        break
                    else:
                        pass
                to=recepient
                sendEmail(to,content)
                speak('Email has been sent:')
            except Exception as e:
                print(e)
                speak('Sorry! unable to send email')

        elif 'sleep' in query:
            break
root.title('DesktopAsisstant')
root['bg']='violet'
root.geometry('400x400')
T=Label(root,text='Desktop Assistant',fg='black',bg='sky blue',font='Helvetica 28 bold italic')
T.pack()
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 25")
screen.pack(fill=X,padx=10,pady=20)
root.bind('<Escape>',quit)
f1=Frame(root,bg='red')
b=Button(f1,text='Speak',font='lucida 15 bold',padx=10,pady=10,height=1,width=3)
b.pack(side=LEFT,padx=5)
b.bind('<Button-1>',desktopasisstant)
f1.pack()
root.mainloop()