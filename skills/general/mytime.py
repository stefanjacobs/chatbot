import time
from base_skill import BaseSkill
from random import sample


class TimeSkill(BaseSkill):

    def __init__(self):
        super().__init__()
        self.intent = __name__
        self.active = True
        self.samples = ["time", "get time", "what time is it", "what is the time", "what time is it at the moment", "what time is it now", "what time is it today"]
        self.responses = ["The time is $0 o'clock.", "Now is $0 o'clock."]

    def actAndGetResponse(self, **kwargs) -> str:
        response = sample(self.responses, 1)[0]
        now = time.strftime("%H:%M")
        return response.replace("$0", now)
