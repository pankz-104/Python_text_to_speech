from gtts import gTTS
import os

fh = open("pankaj.txt","r")
mytext = fh.read().replace("\n"," ")
language = 'en'
output = gTTS(text = mytext, lang = language, slow = False)
output.save("pankaj.mp3")
os.system("pankaj.mp3")
fh.close()
