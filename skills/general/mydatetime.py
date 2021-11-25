import time
from base_skill import BaseSkill
from random import sample


class DateTimeSkill(BaseSkill):

    def __init__(self):
        super().__init__()
        self.intent = __name__
        self.active = True
        self.samples = [
            "datetime",
            "get datetime",
            "what date and time is it",
            "what is the date and time",
            "what is the datetime",
            "what datetime is it now"
        ]
        self.responses = [
            "The date is $0 and the time is $1 o'clock",
            "Now is $0 at $1 o'clock"
        ]

    def actAndGetResponse(self, **kwargs) -> str:
        response = sample(self.responses, 1)[0]    
        today, now = time.strftime("%d %B, %Y"), time.strftime("%H:%M")
        return response.replace("$0", today).replace("$1", now)
