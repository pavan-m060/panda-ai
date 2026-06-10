from brain import ask_panda
from speak import speak
from listen import listen
from wake_word import is_wake_word
from vision import detect_objects
from face_analyzer import analyze_face

print("🐼 PANDA ACTIVATED")

speak("PANDA is online.")

active = False

while True:

    user = listen()

    if user == "":
        continue

    print("You:", user)

    if "exit" in user:
        speak("Goodbye")
        break

    if not active:

        if is_wake_word(user):
            active = True
            speak("Yes, how can I help?")
        continue

        # Vision command
        # Vision command
    if "see" in user:

        objects = detect_objects()

        if objects:

            response = "I can see " + ", ".join(objects)

            print("PANDA:", response)

            speak(response)

        else:

            speak("I cannot see anything.")

        active = False
        continue

    # Face analysis command
    if "analy" in user:

        info = analyze_face()

        if info:

            response = (
                f"I see a {info['gender']} "
                f"approximately {info['age']} years old."
            )

            print("PANDA:", response)

            speak(response)

        else:

            speak("I could not detect a face.")

        active = False
        continue
    
    # Normal AI chat
    answer = ask_panda(user)

    print("PANDA:", answer)

    speak(answer)

    active = False