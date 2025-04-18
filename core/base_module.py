from abc import ABC, abstractmethod
from rich import print as rprint
from core.utils import load_api_keys
from core.utils import color_text

class RedTeamModule(ABC):
    def __init__(self, target, options=None):
        self.target = target
        self.options = options or {}
        self.results = []
        self.has_printed_header = False
        self.methods = {}
        self.api_keys = load_api_keys() or {}

    def bind_method(self, name, method):
        self.methods[name] = method.__get__(self)
    
    def run_method(self, method_name):
        ## Remove when support for .local is functional
        if self.target.endswith(".local"):
            print(color_text(f"- .local hostnames not supported", "red"))
            return
        
        method = self.methods.get(method_name)
        if not method:
            print(f"[!] Method `{method_name}` not found.")
            return
        
        ## Ensure the high level MD elements only print once.
        if not self.has_printed_header:
            if hasattr(self, "target") and self.target:
                rprint(f"\n[bold]# Recon Report for [white]`{self.target}`[/white][/bold]")
            rprint(f"\n[bold][yellow]## Running `{self.__class__.__name__}`[/yellow][/bold]")
            self.has_printed_header = True  # set it to True so it doesn’t repeat
        try:
            method()
        except Exception as e:
            print(f"[!] Error running `{method_name}`: {e}")

    @abstractmethod ## GPT suggestion, not sure I get it
    def run(self):
        pass

    # ## Logging not being used
    # def log_info(self, message):
    #     rprint(f"[blue][[INFO]][/blue] {message}")

    # def log_success(self, message):
    #     rprint(f"[green]✅ {message}[/green]")

    # def log_warning(self, message):
    #     rprint(f"[yellow]⚠️ {message}[/yellow]")

    # def log_error(self, message):
    #     rprint(f"[red]❌ {message}[/red]")

    # def markdown_header(self, title, level=2):
    #     prefix = "#" * level
    #     rprint(f"\n[purple]{prefix} {title}[/purple]")

    def add_result(self, result):
        if result:
            self.results.append(result)
