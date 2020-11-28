import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import subprocess
import re
import smtplib

speakEngine = pyttsx3.init('sapi5')
ai_Voice = speakEngine.getProperty('voices')
speakEngine.setProperty('voice', ai_Voice[0])

def Speak(commands):
    speakEngine.say(commands)
    speakEngine.runAndWait()


def wishMe():
    time = int(datetime.datetime.now().hour)
    if 0<=time<12:
        print("Good Morning Sir!")
        Speak("Good Morning Sir!")
    elif 12<=time<18:
        print("Good Afternoon Sir!")
        Speak("Good Afternoon Sir!")
    else:
        print("Good Evening Sir!")
        Speak("Good Evening Sir!")
    print("My name is Steve. How can I help you ?")
    Speak("My name is Steve. How can I help you ?")
    print("To stop me you can say 'steve stop'")
    Speak("To stop me you can say 'steve stop'")


def takeCommand():
    """
    This is a command used to give commands to
    the assistant.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening....")
        r.pause_threshold = 1
        user_audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(user_audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        print("\nSay that again please.....\n")
        Speak("Say that again please.....")
        return "None"
    return query


def sendMail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('senders-email-address', 'senders-email-password')
    server.sendmail('senders-email-address', to, content)
    server.close()



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            print('\nSearching Wikipedia...')
            Speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            print(f"According to Wikipedia : {results}")
            Speak(f"According to Wikipedia : {results}")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open spotify' in query:
            subprocess.call('spotify.exe')

        elif 'open google' in query:
            chromePath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            os.startfile(chromePath)

        elif 'open vs code' in query:
            vsPath = "C:\Program Files\Microsoft VS Code\Code.exe"
            os.startfile(vsPath)

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            print("\nOn which app you want to play")
            Speak("On which app you want to play")
            confirm = takeCommand().lower()
            try:
                if 'spotify' in confirm:
                    print("\nOpening Spotify")
                    Speak("Opening Spotify")
                    subprocess.call('spotify.exe')
                else:
                    subprocess.call('groove.exe')
            except Exception as e:
                print("No such application found, try search for something else...")
                Speak("No such application found, try search for something else...")

        elif 'the time' in query:
            today = datetime.datetime.today()
            am_pm_str = ""
            if 0<=today.hour<12:
                am_pm_str = "AM"
            else:
                am_pm_str = "PM"
            print(f"The time is {today.hour//2}:{today.minute} {am_pm_str}\n")
            Speak(f"The time is {today.hour//2}:{today.minute} {am_pm_str}")


        elif 'send mail' in query:
            try:
                print("To whom you would like send a mail ?")
                Speak("To whom you would like send a mail ?")
                mail_id = takeCommand().lower().replace(' ', '')
                print(mail_id)
                find_mail = re.findall(r"[a-zA-Z0-9._+%]+@[a-zA-Z0-9._+%]+[.][a-zA-Z0-9]+", mail_id)
                to = find_mail
                print("What should I say to the receiver ?")
                Speak("What should I say to the receiver ?")
                content = takeCommand()
                sendMail(to, content)
                print("Email has been sent!")
                Speak("Email has been sent!")
            except Exception as e:
                print("Sorry Sir,  something went wrong!")
                Speak("Sorry Sir, something went wrong!")



        elif 'steve stop' in query:
            print("Thank you Sir, for choosing me as your Personal Assistant!")
            Speak("Thank you Sir, for choosing me as your Personal Assistant!")
            break

        elif query != "":
            print("No such thing found. Please try again... !")
            Speak("No such thing found. Please try again... !")
