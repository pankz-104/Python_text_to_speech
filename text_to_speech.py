from gtts import gTTS
import os

myText = "Text to speech conversion in python language"
language = 'en'
engine_output = gTTS(text = myText, lang = language, slow = False)
engine_output.save("output.mp3")
os.system("start output.mp3")
