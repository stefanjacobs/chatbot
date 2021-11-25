from base_skill import BaseSkill
from random import sample
import colorama

class QuitSkill(BaseSkill):

    def __init__(self):
        super().__init__()
        self.intent = __name__
        self.active = True
        self.samples = [    
            "quit",
            "exit",
            "shutdown",
            "please end program",
            "shut down"
        ]
        self.responses = [
            "Bye!",
            "See you later!",
            "Goodbye!",
            "Have a nice day!",
            "I'll be back!"
        ]

    def actAndGetResponse(self, **kwargs) -> str:
        voice = kwargs["voice"]
        response = sample(self.responses, 1)[0]
        voice.say(response)
        voice.say("Shutting down...")
        voice.join(5)
        colorama.deinit()
        exit()