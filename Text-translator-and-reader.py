import os
from googletrans import Translator, constants
from gtts import gTTS as t2s
from playsound import playsound as ps

file = "speech.mp3"

text_org = "Hello, World!"

def prints(text="", ):
    """
    docstring
    """
    pass

ts = Translator()
detect = ts.detect(text_org)
src_lang = detect.lang
src_con = detect.confidence
src_con_per = int(src_con*100)
des_lang = "ja"

text = ts.translate(text_org, src=src_lang, dest=des_lang).text

print(f"{text_org} ({constants.LANGUAGES[src_lang]} - confidence: {src_con_per}%) --> {text} ({constants.LANGUAGES[des_lang]})")

s = t2s(text=text, lang=des_lang)
s.save(file)
ps(file)
os.remove(file)
