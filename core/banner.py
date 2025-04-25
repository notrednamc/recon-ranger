from rich.console import Console
from rich import print as rprint

console = Console()

def show_banner(name: str=""):
    banners = {
        "name"  : banner_name
    }

    banner = banners.get(name, banner_name)()

def banner_name():
    banner = r"""
    [bold red]
    ██████  ███████ ██████       ████████ ███████  █████  ███    ███        ██████  ███████ ██████    ██████    ███    ██
    ██   ██ ██      ██    ██        ██    ██      ██   ██ ████  ████        ██   ██ ██      ██      ██      ██  ████   ██
    ██████  █████   ██    ██        ██    █████   ███████ ██ ████ ██        ██████  █████   ██      ██      ██  ██ ███ ██
    ██   ██ ██      ██    ██        ██    ██      ██   ██ ██  ██  ██        ██   ██ ██      ██      ██      ██  ██   ████
    ██   ██ ███████ ███████         ██    ███████ ██   ██ ██      ██        ██   ██ ███████ ██████    ██████    ██    ███
    [/bold red]
"""
    console.print(banner)
    rprint("[bold yellow][ Red Team Modular Toolkit ][/bold yellow]")