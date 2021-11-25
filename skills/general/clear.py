from base_skill import BaseSkill
from random import sample

class ClearSkill(BaseSkill):

    def __init__(self):
        super().__init__()
        self.intent = __name__
        self.active = True
        self.samples = [
            "clear screen",
            "new screen",
            "clear terminal",
            "reset terminal"
        ]
        self.responses = [
            "Screen cleared",
            "Terminal cleared",
            "Screen reset",
            "Terminal reset"
        ]

    def actAndGetResponse(self, **kwargs) -> str:
        print("\033c", end="")
        return sample(self.responses, 1)[0]