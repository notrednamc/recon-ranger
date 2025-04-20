from zeroconf import Zeroconf, ServiceBrowser, ServiceListener
from core.utils import color_text
import socket
import time
from rich import print as rprint

class HostnameResolver(ServiceListener):
    def __init__(self, target):
        self.target = target
        self.resolved_ip = None

    def remove_service(self, zeroconf, type, name):
        pass

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        if info and self.target in name:
            addresses = info.parsed_addresses()
            if addresses:
                self.resolved_ip = addresses[0]

    def update_service(self, zeroconf, type, name):
        pass

def resolve_local_hostname(target):
    rprint(color_text("\n### Resolving hostname with zeroconf", "cyan"))

    zeroconf = Zeroconf()
    listener = HostnameResolver(target)

    # Browse all services to find one matching the hostname
    browser = ServiceBrowser(zeroconf, "_services._dns-sd._udp.local.", listener)

    # Give some time for discovery
    time.sleep(2)

    zeroconf.close()

    if listener.resolved_ip:
        rprint(color_text(f"- Resolved {target} to {listener.resolved_ip}", "green"))
        return listener.resolved_ip
    else:
        rprint(color_text(f"- Could not resolve {target}", "red"))
        return None
