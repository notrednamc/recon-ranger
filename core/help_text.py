from rich.console import Console

console = Console()

def print_general_help():
    console.print("""
[bold cyan]Usage:[/bold cyan]
  ./main.py <module> <method> <target> [--options]

[bold cyan]Modules:[/bold cyan]
  dns         Perform DNS-based recon
  osint       Open Source Intelligence (OSINT) recon
  kitchen     Run everything at once
  close       Finish recon session

[bold cyan]Examples:[/bold cyan]
  ./main.py -h
  ./main.py dns -h
  ./main.py dns subdomain_enum example.com
  ./main.py osint whois example.com
  ./main.py dns --list
""")

def print_dns_help():
    console.print("""
[bold cyan]DNS Module Help:[/bold cyan]

[bold yellow]Methods:[/bold yellow]
  dns_zone_transfer         : DNS Zone Transfer
  query_dns_records         : Query DNS Records
  subdomain_enum            : Subdomain Enumeration/Bruteforcing
  reverse_dns_lookup        : Reverse DNS Lookup
  check_dns_sec             : Check DNSSec
  dns_service_version       : DNS Service Version
  resolve_local_hostname    : Resolve Local Hostname
  query_crtsh               : Query Certsh

[bold cyan]Example:[/bold cyan]
  ./main.py dns subdomain_enum example.com
  ./main.py dns subdomain_enum example.com --wordlist /path/to/list
""")

def print_osint_help():
    console.print("""
[bold cyan]OSINT Module Help:[/bold cyan]

[bold yellow]API Keys:[/bold yellow]                  
[bold green][!] If you have API Keys for the selected module add them to config/api_keys.txt[/bold green]

[bold yellow]Methods:[/bold yellow]
  whois
  email_harvest
  social_links
  pastebin_leaks
  breachdump_lookup

[bold cyan]Example:[/bold cyan]
  ./main.py osint whois example.com
""")