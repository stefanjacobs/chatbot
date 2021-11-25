from base_skill import BaseSkill
from random import sample
import colorama


class HelpSkill(BaseSkill):

    def __init__(self):
        super().__init__()
        self.intent = __name__
        self.active = True
        self.samples = [
            "i need help",
            "help",
            "list skills",
            "please help"
        ]
        self.responses = [
            "Here is the list of skills.",
            "Those are the skills that are active."
        ]

    def actAndGetResponse(self, **kwargs) -> str:
        skills = kwargs["skills"]
        print("The list of skills is:")
        for intent, skill in skills.items():
            if skill.active:
                print(colorama.Fore.GREEN + "- " + intent)
        return sample(self.responses, 1)[0]