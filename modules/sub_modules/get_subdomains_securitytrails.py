from rich import print as rprint
import requests

def get_subdomains_securitytrails(domain, api_key):
    rprint(f"\n[bold cyan]### Fetching subdomains from SecurityTrails...[/bold cyan]")
    url = f"https://api.securitytrails.com/v1/domain/{domain}/subdomains"
    
    ## Set the APIKEY header to be used in the request
    headers = {"APIKEY": api_key}
    response = requests.get(url, headers=headers, timeout=10)
    error_responses = {
            "401" : rprint(f"[red]- API Key Error: {response.status_code} - {response.reason}[/red]"),
            "302" : rprint(f"[yellow]- Redirect Encountered: {response.status_code} - {response.reason}[/yellow]"),
        }
    try:
        if response.status_code != 200:
            ## If both 401 and 302 happen, its because its unauthorized and was redirected.
            if   response.status_code == 401: error_responses["401"]
            elif response.status_code == 302: error_responses["302"]
            return set()
       
        data = response.json()
        subdomains = {f"{sub}.{domain}" for sub in data.get("subdomains", [])}
        return subdomains
        

    except Exception as e:
        rprint(f"[red][!] Error fetching SecurityTrails data: {e}[/red]")
        return set()