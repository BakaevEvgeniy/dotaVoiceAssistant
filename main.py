from threading import Thread
import pyaudio
import time

import speech_recognition as sr

from pynput.keyboard import Controller
from pynput.keyboard import Listener

import invoker as invoker
import sf as sf

p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    dev = p.get_device_info_by_index(i)
    print((i, dev['name'], dev['maxInputChannels']))

r = sr.Recognizer()
m = sr.Microphone()

keyboard = Controller()

isAssistantActivated = False

def listenAndCast():
    global isAssistantActivated
    while True:
        if isAssistantActivated == True:
            with m as source:

                print("say something")
                isAssistantActivated = False
                audio = r.listen(source, phrase_time_limit = 1.5)
                strt = time.time()
                try:

                    s = r.recognize_google(audio, language='ru')
                    print(s)
                    ss = s.split(" ")
                    amount = 1
                    self_cast = False
                    for text in ss:
                        if invoker.tryCastInvoker(text, keyboard):
                            continue
                        elif sf.tryCastSF(text, keyboard):
                            continue
                        elif text.lower() == "triple":
                            amount = 3
                        elif text.lower() == "double" or text.lower() == "двойной":
                            self_cast = True
                        else:
                            for i in text:
                                pairs = {"в": "w", "е": "e", "и": "e", "д": "d", "ф": "f", "р" : "r", "я" : "q"}
                                for j in range(amount):
                                    if self_cast:
                                            keyboard.press(keyboard._Key.alt)
                                    if i.lower() in ["q", "w", "e","r","d","f","v","c","x", "t", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                                        print(i.lower())
                                        keyboard.press(i.lower())
                                        keyboard.release(i.lower())
                                        time.sleep(0.15)
                                    elif i.lower() in pairs.keys():
                                        keyboard.press(pairs[i.lower()])
                                        keyboard.release(pairs[i.lower()])
                                        time.sleep(0.15)
                                    if self_cast:
                                            keyboard.release(keyboard._Key.alt)
                            time.sleep(0.15)
                    print(time.time() - strt)
                        
                except sr.UnknownValueError:
                    print("Could not understand")
                except sr.RequestError as e:
                    print("errpr: {0}".format(e))


def on_press(key):
    global isAssistantActivated
    if key == keyboard._Key.page_up and isAssistantActivated == False:
        isAssistantActivated = True

with Listener(on_press=on_press) as listener:
    x = Thread(target=listenAndCast,)
    x.start()
    x.join()
    listener.join()  