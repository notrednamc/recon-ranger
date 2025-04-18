from core.utils import color_text
from rich.console import Console

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
    print(color_text("[ Red Team Modular Toolkit ]", "yellow"))