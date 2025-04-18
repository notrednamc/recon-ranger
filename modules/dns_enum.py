from core.base_module import RedTeamModule
from core.utils import get_default_wordlist, load_and_bind_methods

class DNSModule(RedTeamModule):
    def __init__(self, target, options=None):
        super().__init__(target, options)
        
        ## Load the target and default wordlislt into self
        self.target = target
        self.default_subdomains_wordlist = self.options.get("wordlist") or get_default_wordlist()
        
        ## Load the method name, mapped to the function into self
        load_and_bind_methods(self, {
            'dns_zone_transfer'      : 'modules.sub_modules.dns_zone_transfer.dns_zone_transfer',
            'query_dns_records'      : 'modules.sub_modules.query_dns_records.query_dns_records',
            'subdomain_enum'         : 'modules.sub_modules.subdomain_enum.subdomain_enum',
            'reverse_dns_lookup'     : 'modules.sub_modules.reverse_dns_lookup.reverse_dns_lookup',
            'check_dns_sec'          : 'modules.sub_modules.check_dns_sec.check_dns_sec',
            'dns_service_version'    : 'modules.sub_modules.dns_service_version.dns_service_version',
            # 'resolve_local_hostname' : 'modules.sub_modules.resolve_local_hostname.resolve_local_hostname',
            'query_crtsh'            : 'modules.sub_modules.query_crtsh.query_crtsh',
        })

    # Run method
    def run(self):
        for method_name in self.methods:
            self.run_method(method_name)

    # ## Not in use
    # def _validate_file(self, path):
    #     try:
    #         with open(path, "r"):
    #             return True
    #     except:
    #         return False