from core.base_module import RedTeamModule
from utils.method_loader import load_and_bind_methods
from core.utils import load_api_keys
from modules.sub_modules.get_all_subdomains import get_all_subdomains
from rich import print

class OSINTModule(RedTeamModule):
    def __init__(self, target, options=None):
        super().__init__(target, options)

        self.target = target
        self.api_keys = load_api_keys() or {}
        
        self.methods['get_all_subdomains'] = self.subdomain_lookup_wrapper

        load_and_bind_methods(self, {
            'whois_lookup'       : 'modules.sub_modules.whois_lookup.whois_lookup',
            'email_harvest'      : 'modules.sub_modules.email_harvest.email_harvest'
            # 'get_all_subdomains' : 'self.subdomain_lookup_wrapper'
        })

    def run(self):
        for method_name in self.methods:
            self.run_method(method_name)

    def _validate_file(self, path):
        try:
            with open(path, "r"):
                return True
        except:
            return False

    def subdomain_lookup_wrapper(self):
        print(f"\n[bold yellow]### Looking up subdomains for {self.target}[/bold yellow]")
        subdomains = get_all_subdomains(self.target, self.api_keys)

        for subdomain in subdomains:
            print(f"[cyan]- {subdomain}[/cyan]")

