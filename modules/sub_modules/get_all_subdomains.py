from urllib.parse import quote
from rich import print as rprint
from modules.sub_modules import get_subdomains_securitytrails
from modules.sub_modules import query_crtsh

def get_all_subdomains(self, api_keys={}):
    all_subdomains = set()
    target = self.target
    securitytrails_api_key = self.api_keys.get("securitytrails")
    
    all_subdomains.update(query_crtsh(target))
    
    if not self.api_keys:
        print("No API keys available.")
        
    all_subdomains.update(get_subdomains_securitytrails(target, securitytrails_api_key))

    rprint(f"\n[*] Found {len(all_subdomains)} subdomains for [cyan]{target}[/cyan].")
    # print(f"\n[green]- {all_subdomains}[/green].")
    return sorted(all_subdomains)
