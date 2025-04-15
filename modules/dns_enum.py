from core.base_module import RedTeamModule
from core.utils import color_text
from termcolor import colored
from utils.file_helpers import get_default_wordlist
from utils.method_loader import load_and_bind_methods

class DNSModule(RedTeamModule):
    def __init__(self, target, options=None):
        super().__init__(target, options)
        
        self.target = target
        self.default_subdomains_wordlist = self.options.get("wordlist") or get_default_wordlist()
        
        load_and_bind_methods(self, {
            'dns_zone_transfer'      : 'modules.dns.dns_zone_transfer.dns_zone_transfer',
            'query_dns_records'      : 'modules.dns.query_dns_records.query_dns_records',
            'subdomain_enum'         : 'modules.dns.subdomain_enum.subdomain_enum',
            'reverse_dns_lookup'     : 'modules.dns.reverse_dns_lookup.reverse_dns_lookup',
            'check_dns_sec'          : 'modules.dns.check_dns_sec.check_dns_sec',
            'dns_service_version'    : 'modules.dns.dns_service_version.dns_service_version',
            'resolve_local_hostname' : 'modules.dns.resolve_local_hostname.resolve_local_hostname',
            'query_crtsh'            : 'modules.dns.query_crtsh.query_crtsh',
        })


    def print_methods(self):
        print("\nAvailable DNS methods:")
        for method in [
            'dns_zone_transfer',
            'query_dns_records',
            'subdomain_enum',
            'reverse_dns_lookup',
            'check_dns_sec',
            'dns_service_version',
            'resolve_local_hostname',
            'query_crtsh'
        ]:
            if hasattr(self, method):
                print(f"  - {method}")

    def run(self):
        print(colored(f"# DNS Recon Report for `{self.target}`", "white", attrs=["bold"]))
        for method_name in self.methods:
            self.run_method(method_name)

    def _validate_file(self, path):
        try:
            with open(path, "r"):
                return True
        except:
            return False
