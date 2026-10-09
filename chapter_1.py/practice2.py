import pyttsx3

engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')

# Print available voices (optional, helpful for choosing)
for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name}, ID: {voice.id}, Lang: {voice.languages}")

# Change to a different voice
