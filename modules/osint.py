from core.base_module import RedTeamModule
from core.utils import color_text
from utils.method_loader import load_and_bind_methods

class OSINTModule(RedTeamModule):
    def __init__(self, target, options=None):
        super().__init__(target, options)
        self.target = target

        load_and_bind_methods(self, {
            'whois': 'modules.osint.whois.whois_lookup',
            'email_harvest': 'modules.osint.email_harvest.email_harvest',
            'social_links': 'modules.osint.social_links.social_links',
            'pastebin_leaks': 'modules.osint.pastebin_leaks.pastebin_leaks',
            'breachdump_lookup': 'modules.osint.breachdump_lookup.breachdump_lookup',
        })

    def run(self):
        print(color_text(f"# OSINT Report for `{self.target}`", "cyan"))
        self.whois()
        self.email_harvest()
        self.social_links()
        self.pastebin_leaks()
        self.breachdump_lookup()
