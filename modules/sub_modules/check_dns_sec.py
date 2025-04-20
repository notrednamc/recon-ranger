from rich import print as  rprint
import subprocess

def check_dns_sec(self):
    print(f"\n[cyan]### DNSSEC Check for {self.target}[/cyan]")
    try:
        output = subprocess.check_output(f"dig +dnssec {self.target}", shell=True)
        decoded = output.decode().lower()
        
        ## ad denotes the presense of dnssec
        if 'ad' in decoded:
            print(f"[green]- DNSSEC is enabled for {self.target}[/green]")
        else:
            print(f"[red]- DNSSEC not detected for {self.target}[/red]")
    except subprocess.CalledProcessError as e:
        rprint(f"[red]- DNSSEC check failed: {e}[/red]")