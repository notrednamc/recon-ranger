from core.base_module import RedTeamModule
import subprocess
import ipaddress
import socket
import re
from rich import print as rprint


class HostDiscovery(RedTeamModule):
    def __init__(self, target, options=None):
        super().__init__(target, options or {})
        if self.options:
            rprint(f"[yellow]- Options passed are not needed for this module.[/yellow]")

    def resolve_target(self, target):
        try:
            return socket.gethostbyname(target)
        except socket.gaierror:
            rprint(f"[red]- Could not resolve FQDN: {target}[/red]")
            return None

    def parse_range(self, target):
        match = re.match(r"(\d+\.\d+\.\d+\.)(\d+)-(\d+)", target)
        if not match:
            rprint(f"[red]- Invalid IP range format: {target}[/red]")
            return []

        base, start, end = match.groups()
        return [f"{base}{i}" for i in range(int(start), int(end) + 1)]

    def ping_host(self, ip_str):
        try:
            result = subprocess.run(
                ["ping", "-c", "1", "-W", "1", ip_str],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            return result.returncode == 0
        except Exception as e:
            rprint(f"[red]- Error pinging {ip_str}: {e}[/red]")
            return False

    def host_discovery(self):
        rprint(f"[bold cyan]### Starting ping sweep on {self.target}[/bold cyan]")

        # Detect and expand target
        targets = []

        if re.match(r"\d+\.\d+\.\d+\.\d+/\d+", self.target):  # CIDR
            try:
                network = ipaddress.ip_network(self.target, strict=False)
                targets = [str(ip) for ip in network.hosts()]
            except ValueError as e:
                rprint(f"[red]- Invalid CIDR: {e}[/red]")
                return

        elif re.match(r"\d+\.\d+\.\d+\.\d+-\d+", self.target):  # IP range
            targets = self.parse_range(self.target)

        elif re.match(r"\d+\.\d+\.\d+\.\d+", self.target):  # Single IP
            targets = [self.target]

        else:  # FQDN
            resolved_ip = self.resolve_target(self.target)
            if resolved_ip:
                targets = [resolved_ip]
            else:
                return

        if not targets:
            rprint(f"[red]- No valid targets found[/red]")
            return

        live_hosts = []

        for ip in targets:
            if self.ping_host(ip):
                rprint(f"[green]- Host is up: {ip}[/green]")
                live_hosts.append(ip)
            else:
                rprint(f"[yellow]- No reply (possibly filtered): {ip}[/yellow]")

        if live_hosts:
            rprint(f"\n[bold green]- Found {len(live_hosts)} live host(s)[/bold green]")
        else:
            rprint("[yellow]- No live hosts found[/yellow]")

    def run(self):
        self.host_discovery()
