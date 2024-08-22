import os
import webbrowser
import datetime
import pyttsx3
import subprocess
import ctypes
import time
import wolframalpha
import winshell
import pyjokes
import requests
from ecapture import ecapture as ec
from urllib.request import urlopen
import json
import shutil
import speech_recognition as sr
import smtplib
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

for voice in voices:
    print(voice.id, voice.languages, voice.name)

for voice in voices:
    if "Spanish" in voice.languages or "es" in voice.id:
        engine.setProperty('voice', voice.id)
        break

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Buenos días!")
    elif hour >= 12 and hour < 18:
        speak("Buenas tardes!")   
    else:
        speak("Buenas noches!")  
  
    assname = "Ricardito"
    speak("Soy tu asistente")
    speak(assname)
 
def username():
    speak("como quiere que lo llame?")
    uname = takeCommand()
    speak("Welcome" + uname)
    columns = shutil.get_terminal_size().columns
     
    print("#####################".center(columns))
    print(f"Welcome Mr. {uname}".center(columns))
    print("#####################".center(columns))
    
    speak("En que lo puedo ayudar?" + uname) 
 
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Reconociendo...")    
        query = r.recognize_google(audio, language='es-ES')
        print(f"Usuario dice: {query}\n")
    except Exception as e:
        print(e)    
        print("No se pudo reconocer tu voz.")  
        return "None"
     
    return query
  
def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        # Enable low security in Gmail
        server.login('your email id', 'your email password')
        server.sendmail('your email id', to, content)
        server.close()
        speak("Email fue enviado!")
    except Exception as e:
        print(e)
        speak("No pude enviar el email")

if __name__ == '__main__':
    clear = lambda: os.system('cls')

   
    clear()
    wishMe()
    username()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Buscando Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("Según Wikipedia")
            print(results)
            speak(results)

        elif 'Abrir youtube' in query or 'Youtube' in query:
            speak("Abriendo Youtube\n")
            webbrowser.open("youtube.com")

        elif 'Abrir google'in query or 'Google' in query:
            speak("Abriendo Google\n")
            webbrowser.open("google.com")

        elif 'abrir stackoverflow' in query or 'stackoverflow' in query:
            speak(":v yendo a stackoverflow!")
            webbrowser.open("stackoverflow.com")

        elif 'musica' in query or "spaceghostpurrp" in query:
            speak("antidoto xd")
            webbrowser.open("https://on.soundcloud.com/AM7EX6Wbot5fnnNJA")

        elif 'Hora' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Esta es la fecha y hora{strTime}")

        elif 'abrir navegador' in query:
            codePath = r"C:\\Users\\MARKO-PX\\AppData\\Local\\Programs\\Vivaldi\\launcher.exe"
            os.startfile(codePath)

        elif 'email para marko' in query or 'enviar correo' in query:
            try:
                speak("Que quieres decir?")
                content = takeCommand()
                if 'email para marko' in query:
                    to = "markogamarra94@gmail.com"
                else:
                    speak("A quien le envio el correo?")
                    to = input("Enter email address: ")
                sendEmail(to, content)
                speak("Email fue enviado!")
            except Exception as e:
                print(e)
                speak("No se pudo enviar")

        elif 'como estas' in query:
            speak("Estoy bien, gracias por preguntar")
            speak("Como esta usted?")

        elif 'bien' in query or "good" in query:
            speak("Es bueno escuchar que esta bien")

        elif "Cambia mi nombre" in query:
            query = query.replace("cambia mi nombre a ", "")
            assname = query

        elif "Cambiar nombre" in query:
            speak("Como le gustaria llamarme?")
            assname = takeCommand()
            speak("Gracias por ponerme un nombre")

        elif "cual estu nombre" in query or "como te llamas" in query:
            speak("mis amigos me llaman" + assname)
            print("Mis amigos me llaman", assname)

        elif 'exit' in query:
            speak("Gracias por tu tiempo")
            exit()

        elif "quien te creo" in query or "who created you" in query:
            speak("Fuí creado por Marko.")

        elif 'chiste' in query:
            speak(pyjokes.get_joke())

        elif "calcula" in query:
            app_id = "Wolframalpha API ID"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("la respuesta es " + answer)
            speak("la respuesta es " + answer)

        elif 'busca' in query or 'reproduce' in query:
            query = query.replace("search", "").replace("play", "")
            webbrowser.open(query)

        elif "quien soy" in query:
            speak("Si hablas definitivamente eres un humano.")

        elif "Como viniste al mundo" in query:
            speak("Gracias a Marko, no le digas a nadie es un secreto.")

        elif 'power point' in query:
            speak("Opening PowerPoint presentation")
            power = r"C:\\Users\\GAURAV\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
            os.startfile(power)

        elif 'es amor' in query:
            speak("It is the 7th sense that destroys all other senses.")

        elif "quien eres" in query:
            speak("Soy tu asistente virtual.")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, "Location of wallpaper", 0)
            speak("Background changed successfully")

        elif 'abre bluestacks' in query:
            appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
            os.startfile(appli)

        elif 'noticias' in query:
            try:
                jsonObj = urlopen('''https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=times_of_india_api_key''')
                data = json.load(jsonObj)
                i = 1

                speak('Aqui hay algunas noticias de la India')
                print('=============== TIMES OF INDIA ============\n')

                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                print(str(e))

        elif 'lock window' in query:
            speak("Locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'apaga el sistema' in query:
            speak("Hold on a second! Your system is on its way to shut down")
            subprocess.call('shutdown /p /f')

        elif 'vacia la papelera' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin emptied")

        elif "no escuches" in query or "para de escuchar" in query:
            speak("Por cuanto tiempo quieres que deje de escuchar?")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "donde esta" in query:
            query = query.replace("donde esta", "")
            location = query
            speak("Pregunto la ubicación")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location)

        elif "camara" in query or "toma una foto" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")

        elif "reinicia" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernar" in query or "duerme" in query:
            speak("Hibernando")
            subprocess.call("shutdown /h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the applications are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "escribe una nota" in query:
            speak("Que quiere escribir?")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Incluyo la fecha y la hora?")
            snfm = takeCommand()
            if 'si' in snfm or 'claro' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
            file.close()

        elif "mostrar nota" in query:
            speak("Mostrando notas")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))
            file.close()

        elif "update assistant" in query:
            speak("After downloading the file, please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream=True)

            with open("Voice.py", "wb") as Pypdf:
                total_length = int(r.headers.get('content-length'))

                for ch in progress.bar(r.iter_content(chunk_size=2391975),
                                       expected_size=(total_length / 1024) + 1):
                    if ch:
                        Pypdf.write(ch)

        elif "Ricardito" in query:
            wishMe()
            speak("Estoy a tu servicio")
            speak(assname)

        elif "clima" in query:
            api_key = "Your_OpenWeather_API_Key"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak("City name")
            print("City name: ")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]

                print("Temperature (in kelvin unit) = " +
                      str(current_temperature) +
                      "\nAtmospheric pressure (in hPa unit) = " +
                      str(current_pressure) +
                      "\nHumidity (in percentage) = " +
                      str(current_humidity) +
                      "\nDescription = " +
                      str(weather_description))

                speak("Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\nAtmospheric pressure in hPa unit is " +
                      str(current_pressure) +
                      "\nHumidity in percentage is " +
                      str(current_humidity) +
                      "\nDescription " +
                      str(weather_description))

            else:
                speak("City not found")

        elif "send message " in query:
            pass

        elif "buenos dias" in query:
            speak("Buneos dias")
            speak(assname)

        elif "Buenas tardes" in query:
            speak("Buenas tardes. en que puedo ayudarte?")

        elif "Buenas noches" in query:
            speak("Buenas noches, descansa!")

        elif "Para" in query:
            speak("Como tu desees, Apagando.")
            exit()
