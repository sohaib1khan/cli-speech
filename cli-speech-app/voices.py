import pyttsx3

engine = pyttsx3.init()

# List all available voices
voices = engine.getProperty('voices')
for idx, voice in enumerate(voices):
    print(f"Voice #{idx}: ID: {voice.id}, Name: {voice.name}, Languages: {voice.languages}")

# Set a specific voice by its ID
chosen_voice_id = voices[17].id  # Example: choose the first voice
engine.setProperty('voice', chosen_voice_id)

# Test the chosen voice
engine.say("Hello, how are you?")
engine.runAndWait()
