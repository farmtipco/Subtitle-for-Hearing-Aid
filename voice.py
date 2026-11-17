
import speech_recognition as sr
import whisper

# Load Whisper model
print("Loading Whisper model...")
model = whisper.load_model("small")

# Initialize microphone recognizer
recognizer = sr.Recognizer()
mic = sr.Microphone()

print("Ready for listening... Press Ctrl+C to stop.")

try:
    with mic as source:

        # Adjust for background noise
        recognizer.adjust_for_ambient_noise(source)

        while True:
            print("\nListening...")

            # Record audio for up to 3 seconds
            audio = recognizer.listen(
                source,
                phrase_time_limit=3
            )

            # Save audio temporarily
            with open("temp.wav", "wb") as f:
                f.write(audio.get_wav_data())

            # Transcribe audio using Whisper
            result = model.transcribe("temp.wav")

            text = result["text"].strip()

            if text:
                print("You said:", text)

except KeyboardInterrupt:
    print("\nExiting...")
