
import speech_recognition as sr

recognizer = sr.Recognizer()

print("Available microphones:")

for i, name in enumerate(sr.Microphone.list_microphone_names()):
    print(i, name)

print("\nStarting microphone test...")

with sr.Microphone() as source:
    print("Calibrating microphone...")
    recognizer.adjust_for_ambient_noise(source, duration=2)

    print("Speak now!")

    audio = recognizer.listen(source, phrase_time_limit=5)

    print("Your microphone captured audio successfully!")
    print("Audio length:", len(audio.get_raw_data()))
