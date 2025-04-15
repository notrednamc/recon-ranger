#!/usr/bin/env python3

import argparse
# import logging
from core.utils import color_text, setup_logger
from core.banner import show_banner
import argparse
import sys
from modules.dns_enum import DNSModule
# from modules.osint import OSINTModule
from rich.console import Console

console = Console()

BANNER = """
[bold red]
██████  ███████ ██████       ████████ ███████  █████  ███    ███        ██████  ███████ ██████    ██████    ███    ██
██   ██ ██      ██    ██        ██    ██      ██   ██ ████  ████        ██   ██ ██      ██      ██      ██  ████   ██
██████  █████   ██    ██        ██    █████   ███████ ██ ████ ██        ██████  █████   ██      ██      ██  ██ ███ ██
██   ██ ██      ██    ██        ██    ██      ██   ██ ██  ██  ██        ██   ██ ██      ██      ██      ██  ██   ████
██   ██ ███████ ███████         ██    ███████ ██   ██ ██      ██        ██   ██ ███████ ██████    ██████    ██    ███
[/bold red]
"""

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
  dns_zone_transfer
  query_dns_records
  subdomain_enum
  reverse_dns_lookup
  check_dns_sec
  dns_service_version
  resolve_local_hostname
  query_crtsh

[bold cyan]Example:[/bold cyan]
  ./main.py dns subdomain_enum example.com
""")

def print_osint_help():
    console.print("""
[bold cyan]OSINT Module Help:[/bold cyan]

[bold yellow]Methods:[/bold yellow]
  whois
  email_harvest
  social_links
  pastebin_leaks
  breachdump_lookup

[bold cyan]Example:[/bold cyan]
  ./main.py osint whois example.com
""")

# Map module types to class and help function
module_map = {
    "dns": (DNSModule, print_dns_help),
    # "osint": (OSINTModule, print_osint_help),
}

def main():
    args = sys.argv

    if len(args) == 1 or args[1] in ("-h", "--help"):
        print_general_help()
        return

    module_type = args[1].lower()

    if module_type not in module_map:
        console.print(f"[red][!] Unknown module: {module_type}[/red]")
        return

    module_class, help_func = module_map[module_type]

    if len(args) == 3 and args[2] in ("-h", "--help"):
        help_func()
        console.print(f"\n[bold cyan]Available Methods in '{module_type}' module:[/bold cyan]")
        dummy = module_class("example.com")
        dummy.print_methods()
        return

    if len(args) == 3 and args[2] == "--list":
        console.print(f"[bold cyan]Available Methods in '{module_type}' module:[/bold cyan]")
        dummy = module_class("example.com")
        dummy.print_methods()
        return

    if len(args) < 4:
        console.print("[red][!] Not enough arguments[/red]\n")
        print_general_help()
        return

    method = args[2]
    target = args[3]

    extra_options = {}
    if len(args) > 4:
        for opt in args[4:]:
            if "=" in opt:
                key, val = opt.split("=", 1)
                extra_options[key.lstrip('-')] = val

    module_instance = module_class(target, options=extra_options)
    module_instance.run_method(method)
    
if __name__ == "__main__":
    main()