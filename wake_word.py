def is_wake_word(text):
    wake_words = [
        "hey panda",
        "hi panda",
        "hello panda",
        "panda"
    ]

    text = text.lower()

    for word in wake_words:
        if word in text:
            return True

    return False