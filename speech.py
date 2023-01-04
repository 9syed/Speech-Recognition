import speech_recognition as sr

a = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            print("Say Something....")
            audio = a.listen(source)

            text = a.recognize_google(audio)
            text = text.lower()
            print(f"Recognized speech: {text}")
    except:
        print("Could not understand, please repeat")
        a = sr.Recognizer()
        continue