from tkinter import Tk, Label, Entry, Button, filedialog
from pytube import YouTube
import speech_recognition as sr
import webbrowser
from pywikihow import search_wikihow
import pywhatkit
import wikipedia
from googletrans import Translator
import os
import pyautogui
import psutil
from tkinter import Label, Entry, Button, Tk, StringVar
from gtts import gTTS
import PyPDF2
import datetime
import keyboard
import pyjokes
import webbrowser
import wikipedia as google_scrap
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import requests
from playsound import playsound
from fpdf import FPDF 
from bs4 import BeautifulSoup
import webbrowser
import smtplib
import platform
import subprocess
import time
import wolframalpha
import requests
import listener
#engine = pyttsx3.init('sapi5')
#voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[1].id)
#engine.setProperty('rate', 170)

engine = pyttsx3.init('sapi5')  # Initialize the TTS engine with the 'sapi5' driver
voices = engine.getProperty('voices')

# Check if there are available voices and set the voice property
if voices:
    engine.setProperty('voice', voices[0].id)  # Assuming the first voice is available
else:
    print("No voices available")

engine.setProperty('rate', 170)  # Set the speech rate to 170 words per minute
#listener = sr.Recognizer()
#engine = pyttsx3.init()
#voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[1].id)

def speak(audio):
    print(f"Jarvis: {audio}")
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except:
        return "None"

    return query.lower()


def create_todo_list():
    todo_list = []  # Initialize an empty to-do list

    try:
        speak("You can add tasks to your to-do list one by one. When you're done, say 'finish' to generate a PDF.")
        while True:
            with sr.Microphone() as source:
                print('Listening for task...')
                voice = listener.listen(source)
                print('Recognizing...')

                task = listener.recognize_google(voice).lower()
                print('You added:', task)

                if 'finish' in task:
                    if todo_list:
                        create_pdf(todo_list)
                        speak("Your to-do list is ready as a PDF. Is there anything else I can do for you?")
                    else:
                        speak("Your to-do list is empty. Is there anything else I can do for you?")
                    break  # Exit the loop
                else:
                    todo_list.append(task)  # Add the task to the to-do list
                    speak("Task added. You can continue adding more tasks.")

    except sr.UnknownValueError:
        speak("I couldn't understand your request. Please try again.")
    except sr.RequestError as e:
        speak(f"I couldn't request results; {e}")

def create_pdf(todo_list):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="To-Do List", ln=True, align="C")
    pdf.ln(10)  # Add a line break

    for task in todo_list:
        pdf.multi_cell(0, 10, task, align="L")
        pdf.ln()

    pdf_file = "to_do_list.pdf"
    pdf.output(pdf_file)
    os.system(f"start {pdf_file}")  # Open the PDF file
    
def translate_hindi_to_english(hindi_text):
    translator = Translator()
    translation = translator.translate(hindi_text, src='hi', dest='en')
    return translation.text

# Example usage:import speech_recognition as sr
from googletrans import Translator

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak in Hindi:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        hindi_text = recognizer.recognize_google(audio, language='hi-IN')
        return hindi_text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return None
    except sr.RequestError as e:
        print(f"Error with the speech recognition service; {e}")
        return None

def translate_hindi_to_english(hindi_text):
    translator = Translator()
    translation = translator.translate(hindi_text, src='hi', dest='en')
    return translation.text


def create_shopping_list():
    sh_list = []  # Initialize an empty to-do list

    try:
        speak("You can add items to your shopping list one by one. When you're done, say 'finish' to generate a PDF.")
        while True:
            with sr.Microphone() as source:
                print('Listening for task...')
                voice = listener.listen(source)
                print('Recognizing...')

                task = listener.recognize_google(voice).lower()
                print('You added:', task)

                if 'finish' in task:
                    if sh_list:
                        createnew_pdf(sh_list)
                        speak("Your Shopping list is ready as a PDF. Is there anything else I can do for you?")
                    else:
                        speak("Your Shopping list is empty. Is there anything else I can do for you?")
                    break  # Exit the loop
                else:
                    sh_list.append(task)  # Add the task to the to-do list
                    speak("Item added. You can continue adding more tasks.")

    except sr.UnknownValueError:
        speak("I couldn't understand your request. Please try again.")
    except sr.RequestError as e:
        speak(f"I couldn't request results; {e}")


def createnew_pdf(sh_list):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="To-Do List", ln=True, align="C")
    pdf.ln(10)  # Add a line break

    for task in sh_list:
        pdf.multi_cell(0, 10, task, align="L")
        pdf.ln()

    pdf_file = "Shopping_List.pdf"
    pdf.output(pdf_file)
    os.system(f"start {pdf_file}")  # Open the PDF file
    
    

def notes_list():
    n_list = []  # Initialize an empty to-do list

    try:
        speak("You can add note. When you're done, say 'finish' to generate a PDF.")
        while True:
            with sr.Microphone() as source:
                print('Listening for task...')
                voice = listener.listen(source)
                print('Recognizing...')

                task = listener.recognize_google(voice).lower()
                print('You added:', task)

                if 'finish' in task:
                    if n_list:
                        createn_pdf(n_list)
                        speak("Your Notes are ready as a PDF. Is there anything else I can do for you?")
                    else:
                        speak("Your Note is empty. Is there anything else I can do for you?")
                    break  # Exit the loop
                else:
                    n_list.append(task)  # Add the task to the to-do list
                    speak("Note added. You can continue adding more notes.")

    except sr.UnknownValueError:
        speak("I couldn't understand your request. Please try again.")
    except sr.RequestError as e:
        speak(f"I couldn't request results; {e}")
def takeCommand():
    #It takes microphone input from the user and returns string output

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
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def createn_pdf(n_list):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="To-Do List", ln=True, align="C")
    pdf.ln(10)  # Add a line break

    for task in n_list:
        pdf.multi_cell(0, 10, task, align="L")
        pdf.ln()

    pdf_file = "Notes.pdf"
    pdf.output(pdf_file)
    os.system(f"start {pdf_file}")  # Open the PDF file
def music():
    speak("Tell me the name of the song!")
    music_name = take_command()
    pywhatkit.playonyt(music_name)
    speak("Your song has been started! Enjoy, sir!")




def youtube_auto():
    speak("What's your command?")
    comm = take_command()

    if 'pause' in comm:
        keyboard.press('space bar')
    elif 'restart' in comm:
        keyboard.press('0')
    elif 'mute' in comm:
        keyboard.press('m')
    elif 'skip' in comm:
        keyboard.press('l')
    elif 'back' in comm:
        keyboard.press('j')
    elif 'full screen' in comm:
        keyboard.press('f')
    elif 'film mode' in comm:
        keyboard.press('t')
    speak("Done, sir")


def take_hindi():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        command.pause_threshold = 1
        audio = command.listen(source)

    try:
        print("Recognizing.....")
        query = command.recognize_google(audio, language='hi')
        print(f"You said: {query}")

    except:
        return "none"

    return query.lower()


def translator():
    speak("Tell me the line!")
    line = take_hindi()
    translate = Translator()
    result = translate.translate(line)
    text = result.text
    speak(text)

def sleep_system():
    system_platform = platform.system().lower()

    if system_platform == "windows":
        # For Windows
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    elif system_platform == "linux" or system_platform == "darwin":
        # For Linux and macOS
        subprocess.run(["sudo", "pmset", "sleepnow"])
    else:
        print(f"Sleep not supported on {system_platform}.")

def chrome_auto():
    speak("Chrome Automation started!")

    command = take_command()

    if 'close this tab' in command:
        keyboard.press_and_release('ctrl + w')
    elif 'open new tab' in command:
        keyboard.press_and_release('ctrl + t')
    elif 'open new window' in command:
        keyboard.press_and_release('ctrl + n')
    elif 'history' in command:
        keyboard.press_and_release('ctrl +h')
    # Add more functions as needed...

def close_apps(query):
    speak("Ok Sir, Wait a second!")

    if 'youtube' in query:
        os.system("TASKKILL /F /IM chrome.exe")

    elif 'chrome' in query:
        os.system("TASKKILL /F /IM chrome.exe")

    elif 'telegram' in query:
        os.system("TASKKILL /F /IM Telegram.exe")

    elif 'code' in query:
        os.system("TASKKILL /F /IM code.exe")

    elif 'instagram' in query:
        os.system("TASKKILL /F /IM chrome.exe")

    speak("Your command has been successfully completed!")

def play_alarm():
    system_platform = platform.system().lower()

    if system_platform == "windows":
        # For Windows
        import winsound
        frequency = 2500  # Set frequency to 2500 Hertz
        duration = 1000  # Set duration to 1000 milliseconds (1 second)
        winsound.Beep(frequency, duration)
    elif system_platform == "linux" or system_platform == "darwin":
        # For Linux and macOS (requires the 'pygame' library)
        try:
            import pygame
            pygame.mixer.init()
            pygame.mixer.music.load("path_to_alarm_sound_file.mp3")  # Replace with the actual path
            pygame.mixer.music.play()
            time.sleep(5)  # Adjust the sleep duration as needed
            pygame.mixer.music.stop()
        except ImportError:
            print("pygame module not installed. Install it using 'pip install pygame'.")
    else:
        print(f"Alarm not supported on {system_platform}.")

def get_time_from_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please say the time for the alarm (e.g., 'Set alarm for 7:30'):")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        time_str = recognizer.recognize_google(audio)
        return time_str
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the time.")
        return None
    except sr.RequestError as e:
        print(f"Error with the speech recognition service; {e}")
        return None

def get_period_from_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Is it in the morning or evening? (Say 'morning' or 'evening'):")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        period = recognizer.recognize_google(audio).lower()
        if period in ['morning', 'evening']:
            return period
        else:
            print("Please say 'morning' or 'evening'.")
            return None
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the period.")
        return None
    except sr.RequestError as e:
        print(f"Error with the speech recognition service; {e}")
        return None

def set_alarm():
    time_str = get_time_from_speech()

    if time_str:
        # Extract hour and minute from the time string
        try:
            alarm_time_obj = datetime.datetime.strptime(time_str, "%I:%M")
        except ValueError:
            print("Invalid time format. Please try again.")
            return

        period = None
        while period not in ['morning', 'evening']:
            period = get_period_from_speech()

        # Adjust the time based on the period
        if period == 'evening' and alarm_time_obj.hour < 12:
            alarm_time_obj = alarm_time_obj.replace(hour=alarm_time_obj.hour + 12)

        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print(f"Setting alarm for {alarm_time_obj.strftime('%I:%M %p')}. Current time is {current_time}.")
        speak(f"Setting an alarm for {alarm_time_obj.strftime('%I:%M %p')}. Get ready!")

        while True:
            now = datetime.datetime.now().strftime("%I:%M %p")
            if now == alarm_time_obj.strftime("%I:%M %p"):
                print("Time's up! Playing alarm.")
                speak("Time's up! Playing alarm.")
                play_alarm()
                break
            time.sleep(1)


def screenshot():
    speak("OK Boss, what should I name that file?")
    file_name = take_command()
    file_name_with_extension = file_name + ".png"
    
    # Remove spaces from the path and concatenate
    base_path = "C:\\Users\\Dell\\OneDrive\\Desktop\\Pro\\screenshot"
    screenshot_path = os.path.join(base_path.replace(" ", ""), file_name_with_extension)
    
    screenshot_image = pyautogui.screenshot()
    screenshot_image.save(screenshot_path)
    
    os.startfile(base_path)
    
    speak("Here is your screenshot")
def Temp():
    search = "temperature in delhi"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temperature = data.find("div", class_="BNeawe").text
    speak(f"The Temperature Outside Is {temperature} Celsius")

def temp_new():
    speak("Tell Me The Name Of the Place")
    name = take_command()
    search = f"temperature in {name}"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temperature = data.find("div", class_="BNeawe").text
    speak(f"The Temperature in {name} is {temperature} Celsius")
def choose_directory():
    directory_path = filedialog.askdirectory()
    folder_path.delete(0, 'end')
    folder_path.insert(0, directory_path)

def download_video():
    video_url = link.get()
    directory = folder_path.get()

    try:
        yt = YouTube(video_url)
        stream = yt.streams.first()
        stream.download(directory)
        status_label.config(text="Downloaded")
    except Exception as e:
        status_label.config(text="Download failed")

root = Tk()
root.geometry('500x350')
root.resizable(0, 0)
root.title("YouTube Video Downloader")

Label(root, text="YouTube Video Downloader", font='arial 15 bold').pack()

link = Entry(root, width=70)
link.place(x=32, y=90)

folder_path = Entry(root, width=40)
folder_path.place(x=32, y=150)

browse_button = Button(root, text="Browse", font='arial 10', command=choose_directory)
browse_button.place(x=320, y=145)

download_button = Button(root, text="Download", font='arial 15 bold', bg='pale violet red', padx=2, command=download_video)
download_button.place(x=180, y=210)

status_label = Label(root, text="", font='arial 15')
status_label.place(x=180, y=270)

root.mainloop()


# def VideoDownloader():
# 	    url = YouTube(str(link.get()))
# 	    video = url.streams.first()
# 	    video.download()
# 	    Label(root,text = "Downloaded",font = 'arial 15').place(x= 180,y=210)
	

# 	    Button(root,text = "Download",font = 'arial 15 bold',bg = 'pale violet red',padx = 2 , command = VideoDownloader).place(x=180,y=150)
	

# 	    root.mainloop()
# 	    speak("Video Downloaded")

def remember():
    speak("tell me the thing you want to remember")
    query=take_command()
    remember_msg = query.replace("remember that", "")
    remember_msg = remember_msg.replace("jarvis", "")
    speak("You told me to remind you that: " + remember_msg)
    remember_file = open('data.txt', 'w')
    remember_file.write(remember_msg)
    remember_file.close()

def recall_memory():
    remember_file = open('data.txt', 'r')
    speak("You told me that" + remember_file.read())

def wake_up_jarvis():
    recognizer = sr.Recognizer()

    print("Listening for wake-up phrase...")
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        wake_up_phrase = recognizer.recognize_google(audio).lower()
        print(f"Recognized: {wake_up_phrase}")

        if "jarvis" in wake_up_phrase:
            print("Jarvis is awake!")
            # Add your additional wake-up logic here
        else:
            print("Wake-up phrase not recognized.")

    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Error connecting to Google Speech Recognition service: {e}")

# Example usage:
# After calling sleep_system(), you can call wake_up_jarvis() to wake Jarvis up.

# Uncomment the line below to test the wake-up function
# wake_up_jarvis()

def close_browser():
    pyautogui.hotkey('ctrl', 'w')  # Close the current tab using Ctrl + W
def launch_website():
    speak("Sure, launching website. Please specify the website.")
    website_query = take_command()
    
    if website_query:
        website_url = f"https://www.{website_query}.com"
        webbrowser.open(website_url)
        speak(f"Launched {website_query} website.")
    else:
        speak("Sorry, I didn't catch the website name. Please try again.")

def task_execution():
    while True:
        query = take_command()

        if 'hello' in query:
            speak("Hello sir, I am Jarvis.")
            speak("Your personal AI Assistant!")
            speak("How may I help you?")
        elif 'how are you' in query:
            speak("I am fine, sir. What about you?")
        elif 'exit' in query:
            speak("Exiting Jarvis. Goodbye!")
            break
        
        elif 'download video' in query:
            def choose_directory():
                directory_path = filedialog.askdirectory()
                folder_path.delete(0, 'end')
                folder_path.insert(0, directory_path)
            def download_video():
                video_url = link.get()
                directory = folder_path.get()

                try:
                    yt = YouTube(video_url)
                    stream = yt.streams.first()
                    stream.download(directory)
                    status_label.config(text="Downloaded")
                except Exception as e:
                    status_label.config(text="Download failed")

            root = Tk()
            root.geometry('500x350')
            root.resizable(0, 0)
            root.title("YouTube Video Downloader")

            Label(root, text="YouTube Video Downloader", font='arial 15 bold').pack()

            link = Entry(root, width=70)
            link.place(x=32, y=90)

            folder_path = Entry(root, width=40)
            folder_path.place(x=32, y=150)

            browse_button = Button(root, text="Browse", font='arial 10', command=choose_directory)
            browse_button.place(x=320, y=145)

            download_button = Button(root, text="Download", font='arial 15 bold', bg='pale violet red', padx=2, command=download_video)
            download_button.place(x=180, y=210)

            status_label = Label(root, text="", font='arial 15')
            status_label.place(x=180, y=270)

            root.mainloop()


        elif 'remember' in query:
            remember()
        elif 'recall reminders' in query:
            recall_memory()
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'close google' in query:
            close_browser()
            speak("Closed Instagram.")
        elif 'screenshot' in query:
            screenshot()
        elif 'wake up' in query:
            wake_up_jarvis()
        elif 'music' in query:
            music()
        elif 'youtube auto' in query:
            youtube_auto()
        elif 'launch website' in query:
            launch_website()
        elif 'take hindi' in query:
            take_hindi()
        elif 'translator' in query:
            translator()
        elif 'chrome auto' in query:
            chrome_auto()
        elif 'screenshot' in query:
            screenshot()
        elif 'recall memory' in query:
            recall_memory()
        if 'mute' in query:
            keyboard.press('m')
        elif 'restart' in query:
            keyboard.press('0')
        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'youtube tool' in query:
            youtube_auto()
        elif 'chrome tool' in query:
            chrome_auto()

        elif 'close the tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')
        elif 'search in google' in query:
            search_query = query.replace('search google', '')
            speak('Searching Google for ' + search_query)
    
    # Use webbrowser to perform a Google search
            google_search_url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(google_search_url)
        elif 'my location' in query:
            speak("Ok Sir, Wait A Second!")
            webbrowser.open('https://www.google.com/maps/@28.7091225,77.2749958,15z')
        elif 'how to' in query:
            speak("Getting Data From The Internet!")
            op = query.replace("jarvis", "")
            max_result = 1
            how_to_func = search_wikihow(op, max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            speak(how_to_func[0].summary)
        elif 'search in youtube' in query:
            search_query = query.replace('search youtube', '')
            speak('Searching YouTube for ' + search_query)
    
    # Use webbrowser to perform a YouTube search
            youtube_search_url = f"https://www.youtube.com/results?search_query={search_query}"
            webbrowser.open(youtube_search_url)
        elif 'time' in query:
            now = datetime.datetime.now()
            current_time = now.strftime("%I:%M:%p")
            print("Current Time is", current_time)
            speak("The current time is " + current_time) 
        
        elif 'shutdown' in query:
            speak("Shutting down the system. Goodbye!")
            os.system("shutdown /s /t 1")
        elif 'sleep' in query:
            sleep_system()
        elif 'switch off' in query:
            speak("Closing the voice assistant. Goodbye!")
            return False  # Set the flag to False to exit the program
        elif 'alarm'in query:
            set_alarm()

        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")
        elif "open calculator" in query:
            def wolfram_alpha_query(app_id, query):
                client = wolframalpha.Client(app_id)
                res = client.query(query)
                try:
                    answer = next(res.results).text
                    return answer
        
                except StopIteration:
                    return "No results found."

            def recognize_speech():
                recognizer = sr.Recognizer()

                with sr.Microphone() as source:
                    print("Speak your math question:")
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source)

                try:
                    question = recognizer.recognize_google(audio)
                    print(f"Recognized question: {question}")
                    return question
                except sr.UnknownValueError:
                    print("Sorry, I couldn't understand the question.")
                    return None
                except sr.RequestError as e:
                    print(f"Error with the speech recognition service; {e}")
                    return None

# Replace 'YOUR_WOLFRAM_ALPHA_APP_ID' with your actual Wolfram Alpha API key
            app_id = 'YYT3LQ-QP67YE34WV'

# Example usage: Get the result for a math question
            question = recognize_speech()

            if question is not None:
                result = wolfram_alpha_query(app_id, question)
                print(f"Result: {result}")
            else:
                print("No question provided.")
        elif 'alarm' in query:
            set_alarm()
        elif 'close maps' in query:
            close_browser()
            speak("Closed Maps.")
	
        elif 'temperature' in query:
            Temp()
        elif 'another cities weather' in query:
            temp_new()
        elif 'translator' in query:
            translator()
        elif 'translater' in query:
            translator()
        elif 'how to' in query:
            speak("Getting Data From The Internet !")
            op = query.replace("jarvis","")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            speak(how_to_func[0].summary)
        elif 'hindi to english' in query:
            def translate_hindi_to_english(hindi_text):
                translator = Translator()
                translation = translator.translate(hindi_text, src='hi', dest='en')
                return translation.text



            def recognize_speech():
                recognizer = sr.Recognizer()

                with sr.Microphone() as source:
                    print("Speak in Hindi:")
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source)

                try:
                    hindi_text = recognizer.recognize_google(audio, language='hi-IN')
                    return hindi_text
                except sr.UnknownValueError:
                    print("Sorry, I couldn't understand.")
                    return None
                except sr.RequestError as e:
                    print(f"Error with the speech recognition service; {e}")
                    return None

            def translate_hindi_to_english(hindi_text):
                translator = Translator()
                translation = translator.translate(hindi_text, src='hi', dest='en')
                return translation.text

            hindi_text = recognize_speech()
            if hindi_text:
                translated_text = translate_hindi_to_english(hindi_text)
                print(f"Translated: {translated_text}")
                speak(translated_text)
        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com/')
        elif 'DIY' in query:
            class DIYAssistant:
                def __init__(self):
                    self.projects = {
                        "chatbot development": ["Define the purpose and scope of your chatbot.",
                                   "Choose a platform or framework for development (e.g., Python with NLTK or spaCy).",
                                   "Design the conversation flow and user interactions.",
                                   "Implement natural language processing (NLP) for understanding user input.",
                                   "Integrate with a chat platform or create a standalone chat interface.",
                                   "Test the chatbot with various inputs and refine its responses.",
                                   "Deploy the chatbot for public or internal use.",
                                   "Continuously improve the chatbot based on user feedback."],
                        "virtual assistant": ["Define the functionalities and services your virtual assistant will provide.",
                                   "Choose a suitable voice recognition library or API.",
                                   "Implement speech-to-text and text-to-speech functionality for voice interaction.",
                                   "Integrate with external APIs for weather updates, news, and other information.",
                                   "Design a conversation flow and handle user queries effectively.",
                                   "Test the virtual assistant with various voice commands.",
                                   "Deploy the virtual assistant on a platform of your choice (e.g., desktop, mobile, smart speaker).",
                                   "Continuously update and improve the virtual assistant based on user feedback."],
                        "spam email classifier": ["Collect and preprocess a dataset of labeled emails (spam and non-spam).",
                                    "Extract features from the email text (e.g., TF-IDF vectors).",
                                    "Split the dataset into training and testing sets.",
                                    "Train a machine learning model (e.g., Naive Bayes, SVM) on the training set.",
                                    "Evaluate the model on the testing set to measure its accuracy.",
                                    "Integrate the classifier into an email system or create a standalone tool.",
                                    "Test the classifier with new emails and refine its performance.",
                                    "Explore additional techniques for improving spam detection."],
                        "stock price prediction": ["Gather historical stock price data for a specific company.",
                                    "Preprocess the data, including handling missing values and scaling features.",
                                    "Split the data into training and testing sets.",
                                    "Choose a machine learning model suitable for time-series prediction (e.g., LSTM, ARIMA).",
                                    "Train the model on the training set and fine-tune hyperparameters.",
                                    "Evaluate the model's performance on the testing set.",
                                    "Implement a simple user interface to input new data and get predictions.",
                                    "Explore alternative models or features for improving predictions."],
                        "autonomous robot navigation": ["Build a small robot platform with sensors (e.g., ultrasonic, infrared).",
                                    "Implement obstacle avoidance algorithms for navigation.",
                                    "Integrate sensors with a microcontroller or Raspberry Pi.",
                                    "Program the robot to navigate autonomously in a controlled environment.",
                                    "Test the robot's performance and refine the navigation algorithms.",
                                    "Explore additional features like mapping or path planning.",
                                    "Consider using computer vision for more advanced navigation tasks.",
                                    "Document the robot's design and share the project with the community."],
                        "fake news detection": ["Collect a labeled dataset of news articles (real and fake).",
                                   "Preprocess the text data, including tokenization and vectorization.",
                                   "Split the dataset into training and testing sets.",
                                   "Choose and train a machine learning model for text classification.",
                                   "Evaluate the model's performance on the testing set.",
                                   "Implement a simple web interface for users to input news articles.",
                                   "Integrate the fake news detection model to classify articles.",
                                   "Explore additional techniques like deep learning for improved accuracy."],
                        "language translation tool": ["Choose a language translation API or library (e.g., Google Translate, spaCy).",
                                    "Integrate the tool into a web or mobile application.",
                                    "Design a user-friendly interface for users to input text and select languages.",
                                    "Test the translation tool with various phrases and languages.",
                                    "Consider adding additional features like pronunciation or cultural nuances.",
                                    "Optimize the translation tool for speed and accuracy.",
                                    "Seek feedback from users to identify areas for improvement.",
                                    "Explore multilingual and bidirectional translation capabilities."],
            # Add more DIY projects as needed
        }
                    
                    self.tts_engine = pyttsx3.init()

                def get_diy_project(self, project_name):
                    return self.projects.get(project_name.lower())

                def get_random_project(self):
                    project_name = random.choice(list(self.projects.keys()))
                    return project_name, self.get_diy_project(project_name)

                def speak_and_print(self, text):
        # Use text-to-speech to speak the given text
                    self.tts_engine.say(text)
                    self.tts_engine.runAndWait()

        # Print the text to the console
                    print(text)
            def main():
                diy_assistant = DIYAssistant()

    # Example: Get random step-by-step instructions for a DIY project
                random_project_name, random_project_steps = diy_assistant.get_random_project()

                diy_assistant.speak_and_print(f"Random DIY Project: {random_project_name.capitalize()}")
                for step_number, step in enumerate(random_project_steps, start=1):
                        diy_assistant.speak_and_print(f"Step {step_number}: {step}")

            if __name__ == "__main__":
                main()

        elif 'close youtube' in query:
            close_browser()
            speak("Closed YouTube.")
        elif 'open facebook' in query:
            webbrowser.open('https://www.facebook.com/')
        elif 'close facebook' in query:
            close_browser()
            speak("Closed Facebook.")
        elif 'open instagram' in query:
            webbrowser.open('https://www.instagram.com/')
        elif 'close instagram' in query:
            close_browser()
            speak("Closed Instagram.")        
        elif 'open maps' in query:
	        webbrowser.open('https://www.google.com/maps/@28.7091225,77.2749958,15z')
        




if __name__ == "__main__":
    task_execution()
