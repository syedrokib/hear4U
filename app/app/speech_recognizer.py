import speech_recognition as sr
from os import path

r = sr.Recognizer()

# with sr.AudioFile(path.join(path.dirname(path.realpath(__file__)), "audio-stereo-16-bit-44100Hz.wav")) as source:
#     audio = r.record(source)  # read the entire audio file
#     print r.recognize_sphinx(audio)

# input_wav = sr.AudioFile('harvard.wav')
# with input_wav as source:
#     # audio = r.record(source)
#     # print r.recognize_sphinx(audio)
#     print sr.Microphone.list_microphone_names()
mic = sr.Microphone()
with mic as source:
    audio = r.listen(source)
    print r.recognize_google(audio)
