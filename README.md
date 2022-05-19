# Dota Voice Assistant
Dota 2 Voice assistant 

# Install
TODO: requirements.txt, and virtualenv

pip install SpeechRecognition

pip install pynput

pip install PyAudio

# How to use
Use eng keyboard on windows. If keyboard is RU, assistant will use only numbers. Recommend to use quickcast in dota
run python main.py
When you need to cast spell:
1) use page_up (bind some your mouse key to page_up!)

2) call key or word. Each char in word will be used as key if char is one of ["q", "w", "e","r","d","f","v","c","x", "t", "1", "2", "3", "4", "5", "6", "7", "8", "9"]. 
(For RU: Пара "x": "y" означает, что по русской x будет использоваться клавиша y. Пары: ["в": "w", "е": "e", "и": "e", "д": "d", "ф": "f", "р" : "r", "я" : "q"]). For example, if you say: "funny friends" assistant will cast ffrd.

3) For self cast say: "double *KEY*" or "двойной *KEY*"

4) SF and Invoker has combos: check it in sf.py and invoker.py. Boom/бум/let me die/ for eul and requiem of souls. Камень, снег, духи, луч, стена, торнадо, невидимость, бласт, минус для meteor, coldsnap, forge spirits, sunstrike, icewall, tornado, ghostwalk, blast and EMP.

5) Have fun!
