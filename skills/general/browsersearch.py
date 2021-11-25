from base_skill import BaseSkill
from random import sample
import webbrowser

class BrowserSearchSkill(BaseSkill):

    def __init__(self):
        super().__init__()
        self.intent = __name__
        self.active = True
        self.samples = [
            "open browser and search for",
            "google for ",
            "search for ",
            "try to find online",
            "search online for",
            "search for on the web",
            "search for on the internet",
        ]
        self.responses = [
            "Opening browser and searching for $0.",
            "Searching for $0 using your default browser."
        ]
        self.entities = {
            "query": {"spec": "pobj", "default": ""}
        }


    def actAndGetResponse(self, **kwargs) -> str:
        url = "https://www.google.com/search?q=" + kwargs["query"]
        webbrowser.get().open_new_tab(url)
        return sample(self.responses, 1)[0].replace("$0", kwargs["query"])


    def parseEntities(self, doc) -> dict():
        params = dict()

        for k, v in self.entities.items():
            params[k] = v["default"]
        
        if len(doc) == 1:
            # pure intent, no entities
            return params
        
        for k, v in self.entities.items():
            if v["spec"] == "pobj":
                for token in doc:
                    if token.dep_ == 'pobj':
                        params[k] = token.text
                        break

        return params