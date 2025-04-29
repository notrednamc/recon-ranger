from core.base_module import RedTeamModule
from core.utils import load_and_bind_methods
# from profiles.sub_modules.get_all_subdomains import get_all_subdomains
from rich import print as rprint
from modules.github_scraper import GitHubDorker


class OSINTModule(RedTeamModule):
    def __init__(self, target, options=None):
        super().__init__(target, options)

        ## Load the target and API keys into self
        self.target = target
        # self.api_keys = load_api_keys() or {}
        

        ## Doesn't get loaded in the load_and_bind_methods method, not sure why.
        # self.methods['get_all_subdomains'] = self.subdomain_lookup_wrapper

        ## Load the method name, mapped to the function into self
        # load_and_bind_methods(self, {
            # subdomain lookup executes first ^^^
            # 'whois_lookup'       : 'modules.sub_modules.whois_lookup.whois_lookup',
            # 'email_harvest'      : 'modules.sub_modules.email_harvest.email_harvest',
            # 'get_all_subdomains' : 'modules.sub_modules.get_all_subdomains.get_all_subdomains'
            # 'trufflehog'         : 'modules.submodules.trufflehog
            # 'github'             : 'tools.github_scraper.GitHubDorker'
            # 'google'             : 'modules.submodules.google
            # 'haveibeenpwned'     : 'modules.submodules.hibp
        # })

    # Run method
    def run(self):
        githubdorker = GitHubDorker(self.target, options={})
        githubdorker.run()
        # for method_name in self.methods:
        #     self.run_method(method_name)

    ## Wrapper for get_all_subdomains to call ALL subdomain methods
    # def subdomain_lookup_wrapper(self):   
    #     subdomains = get_all_subdomains(self.target, self.api_keys)
    #     for subdomain in subdomains:
    #         rprint(f"[green]- {subdomain}[/green]")

    # ## Not in use
    # def _validate_file(self, path):
    #     try:
    #         with open(path, "r"):
    #             return True
    #     except:
    #         return False

    

