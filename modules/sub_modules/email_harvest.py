from rich import print as rprint
import requests
import re

def email_harvest(self):
    ## Ensure valid target is present.
    if not hasattr(self, "target"):
        print("[red]- No target set.[/red]")
        return

    domain = self.target
    rprint(f"\n[bold cyan]### Searching for email addresses related to {domain}[/bold cyan]")

    try:
        # Query crt.sh for the domain
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        resp = requests.get(url, timeout=10)

        if resp.status_code != 200:
            rprint(f"[red]- Failed to fetch data from crt.sh[/red]")
            return

        ## Load the response into data for email scrape
        data = resp.json()
        emails = set()

        for entry in data:
            name_value = entry.get("name_value", "")
            matches = re.findall(r"[a-zA-Z0-9_.+-]+@" + re.escape(domain), name_value)
            emails.update(matches)

        if emails:
            rprint(f"[bold green]#### Found {len(emails)} emails:[/bold green]")
            for email in sorted(emails):
                rprint(f"[cyan]- {email}[/cyan]")
        else:
            rprint("[yellow]- No emails found[/yellow]")

    except Exception as e:
        rprint(f"[red][!] Error during email harvesting: {e}[/red]")
