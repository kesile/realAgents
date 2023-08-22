import openai
from distributions.distro import Distro
from schedulers.scheduler import scheduler

class Agent:
    def __init__(self, api_key, debug = False):
        self.api_key = api_key
        openai.api_key = api_key
        self.debug = debug
        if self.debug: print("Agent Initalized")

    def _generate(self):
        self.person = Distro()
        self.person = self.person.generate()
        if self.debug: print("Generated Person Data")
        self.person.update({"schedule" : scheduler(self.person)})
        return self.person