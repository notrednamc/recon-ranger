from rich import print as rprint
import requests

def get_subdomains_securitytrails(domain, api_key):
    rprint(f"\n[bold purple]#### Fetching subdomains from SecurityTrails...[/bold purple]")
    url = f"https://api.securitytrails.com/v1/domain/{domain}/subdomains"

    ## Set the APIKEY header to be used in the request
    headers = {"APIKEY": api_key}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            rprint(f"[red]- SecurityTrails error: {response.status_code} - {response.reason}[/red]")
            return set()

        data = response.json()
        subdomains = set(f"{sub}.{domain}" for sub in data.get("subdomains", []))
        return subdomains

    except Exception as e:
        rprint(f"[red][!] Error fetching SecurityTrails data: {e}[/red]")
        return set()