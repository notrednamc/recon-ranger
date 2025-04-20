import requests
from rich import print as rprint

def query_crtsh(domain):
    rprint(f"\n[bold cyan]### Passive subdomain lookup with certsh + {domain.target}[/bold cyan]")
    url = f"https://crt.sh/?q=%25.{domain.target}&output=json"

    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            rprint(f"[red]- crt.sh error: {response.status_code}[/red]")
            return set()

        data = response.json()
        if not data:
            rprint(f"[red]- No subdomains found [/red]")
        subdomains = set()
        
        for entry in data:
            name_value = entry.get("name_value", "")
            for sub in name_value.split("\n"):
                if domain.target in sub:
                    subdomains.add(sub.strip())
        
        rprint(f"\n[purple]#### Found [white]{len(subdomains)}[/white] subdomains for [white][bold]{domain.target}[/bold][/purple]")
        
        for subdomain in sorted(subdomains):    
            rprint(f"[green]- {subdomain}[/green]") 
        return subdomains

    except Exception as e:
        rprint(f"[red]- Error fetching crt.sh data: {e}[/red]")
        return set()