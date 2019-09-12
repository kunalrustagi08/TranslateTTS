from gtts import gTTS
from googletrans import Translator
import os

translator = Translator()
ip_text = input('Enter your message')

translated = translator.translate(text = ip_text, dest = "hi") 

tts = gTTS(text = translated.text, lang = "hi")

tts.save('your_text.mp3')	
os.system("mpg321 your_text.mp3") 
