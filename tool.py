#!/usr/bin/env python3

import argparse
import logging
import os
from core.utils import color_text, setup_logger
from core.banner import show_banner
from modules import dns_enum

def clear_log():
    open("logs/debug.log", "w").close()

def main():
    clear_log()
    setup_logger()
    show_banner("name")

    parser = argparse.ArgumentParser(description="RedTeam Toolkit")
    parser.add_argument("module", help="Module to run (dns)")
    parser.add_argument("target", help="Target domain or IP")
    parser.add_argument("--wordlist", help="Path to subdomain wordlist", default="data/wordlists/subdomains.txt")
    parser.add_argument("--debug", help="Enable debug logging", action="store_true")
    args = parser.parse_args()

    if args.module == "dns":
        show_banner("hack")
        module = dns_enum.DNSModule(args.target, {"wordlist": args.wordlist, "debug": args.debug})
        module.run()
    else:
        print(color_text(f"[!] Unknown module '{args.module}'", "red"))

if __name__ == "__main__":
    main()
