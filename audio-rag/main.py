import speech_recognition as sr
r = sr.Recognizer()
file = sr.AudioFile('./audio.wav')
with file as source:
    audio = r.record(source)
print(r.recognize_sphinx(audio))
