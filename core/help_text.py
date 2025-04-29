from rich.console import Console

console = Console()

def general_help():
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

def dns_help():
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

def osint_help():
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
    
def github_dorker_help():
    """
    Placeholder!!
    """

def whois_lookup_help():
    """
    Placeholder!!
    """

def query_crtsh_help():
    """
    Placeholder!!
    """

def host_discovery_help():
    """
    Placeholder!!
    """

def port_scan_help():
  """
  [bold cyan]PortScanModule - TCP Port Scanner[/bold cyan]

  Usage:
      python3 main.py port_scan [options] <target>

  Options:
      [green]--ports <list>[/green]       Comma-separated list of ports to scan (e.g. 22,80,443)
      [green]all[/green]                  Scan all 65535 TCP ports

  Notes:
      • Host discovery is disabled by default ([cyan]-Pn[/cyan] is always used).
      • The scanner assumes all specified targets are online.

  Examples:
      python3 main.py port_scan --ports 22,80,443 target.com
      python3 main.py port_scan -p- 192.168.1.0/24
  """

