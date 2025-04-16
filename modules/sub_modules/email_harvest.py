from rich import print
import requests
import re

def email_harvest(self):
    if not hasattr(self, "target"):
        print("[red]- No target set.[/red]")
        return

    domain = self.target
    print(f"\n[bold yellow]### Searching for email addresses related to {domain}[/bold yellow]")

    try:
        # Query crt.sh for the domain
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        resp = requests.get(url, timeout=10)

        if resp.status_code != 200:
            print(f"[red][!] Failed to fetch data from crt.sh[/red]")
            return

        data = resp.json()
        emails = set()

        for entry in data:
            name_value = entry.get("name_value", "")
            matches = re.findall(r"[a-zA-Z0-9_.+-]+@" + re.escape(domain), name_value)
            emails.update(matches)

        if emails:
            print(f"[bold green]#### Found {len(emails)} emails:[/bold green]")
            for email in sorted(emails):
                print(f"[cyan]- {email}[/cyan]")
        else:
            print("[yellow]- No emails found[/yellow]")

    except Exception as e:
        print(f"[red][!] Error during email harvesting: {e}[/red]")
