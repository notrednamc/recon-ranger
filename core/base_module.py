from abc import ABC, abstractmethod

class RedTeamModule(ABC):
    def __init__(self, target, options=None):
        self.target = target
        self.options = options or {}

    @abstractmethod
    def run(self):
        pass
