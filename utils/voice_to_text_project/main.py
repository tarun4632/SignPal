from voice_to_text import VoiceToText

def main():
    vtt = VoiceToText()
    audio = vtt.record_audio()
    text = vtt.convert_to_text(audio)
    print(f"Recognized text: {text}")

if __name__ == "__main__":
    main()