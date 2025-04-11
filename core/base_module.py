from abc import ABC, abstractmethod

class RedTeamModule(ABC):
    def __init__(self, target, options=None, shared_results=None, api_keys=None):
        self.target = target
        self.options = options or {}
        self.results = shared_results if shared_results is not None else {}
        self.api_keys = api_keys or {}

    @abstractmethod
    def run(self):
        pass

    def log_markdown(self, text, level="info"):
        prefix = {
            "header": "##",
            "success": "- ✔️",
            "fail": "- ❌",
            "warn": "- ⚠️",
            "info": "- ℹ️",
            "action": "- 🔍"
        }.get(level, "-")
        print(f"{prefix} {text}")
