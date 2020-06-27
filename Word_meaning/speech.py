from cred import api_key
import speech_recognition as sr 
import requests

def search_word():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak...")
        word = r.listen(source)
        
        try:
            text = r.recognize_google(word)
            text.strip()
            print(f"word asked is {text}")
            return text.strip()
        except:
            print("sorry i couldnt understand")
            return "none"

def get_meaning(word):
    apikey = api_key()
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/definitions/"

    headers = {
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
        'x-rapidapi-key': apikey
        }

    response = requests.request("GET", url, headers=headers)

    return response.json()['definitions']