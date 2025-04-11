#!/usr/bin/env python3

import argparse
import logging
import os
from core.utils import color_text, setup_logger
from core.banner import show_banner
from modules import dns_enum

import argparse
import sys
from modules.dns_enum import DNSModule
from modules.osint import OSINTModule
from rich import print as rprint
from rich.console import Console

console = Console()

BANNER = """
[bold cyan]
██████  ███████ ██████       ████████ ███████  █████  ███    ███ 
██   ██ ██      ██    ██        ██    ██      ██   ██ ████  ████ 
██████  █████   ██    ██        ██    █████   ███████ ██ ████ ██ 
██   ██ ██      ██    ██        ██    ██      ██   ██ ██  ██  ██ 
██   ██ ███████ ███████         ██    ███████ ██   ██ ██      ██ 
[/bold cyan]
"""

def select_module_menu():
    rprint("[bold green]Select a module:[/bold green]")
    print("  [1] DNS Enumeration")
    print("  [2] OSINT Collection")
    print("  [3] Run All")
    print("  [0] Exit")

    choice = input("\nChoice: ")
    return choice.strip()

def run_modules(module_choice, target, options):
    if module_choice == "1":
        DNSModule(target, options).run()
    elif module_choice == "2":
        OSINTModule(target, options).run()
    elif module_choice == "3":
        rprint(f"\n## 🎯 Starting full recon for `{target}`\n")
        DNSModule(target, options).run()
        OSINTModule(target, options).run()
    elif module_choice == "0":
        rprint("[bold yellow]Exiting...[/bold yellow]")
        sys.exit(0)
    else:
        rprint("[bold red]Invalid choice![/bold red]")
        sys.exit(1)

def main():
    console.print(BANNER)
    parser = argparse.ArgumentParser(description="🔧 Red Team Recon Framework")
    parser.add_argument("target", nargs="?", help="Target domain or IP (e.g., example.com)")
    parser.add_argument("--module", choices=["osint", "dns", "all"], help="Module to run")
    parser.add_argument("--wordlist", help="Path to wordlist for subdomain brute-force")
    parser.add_argument("--hunterio", help="Hunter.io API Key")
    parser.add_argument("--shodan", help="Shodan API Key")
    parser.add_argument("--github", help="GitHub Token")

    args = parser.parse_args()
    options = {
        "wordlist": args.wordlist,
        "hunterio_api_key": args.hunterio,
        "shodan_api_key": args.shodan,
        "github_token": args.github,
    }

    if args.target and args.module:
        run_modules(args.module if args.module != "all" else "3", args.target, options)
    else:
        # Interactive mode
        target = args.target or input("Target domain or IP: ").strip()
        choice = select_module_menu()
        run_modules(choice, target, options)

if __name__ == "__main__":
    main()

