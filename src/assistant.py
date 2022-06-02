from threading import Thread
import time

import speech_recognition as sr

from pynput.keyboard import Controller
from pynput.keyboard import Listener

import src.invoker as invoker
import src.sf as sf


class Assistant():

    def __init__(self):
        self.r = sr.Recognizer()
        self.m = sr.Microphone()
        self.keyboard = Controller()
        self.isAssistantActivated = False

    def listenAndCast(self):
        
        while True:
            if self.isAssistantActivated == True:
                with self.m as source:

                    print("say something")
                    self.isAssistantActivated = False
                    audio = self.r.listen(source, phrase_time_limit = 1.5)
                    strt = time.time()
                    try:

                        s = self.r.recognize_google(audio, language='ru')
                        print(s)
                        ss = s.split(" ")
                        amount = 1
                        self_cast = False
                        for text in ss:
                            if invoker.tryCastInvoker(text, self.keyboard):
                                continue
                            elif sf.tryCastSF(text, self.keyboard):
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
                                                self.keyboard.press(self.keyboard._Key.alt)
                                        if i.lower() in ["q", "w", "e","r","d","f","v","c","x", "t", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                                            print(i.lower())
                                            self.keyboard.press(i.lower())
                                            self.keyboard.release(i.lower())
                                            time.sleep(0.15)
                                        elif i.lower() in pairs.keys():
                                            self.keyboard.press(pairs[i.lower()])
                                            self.keyboard.release(pairs[i.lower()])
                                            time.sleep(0.15)
                                        if self_cast:
                                                self.keyboard.release(self.keyboard._Key.alt)
                                time.sleep(0.15)
                        print(time.time() - strt)
                            
                    except sr.UnknownValueError:
                        print("Could not understand")
                    except sr.RequestError as e:
                        print("errpr: {0}".format(e))


    def on_press(self, key):
        if key == self.keyboard._Key.page_up and self.isAssistantActivated == False:
            self.isAssistantActivated = True
    
    def startListen(self):
        with Listener(on_press=self.on_press) as listener:
            print("Assistant is ready to use.")
            x = Thread(target=self.listenAndCast,)
            x.start()
            x.join()
            listener.join()  


