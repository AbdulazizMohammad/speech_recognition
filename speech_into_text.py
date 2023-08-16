import speech_recognition as sr

r = sr.Recognizer()
while (1):
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
            text = r.recognize_google(audio, language='ar-SA')
            print(text)
    except sr.RequestError as e:
        print(f"Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occurred")
