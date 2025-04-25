from rich import print as rprint
from whois import whois
from core.base_module import RedTeamModule

class WhoIsLookup(RedTeamModule):
    def __init__(self, target, options=None):
        super().__init__(target, options or {})
        if self.options:
            rprint(f"[yellow]- Options passed are not needed for this module.")
        
    def whois_lookup(self):
        try:
            rprint(f"\n[bold cyan]### Looking up Whois information[/bold cyan]")
            result = whois(self.target)
            rprint(f"\n[bold purple]#### WHOIS results for {self.target}:[/bold purple]")
            for key, value in result.items():
                if isinstance(value, list):
                    value = ', '.join(map(str, value))
                rprint(f"[cyan]- {key}[/cyan]: {value}")
        except Exception as e:
            rprint(f"[red][!] Error during WHOIS lookup: {e}[/red]")

    def run(self):
        self.whois_lookup()
        