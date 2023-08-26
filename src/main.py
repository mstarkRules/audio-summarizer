import moviepy.editor as mp
import speech_recognition as sr
import sys
from pydub import AudioSegment

path = "src/assets/audio.ogg"

sound = AudioSegment.from_ogg(path)
sound.export("src/outputs/output.wav", format="wav")

file_audio = sr.AudioFile(r"src/outputs/output.wav")

r = sr.Recognizer()

with file_audio as source:
    audio_text = r.record(source)
    text = r.recognize_google(audio_text, language="pt-BR")

print("text: ", text)
