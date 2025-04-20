from rich import print
from whois import whois

def whois_lookup(self):
    if not hasattr(self, "target"):
        print("[red]- No target set.[/red]")
        return
    try:
        print(f"\n[bold cyan]### Looking up Whois information[/bold cyan]")
        result = whois(self.target)
        print(f"\n[bold purple]#### WHOIS results for {self.target}:[/bold purple]")
        for key, value in result.items():
            if isinstance(value, list):
                value = ', '.join(map(str, value))
            print(f"[cyan]- {key}[/cyan]: {value}")
    except Exception as e:
        print(f"[red][!] Error during WHOIS lookup: {e}[/red]")


        