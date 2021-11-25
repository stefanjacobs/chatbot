
import multiprocessing
import pyttsx3
import concurrent.futures
import threading
import queue
import time

from multiprocessing import Process


def say(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.say(text)
    engine.runAndWait()


class VocalOutputThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.queue = queue.Queue()


    def say(self, message):
        self.queue.put(message)


    def run(self):
        while True:
            time.sleep(0.1)
            # print(".", end="")
            
            if not self.queue.empty():
                message = self.queue.get()
                with multiprocessing.Pool(1) as pool:
                    r = pool.apply_async(say, (message,))
                    while not r.ready():
                        time.sleep(0.1)
                self.queue.task_done()


if __name__ == '__main__':
    messages = ["Hello world!", "How are you?", "I am fine, thank you.", "Goodbye!"]
    t = VocalOutputThread()
    t.daemon = True
    t.start()

    for m in messages:
        t.say(m)
    
    print("all messages to vocal done")
    t.join()


#    with multiprocessing.Pool(processes=1) as pool:
#        for m in messages:
#            r = pool.map_async(say, [m])
#        print("Main Thread has appended all messages")
#        while not r.ready():
#            print(".", end="")
#            r.wait(0.1)