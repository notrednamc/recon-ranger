import requests
from rich import print as rprint
from urllib.parse import quote

def query_crtsh(domain):
    rprint("[bold cyan]\n### Fetching subdomains from crt.sh...[/bold cyan]")
    url = f"https://crt.sh/?q=%25.{domain}&output=json"

    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print(f"[red][!] crt.sh error: {response.status_code}[/red]")
            return set()

        data = response.json()
        if not data:
            rprint(f"[red]- No subdomains found [/red]")
        subdomains = set()
        
        for entry in data:
            name_value = entry.get("name_value", "")
            for sub in name_value.split("\n"):
                if domain in sub:
                    subdomains.add(sub.strip())

        return subdomains

    except Exception as e:
        print(f"[red]- Error fetching crt.sh data: {e}[/red]")
        return set()