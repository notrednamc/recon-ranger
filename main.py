#!/usr/bin/env python3

import argparse
# import logging
from core.utils import color_text, setup_logger
from core.banner import show_banner
import argparse
import sys
from modules.dns_enum import DNSModule
from modules.osintel import OSINTModule
from modules.sub_modules import whois_lookup
from rich.console import Console
from core import banner
from core.help_text import print_dns_help, print_general_help, print_osint_help

console = Console()

banner.show_banner("label")

# Map module types to class and help function
module_map = {
    "dns"   : (DNSModule, print_dns_help),
    "osint" : (OSINTModule, print_osint_help),
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

    if method.lower() == "all":
        console.print(f"[bold green][ Running all methods in '{module_type}' module against '{target}' ][/bold green]")
        for method_name in module_instance.methods:
            module_instance.run_method(method_name)
    else:
        module_instance.run_method(method)

    
if __name__ == "__main__":
    main()