import speech_recognition as sr

class VoiceToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def record_audio(self, duration=5):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source, timeout=duration)
        return audio

    def convert_to_text(self, audio):
        try:
            text = self.recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results; {e}"

# Usage example
if __name__ == "__main__":
    vtt = VoiceToText()
    audio = vtt.record_audio()
    text = vtt.convert_to_text(audio)
    print(f"Recognized text: {text}")