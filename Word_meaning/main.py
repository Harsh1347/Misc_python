import requests
import speech_recognition as sr 
from speech import search_word
from cred import api_key

word = search_word()
apikey = api_key()
url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/definitions/"

headers = {
    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
    'x-rapidapi-key': apikey
    }

response = requests.request("GET", url, headers=headers)

print(response.json()['definitions'])