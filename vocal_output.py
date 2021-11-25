
import threading, multiprocessing, queue
import pyttsx3
import time
import colorama


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
        print(colorama.Fore.GREEN + message + colorama.Fore.RESET)


    def run(self):
        while True:
            time.sleep(0.1)
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
