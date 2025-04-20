from dns.exception import DNSException
from dns import resolver
from rich import print as rprint

def query_dns_records(self):
    rprint("\n[bold cyan]### DNS Record Enumeration [/bold cyan]")
    record_types = ['A', 'MX', 'NS', 'TXT', 'CNAME', 'SOA']
    for record in record_types:
        try:
            rprint(f"\n[bold purple]#### Querying {record} records for {self.target}[/bold purple]")
            answers = resolver.resolve(self.target, record)
            for rdata in answers:
                rprint(f"[green]- {record} record: {rdata}[/green]")
        except DNSException as e:
            rprint(f"[red]- {record} record query failed: {e}[/red]")