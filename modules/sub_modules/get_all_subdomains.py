from rich import print as rprint
from modules.sub_modules.get_subdomains_securitytrails import get_subdomains_securitytrails
from modules.sub_modules.query_crtsh import query_crtsh

def get_all_subdomains(self):
    ## Create an empty list to combine results 
    all_subdomains = set()
    securitytrails_api_key = self.api_keys.get("securitytrails")
    
    ## TODO
    # Create check for each api key as the module to use it comes about.  

    
    crtsh_results = query_crtsh(self)
    if len(crtsh_results) == 0:
        rprint(f"\n[red]- No results returned![/red]")
    else:
        all_subdomains.update(crtsh_results)

    if securitytrails_api_key:
        all_subdomains.update(get_subdomains_securitytrails(self.target, securitytrails_api_key))
    
    # rprint(f"\n[purple]#### Found [white]{len(all_subdomains)}[/white] subdomains for [white][bold]{self.target}[/bold][/purple]")
    
    # for subdomain in sorted(all_subdomains):
    #     rprint(f"[green]- {subdomain}[/green]")
    
    # return sorted(all_subdomains)

