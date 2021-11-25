from base_skill import BaseSkill
from random import sample


class GreetingSkill(BaseSkill):

    def __init__(self):
        super().__init__()
        self.intent = __name__
        self.active = True
        self.responses = [
            "Welcome to Sir-bot-a-lot! How may I serve?",
            "Hi!",
            "S-B-A-L at your service."
        ]

    def actAndGetResponse(self, **kwargs) -> str:
        return sample(self.responses, 1)[0]