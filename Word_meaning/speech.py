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