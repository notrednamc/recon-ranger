import socket
import subprocess
from modules.sub_modules.resolve_local_hostname import resolve_local_hostname
from rich import print as rprint

def dns_zone_transfer(self):
    rprint(f"\n[cyan]### DNS Zone Transfer for {self.target}[/cyan]")

    try:
        # Check if target ends in .local and resolve accordingly
        if self.target.endswith(".local"):
            resolved_ip = resolve_local_hostname(self.target)  # <-- Your Zeroconf handler
        else:
            try:
                resolved_ip = socket.gethostbyname(self.target)  # <-- Regular DNS resolution
            except socket.gaierror as e:
                rprint(f"[red]- DNS resolution failed for {self.target}: {e}[/red]")
                return

        if not resolved_ip:
            rprint("[red]- Could not resolve hostname. Skipping AXFR.[/red]")
            return

        rprint(f"[yellow]- Attempting to resolve hostname: {self.target}[/yellow]")
        rprint(f"[green]- Resolved {self.target} to {resolved_ip}[/green]")

        # Dig AXFR attempt
        output = subprocess.check_output(
            f"dig @{resolved_ip} AXFR", shell=True, stderr=subprocess.STDOUT
        ).decode().strip()

        if not output:
            rprint("[yellow]- Zone transfer completed but returned no results.[/yellow]")
        elif "Transfer failed" in output or "connection timed out" in output.lower():
            rprint(f"[red]- Zone transfer failed:\n{output}[/red]")
        else:
            rprint("\n[green]#### Zone Transfer Output\n" + output + "[/green]")

    except subprocess.CalledProcessError as e:
        rprint(f"[red]- Zone transfer failed: {e.output.decode().strip()}[/red]")
