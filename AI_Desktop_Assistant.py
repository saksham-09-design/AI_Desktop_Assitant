import speech_recognition as sr       
import pyttsx3                        
import webbrowser               
import datetime
import os
import pywhatkit
import json
import pyautogui
import math
import pyjokes
import youtube_dl
import random
import tkinter as tk
import string
import enchant
import random
import requests
from googlesearch import search
import wikipedia
import cv2
import numpy as np
import time
from forex_python.converter import CurrencyRates
from bs4 import BeautifulSoup
import re
from googletrans import Translator
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from List_For_AIDA import *
translator = Translator()
c = CurrencyRates()
engine = pyttsx3.init()   
def speak(message):           
    engine.say(message)        
    engine.runAndWait()
    
def comp_choice():
    comp_c = ['Rock', 'Paper', 'Scissor']
    return(random.choice(comp_c))          

def takeCommand():
    inp = sr.Recognizer()              
    with sr.Microphone() as source:        
        audio = inp.listen(source)         
        try:
            print("Recognizing......")
            query = inp.recognize_google(audio, language = "en-in")
            if "condom" in query.lower():
                query = query.replace("condom","")
                query = query.replace("phantom","")
            print(f"User Said: {query}")
            return query                                        
        except Exception as e:
            return "Some Error Occured Please Try Again."       
def take_picture():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Failed to open camera")
        speak("Failed to open camera")
        exit()
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        speak("Failed to capture frame")
        exit()
    speak("Say Cheese!")
    path = f"C:\\Users\\saksh\\OneDrive\\Documents\\codes\\Python_Projects\\Images_Captuerd_by_AI_Assistant\\{random.randint(1,20000000000000000)}.jpg"
    cv2.imwrite(path, frame)
    cap.release()
    print("Image captured successfully.")
    speak("Image captured successfully")

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Hello, Good Morning Sir, How can I assist you.")
    elif hour>12 and hour<=15:
        speak("Hello, Good Noon Sir, How can I assist you.")
    elif hour>15 and hour<=17:
        speak("Hello, Good Afternoon Sir, How can I assist you.")
    else:
        speak("Hello, Good Evening Sir, How can I assist you.")

def greet_face():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Welcome sir, Good Morning, How can I assist you.")
    elif hour>12 and hour<=15:
        speak("Welcome sir, Good Noon, How can I assist you.")
    elif hour>15 and hour<=17:
        speak("Welcome sir, Good Afternoon, How can I assist you.")
    else:
        speak("Welcome sir, Good Evening, How can I assist you.")

def youtube_download(url):
    ydl_opts = {
        'format': 'bestvideo[height=360]+bestaudio[ext=m4a]',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            speak("Download Started")
            print("Download Started")
            ydl.download([url])
            print("Download complete!")
            speak("Download complete!")
        except Exception as e:
            print("An error occurred:", str(e))

def spellcheck_paragraph_with_suggestions(paragraph):
    dictionary = enchant.Dict("en_US")
    words = paragraph.split()
    corrections = {}
    for word in words:
        if not dictionary.check(word):
            suggestions = dictionary.suggest(word)
            corrections[word] = suggestions
    return corrections

def random_para():
    paragraph_1 = random.choice(paragraphs)
    return paragraph_1

def match(para, inp):
    i = 0
    input_value = inp.split()
    para = para.split()
    para_len = len(para)
    for word in range(min(para_len, len(input_value))):
        if para[word] != input_value[word]:
            i += 1
    return i

def show_result(prompt, para, input_value):
    result_window = tk.Toplevel(root)
    result_window.title("Typing Test Result")

    wpm = len(input_value.split())
    wrong_words = match(para, input_value)
    net_wpm = wpm - wrong_words

    result_text = f"{prompt}\n\n"
    result_text += f"Your Gross Typing Speed: {wpm} WPM\n"
    result_text += f"Your Typed {wrong_words} wrong words\n"
    result_text += f"Your Net Typing Speed: {net_wpm} WPM"

    result_label = tk.Label(result_window, text=result_text, padx=10, pady=10, wraplength=400)
    result_label.pack()

def get_input_with_timeout(prompt, timeout, para_1):
    print(prompt)
    input_value = input_var.get()
    
    if not input_value.strip():  # Check if input is empty
        print("\nNo input received!")
        return

    global stop_typing_test
    stop_typing_test = True
    show_result("Typing Test Result", para_1, input_value)

def get_day_name(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, '%d %B %Y')
        day_name = date_obj.strftime('%A')
        return day_name
    except ValueError as e:
        print(f"Error: {e}")
        return None

def start_typing_test():
    global start_button, input_var, stop_typing_test
    stop_typing_test = False
    para_1 = random_para()
    intro_label.destroy()
    start_button.destroy()
    typing_test_label = tk.Label(root, text="Typing Test", font=("Helvetica", 20))
    typing_test_label.pack(pady=20)
    para_label = tk.Label(root, text=para_1, wraplength=400, font=("Helvetica", 14))
    para_label.pack(pady=20)
    input_var = tk.StringVar()
    input_entry = tk.Entry(root, font=("Helvetica", 12), width=50, textvariable=input_var)
    input_entry.pack(pady=10)
    start_button = tk.Button(root, text="Submit", command=lambda: get_input_with_timeout("Result: ", 60, para_1))
    start_button.pack()
    root.after(60000, get_input_with_timeout, "Timeout!", 0, para_1)

def face_reco():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    camera_radius = 200
    def draw_circular_mask(frame, center, radius):
        mask = np.zeros_like(frame)
        height, width = frame.shape[:2]
        cv2.circle(mask, center, radius, (255, 255, 255), -1)
        masked_frame = cv2.bitwise_and(frame, mask)
        return masked_frame
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Failed to open the camera.")
        return False
    start_time = time.time()
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        frame = draw_circular_mask(frame, (frame.shape[1] // 2, frame.shape[0] // 2), camera_radius)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow('Face Recognition', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if time.time() - start_time > 5:
            if len(faces) > 0:
                cap.release()
                cv2.destroyAllWindows()
                return True
            else:
                cap.release()
                cv2.destroyAllWindows()
                return False

def Stock_Market():
    url_1 = "https://in.investing.com/?ref=www"
    response = requests.get(url_1)
    if response.status_code == 200:
        stock = BeautifulSoup(response.content, 'html.parser')
        stock_a = stock.find_all('tr', class_="common-table-item u-clickable marked")
        speak("Here is the Live Stock Market Status")
        for stock_item in stock_a:
            stock_p = stock_item.find('td', class_="col-last u-txt-align-end")
            if stock_p:
                print(f"NIFTY 50 Points: {stock_p.text.strip()}")
                speak(f"NIFTY 50 Points: {stock_p.text.strip()}")
        try:
            for CHANGE in stock_a:
                change_p = stock_item.find('td', class_="col-chg u-txt-align-end u-down")
                if stock_p:
                    print(f"NIFTY 50 Movement: {change_p.text.strip()}")
                    speak(f"NIFTY 50 Movement: {change_p.text.strip()}")
        except:
            for CHANGE in stock_a:
                change_p = stock_item.find('td', class_="col-chg u-txt-align-end u-up")
                if stock_p:
                    print(f"NIFTY 50 Movement: {change_p.text.strip()}")
                    speak(f"NIFTY 50 Movement: {change_p.text.strip()}")
        BANK_NIFTY = BeautifulSoup(response.content, 'html.parser')
        bse_sen_1 = BANK_NIFTY.find_all('tr', {'data-s': '17950'})
        for bank_nif_50 in bse_sen_1:
            BAN_50 = bank_nif_50.find('td', class_='col-last u-txt-align-end')
            if BAN_50:
                print(f"BANK NIFTY: {BAN_50.text.strip()}")
                speak(f"BANK NIFTY: {BAN_50.text.strip()}")
            ban_nif_50 = bank_nif_50.find('td', class_="col-chg u-txt-align-end u-up")
            if not ban_nif_50:
                ban_nif_50 = bank_nif_50.find('td', class_="col-chg u-txt-align-end u-down")
            if ban_nif_50:
                movement = ban_nif_50.text.strip()
                print(f"BANK NIFTY MOMENT: {movement}")
                speak(f"BANK NIFTY MOMENT: {movement}")
                break
        bse_sen = BeautifulSoup(response.content, 'html.parser')
        bse_sen_1 = bse_sen.find_all('tr', {'data-s': '39929'})
        for stock_bse in bse_sen_1:
            stock_b = stock_bse.find('td', class_='col-last u-txt-align-end')
            if stock_b:
                print(f"BSE SENSEX {stock_b.text.strip()}")
                speak(f"BSE SENSEX {stock_b.text.strip()}")
            movement_elem = stock_bse.find('td', class_="col-chg u-txt-align-end u-up")
            if not movement_elem:
                movement_elem = stock_bse.find('td', class_="col-chg u-txt-align-end u-down")
            if movement_elem:
                movement = movement_elem.text.strip()
                print(f"BSE SENSEX Movement: {movement}")
                speak(f"BSE SENSEX Movement: {movement}")
                break
    else:
        print(f"Error: {response.status_code}")
        speak("Error in Fetching Data")

def leap_year_check(year):
        year = int(year)
        if(year%100==0):
            if(year%400==0):
                print(f"{year} is Leap Year")
                engine.say(f"{year} is Leap Year")
                engine.runAndWait()
                return(True)
            else:
                print(f"{year} is not a Leap Year")
                engine.say(f"{year} is not a Leap Year")
                engine.runAndWait()
                return(False)
        else:
            if(year%4==0):
                print(f"{year} is a Leap Year")
                engine.say(f"{year} is Leap Year")
                engine.runAndWait()
                return(True)
            else:
                print(f"{year} is not a Leap Year")
                engine.say(f"{year} is not a Leap Year")
                engine.runAndWait()
                return(False)

def Micro_rewards():
    pyautogui.press('win')
    pyautogui.sleep(1)
    pyautogui.typewrite('chrome')
    pyautogui.sleep(0.5)
    pyautogui.press('enter')
    pyautogui.sleep(2)
    for a in range(4):
        pyautogui.press('tab')
        pyautogui.sleep(0.1)
    pyautogui.press('enter')
    pyautogui.sleep(2)
    keyword = string.ascii_lowercase
    keyword += string.ascii_uppercase
    keyword = list(keyword)
    i = 0
    for i in range(35):
        pyautogui.click(300,75)
        pyautogui.sleep(0.5)
        pyautogui.typewrite(f"{random.choice(keyword)}{random.choice(keyword)}{random.choice(keyword)}{random.choice(keyword)}")
        pyautogui.press('enter')
        pyautogui.sleep(2)
            
def wiki_search(term):
    query = term
    try:
        info = wikipedia.summary(term,5)
        if info !="":
            speak("Do you Want to Save this Information to file or print on screen or you want to me to explain this and save to file")
            speak("Speak Save to file for saving, Explain me for Explaining you and Print on screen for just printing")
            print("Listning.....")
            user_res = takeCommand()
            if user_res.lower() == "save to file":
                if not os.path.exists("Search_Results"):
                    os.mkdir("Search_Results")
                with open(f"Search_Results\\{term}.txt", "w") as f_1:
                    f_1.write(info)
                speak("Saved to file sir")
            elif user_res.lower() == "explain me":
                speak(info)
            elif user_res.lower() == "print on screen":
                print("Page Summary:")
                print(info)
                speak("Printed Sir")
    except Exception as e:
        print("No Result Found!")
        speak("No Result Found!")

def latest_news():
    url = None
    content = None
    speak("Which Field News Do You Want?")
    print("1. Technology")
    print("2. Entertainment")
    print("3. Business")
    print("4. Science")
    print("5. Health")
    print("6. Sports")
    print("Enter the field news that you want to hear.") 
    speak("Enter the field news that you want to hear.")
    field = input()
    for key,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print("News Found")
            break
        else:
            url = True
    if url == True:
        print("Entered Field is wrong")
    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the Latest news")
    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"To Know More about this Follow This Link: {news_url}.")
        choice_n = input("Enter 1 to Continue the News and 2 to Exit")
        if choice_n == "1":
            pass
        elif choice_n == "2":
            break

def g_search(term):
        query = term
        try:
            search_results = search(query)
            speak("This is what I got from google")
            for result in search_results:
                print(result)
        except Exception as f:
            print("No Result found!")
            speak("No Result Found!")

def alarm(h_1, h_2, m_1, m_2):
    pyautogui.press('win')
    pyautogui.sleep(1)
    pyautogui.typewrite('clock')
    pyautogui.press('enter')
    pyautogui.sleep(4)
    pyautogui.keyDown('alt')
    pyautogui.keyUp('alt')
    pyautogui.press('3')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press(h_1)
    pyautogui.press(h_2)
    pyautogui.press('tab')
    pyautogui.press(m_1)
    pyautogui.press(m_2)
    for i in range(6):
        pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.hotkey('alt','f4')

def send_w_message(person,message):
    pyautogui.press('win')
    pyautogui.sleep(2)
    pyautogui.typewrite('whatsapp')
    pyautogui.sleep(2)
    pyautogui.press('enter')
    pyautogui.sleep(4)
    pyautogui.typewrite(person)
    pyautogui.sleep(2)
    pyautogui.press('down')
    pyautogui.sleep(1)
    pyautogui.press('enter')
    pyautogui.sleep(1)
    pyautogui.typewrite(message)
    pyautogui.sleep(1)
    pyautogui.press('enter')
    pyautogui.sleep(2)
    pyautogui.hotkey('alt','f4')

def gen_pass():
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = "@#$%&*_-?"
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    all_characters = list(all_characters)
    print("Enter Length of Password")
    len_pass = ""
    len_pass = int(input())
    i = 0
    password = ""
    for i in range(len_pass):
        password += random.choice(all_characters)
    return(password)

def calculator():
    speak("Ok Now I will act as a Calculator.") 
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Square Root")
    print("6. Power Calculation")
    print("7. Trignometric Functions")
    print("8. Log Calculation")
    print("9. Currency Conversion")
    print("10. Expression Solving")
    print("You can perform the Calculation listed above. you have to enter the number given before the operation")
    speak("You can perform the Calculation listed above. you have to enter the number given before the operation")
    print("Enter Your Choice From the Above Menu")
    speak("Enter Your Choice from the above menu.")
    choice = int(input())
    match choice:
        case 1: 
            print("Enter Numbers seprated with spaces and press enter to Add the Number")
            speak("Enter Numbers seprated with spaces and press enter to Add the Number")
            number_string = input()
            numbers = re.findall(r'\d+(?:\.\d+)?', number_string)
            numbers = [float(value) if '.' in value else int(value) for value in numbers]
            total =0
            for value in numbers:
                total += value
            print(f"The Addition of Above values is {total}")
            speak(f"The Addition of Above values is {total}")
        case 2: 
            print("Enter Numbers seprated with spaces and press enter to Subtract the Number")
            speak("Enter Numbers seprated with spaces and press enter to Subtract the Number")
            number_string = input()
            numbers = re.findall(r'\d+(?:\.\d+)?', number_string)
            numbers = [float(value) if '.' in value else int(value) for value in numbers]
            total =0
            for value in numbers:
                total -= value
            print(f"The Subtraction of Above values is {total}")
            speak(f"The Subtraction of Above values is {total}")
        case 3: 
            print("Enter Numbers seprated with spaces and press enter to Divide the Number")
            speak("Enter Numbers seprated with spaces and press enter to Divide the Number")
            number_string = input()
            numbers = re.findall(r'\d+(?:\.\d+)?', number_string)
            numbers = [float(value) if '.' in value else int(value) for value in numbers]
            total =0
            for value in numbers:
                total /= value
            print(f"The Division of Above values is {total}")
            speak(f"The Division of Above values is {total}")
        case 4: 
            print("Enter Numbers seprated with spaces and press enter to Multiply the Number")
            speak("Enter Numbers seprated with spaces and press enter to Multiply the Number")
            number_string = input()
            numbers = re.findall(r'\d+(?:\.\d+)?', number_string)
            numbers = [float(value) if '.' in value else int(value) for value in numbers]
            total =0
            for value in numbers:
                total += value
            print(f"The Multiplication of Above values is {total}")
            speak(f"The Multiplication of Above values is {total}")
        case 5:
            print("Enter a Number of which you want to Calculate the Square Root")
            speak("Enter a Number of which you want to Calculate the Square Root")
            num_1 = float(input())
            total = math.sqrt(num_1)
            print(f"The Square Root of {num_1} is {total}")
        case 6: 
            print("Enter Two Numbers A and B to calculate A raise to power B")
            speak("Enter Two Numbers A and B to calculate A raise to power B")
            print("Enter first number")
            speak("Enter first number")
            num_1 = float(input())
            print("Enter Second number")
            speak("Enter Second number")
            num_2 = float(input())
            total = math.pow(num_1, num_2)
            print(total)
            speak(f"The {num_1} raise to power {num_2} is {total}")
        case 7:
            print("1. sin Function")
            print("2. cos Function")
            print("3. tan Function")
            print("4. cosec Function")
            print("5. sec Function")
            print("6. cot Function")
            print("Please Enter Which Function you want to perform")
            speak("Please Enter Which Function you want to perform")
            choice_1 = int(input())
            print("Enter the number")
            speak("Enter the number")
            num_1 = float(input())
            match choice_1:
                case 1:
                    total = math.sin(num_1)
                    print(f"The Sine of {num_1} is {total}")
                    speak(f"The Sine of {num_1} is {total}")
                case 2:
                    total = math.cos(num_1)
                    print(f"The Cosin of {num_1} is {total}")
                    speak(f"The Cosin of {num_1} is {total}")
                case 3:
                    total = math.tan(num_1)
                    print(f"The Tangent of {num_1} is {total}")
                    speak(f"The Tangent of {num_1} is {total}")
                case 4:
                    total = (1/math.sin(num_1))
                    print(f"The Cosecant of {num_1} is {total}")
                    speak(f"The Cosecant of {num_1} is {total}")
                case 5:
                    total = (1/math.cos(num_1))
                    print(f"The Secant of {num_1} is {total}")
                    speak(f"The Secant of {num_1} is {total}")
                case 6:
                    total = (1/math.tan(num_1))
                    print(f"The Cotangent of {num_1} is {total}")
                    speak(f"The Cotangent of {num_1} is {total}")
                case _: 
                    print("Wrong Input!")
                    speak("Wrong Input!")
        case 8:
            print("Enter Number you want to calculate the Log of")
            speak("Enter Number you want to calculate the Log of")
            num_1 = float(input())
            total = math.log(num_1)
            print(f"The Log of {num_1} is {total}")
            speak(f"The Log of {num_1} is {total}")
        case 9:
            print("Enter the country or Currency or Currency Code in which your amount is")
            speak("Enter the country or Currency or Currency Code in which your amount is")
            from_1 = input()
            print("Enter the country or Currency or Currency Code you wish your amount to be converted")
            speak("Enter the country or Currency or Currency Code you wish your amount to be converted")
            to_1 = input()
            source_country_valid = False
            destination_country_valid = False
            for sublist in currency_list:
                for element in sublist:
                    if element.lower() == from_1.lower():
                        source_country_valid = True
                        code_s = sublist[2]
                        break
            if source_country_valid:
                for sublist in currency_list:
                    for element in sublist:
                        if element.lower() == to_1.lower():
                            destination_country_valid = True
                            code_d = sublist[2]
                            break
            if source_country_valid and destination_country_valid:
                print("Enter Amount to be converted")
                speak("Enter Amount to be converted")
                amount_1 = float(input())
                try:
                    conversion_1 = c.convert(code_s, code_d, amount_1)
                    print(f"The converted amount is {conversion_1}")
                    speak(f"The converted amount is {conversion_1}")
                except Exception as f:
                    print("Conversion Error on Server Side")
                    speak("Conversion Error on Server Side")
            else:
                if not source_country_valid:
                    print("Source Country Invalid")
                    speak("Source Country Invalid")
                if not destination_country_valid:
                    print("Destination Country Invalid")
                    speak("Destination Country Invalid")
        case 10:
            print("Enter the Expression")
            speak("Enter the Expression")
            expression = input()
            total = eval(expression)
            print(f"The answer of the given expression is {total}")
            speak(f"The answer of the given expression is {total}")
        case _:
            print("Wrong Input!")
            speak("Wrong Input!") 

def weather(city_1):                
        city = city_1
        params = {
        'key': weather_api,
        'q': city,
    }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            location = data['location']['name']
            temperature = data['current']['temp_c']
            weather_description = data['current']['condition']['text']
            print(f"Location: {location}")
            print(f"Temperature: {temperature}°C")
            print(f"Weather: {weather_description}")
            speak(f"The current Weather at {location} is {weather_description} with temprature of {temperature}")
        else:
            print("Error occurred while fetching weather data.")

if __name__ == '__main__':
    pass
FACE = face_reco()
if FACE:
    greet_face()
else:
    speak("Exiting System, No Face Detected")
    exit()

while True:
    print("Listning.....")
    inp_1 = takeCommand()
    if "hello quantum" in inp_1.lower():
        greet()
    if "robot speaker" in inp_1.lower():
        speak("Ok I will act as a Robo Speaker from Now")
        while True:
            print("Listning.....")
            inp_2 = takeCommand()
            speak(inp_2)
            if "Stop Acting like Robot Speaker".lower() in inp_2.lower():
                break
    for site_open in site_open:
        if f"Open {site_open[0]}".lower() in inp_1.lower():
            speak(f"Opening {site_open[0]} Sir")
            webbrowser.open(site_open[1])
    if "time is it" in inp_1.lower():
        Time = datetime.datetime.now().strftime("%H:%M")
        speak(f"Sir the Current time is {Time}")
    if "quantum play" in inp_1.lower() or "to listen" in inp_1.lower() or "on youtube" in inp_1.lower():
        song = inp_1.lower().replace("quantum","")
        song = song.replace("play","")
        song = song.replace("to listen","")
        song = song.replace("i want","")
        song = song.replace("on youtube","")
        speak(f"Playing {song} on You Tube")
        pywhatkit.playonyt(song)
    if "launch" in inp_1.lower():
        inp_1 = inp_1.lower().replace("quantum", "")
        inp_1 = inp_1.lower().replace("launch", "")
        pyautogui.press("super")
        pyautogui.typewrite(inp_1)
        pyautogui.sleep(1)
        pyautogui.press("enter")
        speak(f"{inp_1} is Launched, Sir.")
    if "weather at" in inp_1.lower():
        index = inp_1.lower().find(' at ')
        if index != -1:
            temp_city = inp_1[index + 3:].strip()
            weather(temp_city)
        else:
            speak("Please Speak Correctly")
    if "play a game" in inp_1.lower():
        speak("Ok, Lets Play Rock, Paper, Scissor. You Have to make your call when I say Rock Paper Scissor")
        speak("Speak Play to start")
        print("Listning.....")
        inp_game = takeCommand()
        while True:
            if inp_game.lower() == "play":
                speak("Rock. Paper. Scissor")
                speak("Your Turn.")
                print("Listning.....")
                user_turn = takeCommand().strip()
                comp_turn = comp_choice()
                if user_turn == comp_turn:
                    speak("It's a Tie")
                elif user_turn.lower() == "rock" and comp_turn.lower() == "paper":
                    speak("I won with Paper")
                elif user_turn.lower() == "rock" and comp_turn.lower() == "Scissor":
                    speak("You won with Rock")
                elif user_turn.lower() == "paper" and comp_turn.lower() == "rock":
                    speak("You won with Paper")
                elif user_turn.lower() == "paper" and comp_turn.lower() == "scissor":
                    speak("I won with Scissor")
                elif user_turn.lower() == "scissor" and comp_turn.lower() == "paper":
                    speak("User won with Scissor")
                elif user_turn.lower() == "scissor" and comp_turn.lower() == "rock":
                    speak("I won with Rock")
                else:
                    speak("Wrong Input Please Try again")
                speak("Want to Play More? speak Yes to Continue the Game")
                print("Listning.....")
                inp_game_c = takeCommand()
                if inp_game_c.lower() != "yes":
                    break
            else:
                speak("No Input Detected Exiting")
                break
    if "some sites" in inp_1.lower():
        index = inp_1.lower().find(' on ')
        if index != -1:
            term = inp_1[index + 4:].strip()
            g_search(term)
        else:
            speak("Please Speak Correctly")
    if "search for" in inp_1.lower():
        index = inp_1.lower().find(' for ')
        if index != -1:
            term = inp_1[index + 4:].strip()
            wiki_search(term)
        else:
            speak("Please Speak Correctly")
    if "calculation" in inp_1.lower() or "calculator" in inp_1.lower():
        calculator()
    '''if "picture" in inp_1.lower():
        take_picture()'''
    if "leap year or not" in inp_1.lower():
        year = ""
        for char in inp_1:
            if char.isdigit():
                year += char
        leap_year_check(int(year))
    if "day on" in inp_1.lower():
        split_1 = inp_1.split()
        day_name = get_day_name(f"{split_1[-3]} {split_1[-2]} {split_1[-1]}")
        print(f"It was {day_name} on {split_1[-3]} {split_1[-2]} {split_1[-1]}")
        speak(f"It was {day_name} on {split_1[-3]} {split_1[-2]} {split_1[-1]}")
    if "enable wi-fi" in inp_1.lower() or "Disable Wi-fi".lower() in inp_1.lower():
        split_2 = inp_1.split()
        try:
            os.system(f'netsh interface set interface "Wi-Fi" admin={split_2[-2].lower()}')
            print("Can't find Wifi Icon. To Enable Wi-Fi again enter 'enable'")
            wifi = input()
            if wifi.lower() == "enable":
                os.system(f'netsh interface set interface "Wi-Fi" admin=enable')
        except:
            print(f"Can't {split_2[-2]} wifi due to lack of Admin Privilages Please Run me as Administrator")
            speak(f"Can't {split_2[-2]} due to lack of Admin Privilages Please Run me as Administrator")
    if "know wi-fi password" in inp_1.lower():
        print("To know password of saved Wi-Fi Networks please enter exact name of Network you want to know passowrd of")
        speak("To know password of saved Wi-Fi Networks please enter exact name of Network you want to know passowrd of")
        wifi_name = input()
        os.system(f'netsh wlan show profile name = "{wifi_name}" key = clear')
        speak("You can find the Password in Key Content field under Security Settings")
    for item in qa_list:
        if item[0].lower() in inp_1.lower():
            print(item[1])
            speak(item[1])
            break
    if "translate" in inp_1.lower():
        split_text = inp_1.split(" to ")
        source_text = split_text[0].lower().replace("Quantum Translate ".lower(), "")
        dest_language = split_text[1]
        for lang in language_list:
            if lang[1] == dest_language:
                dest_code = lang[0]
                translation2 = translator.translate(source_text, src='en', dest=dest_code)
                speak("Translation Done")
                print(f"Translated Text: {translation2.text}")
                break
    if "pick up line" in inp_1.lower():
            pickupline = random.choice(pick_up_lines)
            print(pickupline)
            speak(pickupline)
    if "joke" in inp_1.lower():
        speak("Here is a Joke")
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)
    if "download a youtube video" in inp_1.lower():
        print("Enter the URL of Video")
        speak("Enter the URL of Video")
        url_yt = input()
        youtube_download(url_yt)
    if "news" in inp_1.lower():
        latest_news()
    if "quotes" in inp_1.lower() or "quote" in inp_1.lower():
        quote = random.choice(quotes)
        print("Here is the Quote of the day:")
        speak("Here is the Quote of the day:")
        print(quote)
        speak(quote)
    if "take a note" in inp_1.lower():
        speak("Ok, I will save you speak Now")
        take_note = takeCommand()
        n_part = take_note.split()
        if n_part[0] == "" or n_part[0] == " ":
            n_part[0] = "Untitiled"
        if n_part[1] == "" or n_part[1] == " ":
            n_part[0] = "file"
        with open(f"D:\\codes\\Python_Projects\\Notes\\{n_part[0]} {n_part[1]}_{random.randint(1,999999999999)}.txt", "w") as take_note_file:
            take_note_file.write(take_note)
        speak("Note Taken and Saved sir.")
    if "screenshot" in inp_1.lower():
        sc = pyautogui.screenshot()
        sc.save(f"C:\\Users\\pmkks\\OneDrive\\Pictures\\Screenshots{random.randint(1,999999999999)}.png")
        speak("Screenshot Captured Sir")
    if "close the window" in inp_1.lower():
        pyautogui.hotkey('alt' , 'f4')
    if "generate a password" in inp_1.lower():
        password = gen_pass()
        print(f"Here is your password: {password}")
        speak("Here is you password")
        print(password)
        print("Want to save this to file?, In case you want to access it again.")
        speak("Want to save this to file?, In case you want to access it again.")
        print("Y/N?")
        pass_c = input()
        if pass_c == 'Y' or pass_c == 'y':
            print("Enter the Username for this Password")
            username = input()
            with open(f"C:\\Users\\saksh\\OneDrive\\Documents\\codes\\Python_Projects\\Saved_Passwords\\{username}", "w") as us_pw:
                us_pw.write("Username:")
                us_pw.write(" ")
                us_pw.write(username)
                us_pw.write("\n")
                us_pw.write("Password:")
                us_pw.write(" ")
                us_pw.write(password)
                us_pw.close()
            print("Password Saved with Username")
    if "increase the brightness" in inp_1.lower():
        os.system('WMIC /NAMESPACE:\\\\root\\wmi PATH WmiMonitorBrightnessMethods WHERE "Active=TRUE" CALL WmiSetBrightness Brightness=100 Timeout=0')
        speak("Brightness Increased")
    if "decrease the brightness" in inp_1.lower():
        os.system('WMIC /NAMESPACE:\\\\root\\wmi PATH WmiMonitorBrightnessMethods WHERE "Active=TRUE" CALL WmiSetBrightness Brightness=0 Timeout=0')
        speak("Brightness Decreased")
    if "turn the volume up" in inp_1.lower():
        for i in range(50):
            pyautogui.press('volumeup')
        speak("Volume Maxed")
    if "turn the volume down" in inp_1.lower():
        for i in range(25):
            pyautogui.press('volumedown')
        speak("Volume Decreased by 50 points")
    if "mute the system" in inp_1.lower():
            pyautogui.press('volumemute')
    if "change the tab" in inp_1.lower():
        pyautogui.hotkey('alt','tab')
    if "shutdown the system" in inp_1.lower():
        print("Confirm Shutdown (Y/N)")
        speak("Confirm Shutdown")
        c = input()
        if c=="Y" or c == "y":
            os.system('shutdown /s /t 0')
    if "remember this" in inp_1.lower():
        inp_r = inp_1
        speak("Rememberd Sir.")
    if "you to remember" in inp_1.lower():
        inp_r = inp_r.lower().replace("remember this","")
        inp_r = inp_r.replace("quantum","")
        speak(inp_r)
        print(inp_r)
    if "set an alarm" in inp_1.lower():
        inp_1 = inp_1.lower().replace("o'clock", "")
        inp_s = inp_1.split()
        inp_s = inp_s[-1].split(":")
        h_1 = inp_s[0][0]
        try:
            h_2 = inp_s[0][1]
        except:
            h_2 = h_1
            h_1 = "0"
        try:
            m_1 = inp_s[1][0]
        except:
            m_1 = "0"
        try:
            m_2 = inp_s[1][1]
        except:
            m_2 = "0"
        if h_1 == "2" and h_2 == "4":
            h_1 = "0"
            h_2 = "0"
        alarm(h_1, h_2, m_1, m_2)
        speak(f"Alarm will ring at {h_1}{h_2} : {m_1}{m_2}")
        print(f"Alarm will ring at {h_1}{h_2} : {m_1}{m_2}")
    if "typing test" in inp_1.lower():
        speak("Ok, Here is a 1 Minute Typing Test")
        root = tk.Tk()
        root.title("Typing Test")
        root.geometry("800x500")
        intro_label = tk.Label(root, text="Welcome to the Typing Test!", font=("Helvetica", 18))
        intro_label.pack(pady=20)
        start_button = tk.Button(root, text="Start Typing Test", command=start_typing_test)
        start_button.pack()
        root.mainloop()
    if "stock market" in inp_1.lower():
        Stock_Market()
    if "say hello to" in inp_1.lower():
        inp_1 = inp_1.lower().replace("say hello to", "")
        inp_1 = inp_1.replace("quantum","")
        speak(f"Hello {inp_1}")
    if "send message" in inp_1.lower():
        speak("Ok type your message")
        print("Ok Type your message")
        message = input()
        person = inp_1.lower().replace("quantum","")
        person = person.replace("send message to","")
        person = person.replace("on whatsapp", "")
        send_w_message(person,message)
        speak("Message sent Sir.")
    if "change your voice to" in inp_1.lower():
        voice_1 = inp_1.split()
        voice = voice_1[-1]
        if voice == "male":
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            speak("Voice Changed Sir")
            continue
        elif voice == "female":
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            speak("Voice Changed Sir")
            continue
        else:
            print("Please Choose from Male or Female")
            speak("Please Choose from Male or Female")
    if "check some spellings" in inp_1.lower():
        print("Ok, Please Enter the Paragraph or Spelling you want to check.")
        speak("Ok, Please Enter the Paragraph or Spelling you want to check.")
        para_1 = input()
        corrections = spellcheck_paragraph_with_suggestions(para_1)
        if corrections:
            print("These are the Misspelled words and and some suggestions from my side:")
            speak("These are the Misspelled words and and some suggestions from my side.")
            for word, suggestions in corrections.items():
                print(f"Word: {word}, Suggestions: {', '.join(suggestions)}")
        else:
            print("No misspelled words found.")
            speak("No misspelled words found.")
    if "complete microsoft rewards points" in inp_1.lower():
        print("Ok, Sir Completing Point on Microsoft Rewards")
        speak("Ok, Sir Completing Point on Microsoft Rewards")
        Micro_rewards()
        print("Completed Sir")
        speak("Completed Sir")
    if "heads or tail" in inp_1.lower() or "heads and tail" in inp_1.lower():
        c_1 = random.randint(1,2)
        if c_1 == 1:
            print("Heads")
            speak("Heads")
        else:
            print("Tails")
            speak("Tails")
    if "i am getting bored" in inp_1.lower():
        print(random.choice(entertainment_content))
        speak(random.choice(entertainment_content))
    if "exit quantum" in inp_1.lower():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<=17:
            speak("Exiting System sir. Have a nice Day")
        else:
            speak("Exiting System sir. Good Night.")
        break