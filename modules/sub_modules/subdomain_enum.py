
from core.utils import get_default_wordlist
import socket
from rich import print as rprint

def subdomain_enum(self):
    ## Load provided wordlist, or get the default
    wordlist = self.options.get("wordlist") or get_default_wordlist()

    ## Validate the file
    if not self._validate_file(wordlist):
        rprint(f"[red]- Wordlist not found or unreadable: {wordlist}[/red]")
        return

    rprint(f"\n[bold cyan]### Brute-forcing subdomains using {wordlist}[/bold cyan]")
    rprint(f"[green]- Wordlist: `{wordlist}`[/green]")
    
    try:
        with open(wordlist, "r") as file:
            for line in file:
                subdomain = line.strip()
                fqdn = f"{subdomain}.{self.target}"
                try:
                    ip = socket.gethostbyname(fqdn)
                    rprint(f"[green]- Found: {fqdn} -> {ip}[/green]")
                except Exception:
                    rprint(f"[red]- {fqdn}[/red]")
    except Exception as e:
        msg = f"Error reading wordlist: {e}"
        rprint(f"[red]{msg}[/red]")