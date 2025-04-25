from core.base_module import RedTeamModule
import subprocess
import ipaddress
from rich import print as rprint

class HostDiscovery(RedTeamModule):
    def __init__(self, target, options=None):
        super().__init__(target, options or {})
        if self.options:
            rprint(f"[yellow]- Options passed are not needed for this module.")

    def host_discovery(self):
        rprint(f"[bold cyan]### Starting ping sweep on {self.target}[/bold cyan]")
        try:
            network = ipaddress.ip_network(self.target, strict=False)
        except ValueError as e:
            rprint(f"[red]- Invalid CIDR or IP range: {e}[/red]")
            return

        live_hosts = []

        for ip in network.hosts():
            ip_str = str(ip)
            try:
                result = subprocess.run(
                    ["ping", "-c", "1", "-W", "1", ip_str],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                if result.returncode == 0:
                    live_hosts.append(ip_str)
                    rprint(f"[green]- Host is up: {ip_str}[/green]")
            except Exception as e:
                rprint(f"[red]- Error pinging {ip_str}: {e}[/red]")

        if not live_hosts:
            rprint("[yellow]- No live hosts found[/yellow]")
        else:
            rprint(f"\n[bold green]- Found {len(live_hosts)} live host(s)[/bold green]")

        ## Add support for ip ranges, 192.168.1.50-100
        ## Add support for fqdn entered instead of ip address
        ## Add support for closed/blocked/WAF inturruptions.

    def run(self):
        self.host_discovery()