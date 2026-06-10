import speech_recognition as sr

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.adjust_for_ambient_noise(source, duration=1)

        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)

        print("You:", text)

        return text.lower()

    except Exception as e:
        print("Error:", e)
        return ""