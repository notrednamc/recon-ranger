from rich import print as rprint
from modules.sub_modules.get_subdomains_securitytrails import get_subdomains_securitytrails
from modules.sub_modules.query_crtsh import query_crtsh

def get_all_subdomains(target, api_keys):
    ## Create an empty list to combine results 
    all_subdomains = set()
    securitytrails_api_key = api_keys.get("securitytrails")
    
    ## TODO Create a way to load all api keys, reflect properly loaded to the console.
    if not securitytrails_api_key:
        print("[!] No API key for SecurityTrails provided.")
        return []
    
    crtsh_results = query_crtsh(target)
    if len(crtsh_results) == 0:
        rprint(f"\n[red]- No results returned![/red]")
    else:
        all_subdomains.update(crtsh_results)
        rprint(f"\n[green]- Found [white]{len(all_subdomains)}[/white] subdomains[/green]")

    if securitytrails_api_key:
        all_subdomains.update(get_subdomains_securitytrails(target, securitytrails_api_key))
    
    rprint(f"\n[yellow]### Found [white]{len(all_subdomains)}[/white] subdomains for[/yellow] [white][bold]{target}[/bold][/white]")
    return sorted(all_subdomains)

