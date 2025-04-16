import requests
from rich import print as rprint



def query_crtsh(domain):
    rprint("[bold purple]\n#### Fetching subdomains from crt.sh...[/bold purple]")
    url = f"https://crt.sh/?q=%25.{quote(domain)}&output=json"

    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print(f"[red][!] crt.sh error: {response.status_code}[/red]")
            return set()

        data = response.json()
        subdomains = set()

        for entry in data:
            name_value = entry.get("name_value", "")
            for sub in name_value.split("\n"):
                if domain in sub:
                    subdomains.add(sub.strip())

        return subdomains

    except Exception as e:
        print(f"[red][!] Error fetching crt.sh data: {e}[/red]")
        return set()