import subprocess
from core.base_module import RedTeamModule
from rich import print

class PortScan(RedTeamModule):
    def __init__(self, target, options=None):
        super().__init__(target, options or {})
        self.ports = self.options.get("ports", None)

    def scan_ports(self):
        print(f"[bold cyan]### Scanning ports on {self.target}[/bold cyan]")
        nmap_cmd = ["nmap", "-Pn", "-T4"]

        if self.ports == "-p-":
            nmap_cmd += ["-p-", self.target]
        elif self.ports:
            nmap_cmd += ["-p", self.ports, self.target]
        else:
            nmap_cmd += ["-F", self.target]  # fast scan

        try:
            result = subprocess.run(nmap_cmd, capture_output=True, text=True, timeout=300)

            lines = result.stdout.splitlines()
            start = False
            print("\n[bold green]| PORT     | STATE  | SERVICE        |[/bold green]")
            print("[bold white]|----------|--------|----------------|[/bold white]")

            start = False
            for line in lines:
                if line.strip().startswith("PORT"):
                    start = True
                    continue
                if start and line.strip():
                    parts = line.strip().split()
                    if len(parts) >= 3:
                        port, state, service = parts[0], parts[1], ' '.join(parts[2:])
                        if state.lower() == "open":
                            print(f"[white]| {port:<8} | [bold green]{state:<6}[/bold green] | {service:<14} |[/white]")
                        elif state.lower() == "filtered":
                            print(f"[white]| {port:<8} | [bold yellow]{state:<6}[/bold yellow] | {service:<14} |[/white]")
                        elif state.lower() == "closed":
                            print(f"[white]| {port:<8} | [bold red]{state:<6}[/bold red] | {service:<14} |[/white]")
        except subprocess.TimeoutExpired:
            print("[red][!] Scan timed out[/red]")
        except Exception as e:
            print(f"[red][!] Error running scan: {e}[/red]")

    def run(self):
        self.scan_ports()