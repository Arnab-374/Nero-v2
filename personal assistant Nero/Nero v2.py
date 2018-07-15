#Nero version 2 - by Arnab Bindu Laha


#importing the libraries

import pyttsx3
import speech_recognition as sr
import webbrowser


#initializations
talkToMe = pyttsx3.init('sapi5')
talkToMe.setProperty('rate', 140)

#allowing it to speak
def say(text):

    talkToMe.say(text)
    talkToMe.runAndWait()

#initializing the speech identifier
speech_identification = sr.Recognizer()



#enabling it to listen to commands using the microphone
def command():

    with sr.Microphone() as source:
        speech_identification.adjust_for_ambient_noise(source)
        audio = speech_identification.listen(source)


    try:
        return speech_identification.recognize_google(audio)

    except sr.UnknownValueError:
        print("I'm waiting for your next request.")


    return ""


#setting up the wiki search parameters


#initializing the if else statements for different operations

say("Welcome!")
say("My name is Nero, I am here to help you.")
say("What can i do for you?")

print("\n# Start speaking to Nero.")

while 1:

    str = command()

    print(str)

    if str == "hello" or str == "hi" or str == "hey":
        print("hello sir\n")
        say("hello sir")

    elif str == "nero are you there" or str == "are you there":
        print("yes sir, i am here")
        say("yes sir i am here")

    elif str == "what's up" or str == "what up":
        print("Chillin sir.")
        say("Chilling sir.")

    elif str == "nero are you listening" or str == "are you listening":
        print("yes sir i am always listening")
        say("yes sir i am always listening")

    elif str == "open Reddit python" or str == "reddit python":
        #chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        #url = 'https://www.redit.com/r/python'
        #webbrowser.get(chrome_path).open(url)
        webbrowser.open_new('https://www.redit.com/r/python')

    elif str == "open stackoverflow":
        #chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        #url = 'https://stackoverflow.com/'
        #webbrowser.get(chrome_path).open(url)
        webbrowser.open_new('https://stackoverflow.com/')

    elif str == "open youtube" or str == "open YouTube":
        webbrowser.open_new_tab('https://www.youtube.com/')

