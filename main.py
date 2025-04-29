#!/usr/bin/env python3

from pathlib import Path
from rich.console import Console
import argparse
from core.banner import show_banner
from core.help_text import *

from profiles.dns import DNSModule
from profiles.osint import OSINTModule

from modules.github_scraper import GitHubDorker
from modules.whois_lookup import WhoIsLookup
from modules.query_crtsh import QueryCrtsh
from modules.host_discovery import HostDiscovery
from modules.port_scan import PortScan

console = Console()
show_banner("label")

# Profile map
profile_map = {
    "dns": (DNSModule, dns_help),
    "osint": (OSINTModule, osint_help)
}

# Module map
module_map = {
    "github_dorker"  : (GitHubDorker, github_dorker_help),
    "whois_lookup"   : (WhoIsLookup, whois_lookup_help),
    "query_crtsh"    : (QueryCrtsh, query_crtsh_help),
    "host_discovery" : (HostDiscovery, host_discovery_help),
    "port_scan"      : (PortScan, port_scan_help)
}

def main():
    parser = argparse.ArgumentParser(
        description="Red Team Toolkit CLI",
        usage="main.py --module MODULE --target TARGET [--ports PORTS]"
    )
    
    parser.add_argument("--module", required=True, help="Module or profile to run (e.g., port_scan, dns)")
    parser.add_argument("--target", required=True, help="Target IP/domain/CIDR")
    parser.add_argument("--ports", help="Comma-separated ports (only applies to port_scan)")
    
    # Expand here for future shared options
    # parser.add_argument("--api-key", help="Optional API key for tools that support it")

    args = parser.parse_args()
    
    extra_options = {}
    if args.ports:
        extra_options["ports"] = args.ports

    keyword = args.module.lower()
    target = args.target

    # === Profile ===
    if keyword in profile_map:
        profile_class, help_func = profile_map[keyword]

        try:
            profile_instance = profile_class(target, options=extra_options)
        except ValueError as e:
            console.print(f"[red][!] Error: {e}[/red]")
            return
        
        console.print(f"[bold green][ Running profile '{keyword}' against '{target}' ][/bold green]")
        if hasattr(profile_instance, "run"):
            profile_instance.run()
        else:
            console.print(f"[red][!] Profile '{keyword}' is missing a .run() method[/red]")
        return

    # === Tool ===
    if keyword in module_map:
        tool_class, help_func = module_map[keyword]

        try:
            tool_instance = tool_class(target, options=extra_options)
        except ValueError as e:
            console.print(f"[red][!] Error: {e}[/red]")
            return
        
        console.print(f"[bold green][ Running tool '{keyword}' against '{target}' ][/bold green]")
        if hasattr(tool_instance, "run"):
            tool_instance.run()
        else:
            console.print(f"[red][!] Tool '{keyword}' is missing a .run() method[/red]")
        return

    # === Unknown ===
    console.print(f"[red][!] Unknown module or profile: '{keyword}'[/red]")
    general_help()

if __name__ == "__main__":
    main()
