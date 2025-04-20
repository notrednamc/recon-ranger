from rich import print as rprint
import socket

def reverse_dns_lookup(self):
    rprint("\n[cyan]### Performing Reverse DNS Lookup[/cyan]")
    try:
        ip = socket.gethostbyname(self.target)
        hostname, _, _ = socket.gethostbyaddr(ip)
        rprint(f"[green]- {ip} resolves to {hostname}[/green]")
    except Exception as e:
        rprint(f"[red]- Reverse lookup failed: {e}[/red]")