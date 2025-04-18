from core.utils import color_text
from dns.exception import DNSException
from dns import resolver

def query_dns_records(self):
    print(color_text("\n### DNS Record Enumeration", "cyan"))
    record_types = ['A', 'MX', 'NS', 'TXT', 'CNAME', 'SOA']
    for record in record_types:
        try:
            print(color_text(f"\n#### Querying {record} records for {self.target}", "cyan"))
            answers = resolver.resolve(self.target, record)
            for rdata in answers:
                print(color_text(f"- {record} record: {rdata}", "green"))
        except DNSException as e:
            print(color_text(f"- {record} record query failed: {e}", "red"))