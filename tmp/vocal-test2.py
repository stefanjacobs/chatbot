import multiprocessing
import pyttsx3
from multiprocessing import Process

class _TTS:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 175)

    def start(self,text_):
        self.engine.say(text_)
        self.engine.runAndWait()

def Speakit(words):
    print('running Speakit')
    tts = _TTS()
    tts.start(words)
    del(tts)

def testing(n):
    print(n)
    if n == 0:
        words = 'Argument is zero'
        Speakit(words)
        print(words)
    else:
        words = 'Argument is not zero'
        Speakit(words)
        print(words)

if __name__=="__main__":
    words = 'start'
    Speakit(words)
    p1=Process(target=testing(4),args=(0,))
    p1.start()
    p1.join(0.1)
    p2=Process(target=testing(0),args=(5,))
    p2.start()
    p2.join(0.1)
    print("We're done")
    p1.join()
    p2.join()