from core.utils import color_text, setup_logger
from termcolor import colored
from rich.console import Console

console = Console()

def show_banner(name: str=""):
    banners = {
        "name"  : banner_name,
        "alive" : banner_alive,
        "battle": banner_battle,
        "sleep" : banner_sleep,
        "recon" : banner_recon,
        "hack"  : banner_hack
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
    # print(color_text(banner, "cyan"))
    print(color_text("[ Red Team Modular Toolkit ]", "yellow"))

def banner_alive():
    banner = r"""
           ___
          [o o]     ________
         /  V  \   | Johnny |
        /| === |\  |   5    |
       /_|_____|_\ |--------|
         || ||     |  IS    |
        (_)(_)     | ALIVE! |
        ||  ||     |________|
     ___||__||___
    /   ||  ||   \
   |____||__||____|
    (__)    (__)
"""
    print(color_text(banner, "green"))

def banner_battle():
    banner = r"""
           ___
          [⚙⚙]     ________
         / >_< \  | Johnny |
        /|  X  |\ |   5    |
       /_|_____|_\|--------|
         || ||     | TARGET|
        (__)(__)   |ACQUIRED|
        ||  ||     |________|
     ___||__||___
    /   ||  ||   \
   |____||__||____|
    (__)    (__)
"""
    print(color_text(banner, "red"))

def banner_sleep():
    banner = r"""
           ___
          [- -]     ________
         /  zZ  \  | Johnny |
        /|  ... |\ |   5    |
       /_|_____|_\ |--------|
         || ||     |  SLEEP |
        (__)(__)   |  MODE  |
        ||  ||     |________|
     ___||__||___
    /   ||  ||   \
   |____||__||____|
    (__)    (__)
"""
    print(color_text(banner, "yellow"))

def banner_recon():
    banner = r"""
           ___
         [🔍  o]    ________
         \ o__/   | Johnny |
        /|  .-. |\|   5    |
       /_|__|_|_\ |--------|
         || ||     |SCANNING|
        (__)(__)   |........|
        ||  ||     |________|
     ___||__||___
    /   ||  ||   \
   |____||__||____|
    (__)    (__)
"""
    print(color_text(banner, "red"))

def banner_hack():
    banner = r"""
           ___
         [>_>]     ________
         \___/    | Johnny |
        /| -_- |\ |   5    |
       /_|_____|_\|--------|
         || ||     |ACCESS |
        (__)(__)   | GRANTED|
        ||  ||     |________|
     ___||__||___
    /   ||  ||   \
   |____||__||____|
    (__)    (__)
"""
    print(color_text(banner, "green"))

# def banner_name():
#     banner = r"""
#   ____            _ _______                  _             
#  |  _ \ ___  __ _| |_   _|__ _ __ _ __   ___| |_ ___  _ __ 
#  | |_) / _ \/ _` | | | |/ _ \ '__| '_ \ / _ \ __/ _ \| '__|
#  |  _ <  __/ (_| | | | |  __/ |  | | | |  __/ || (_) | |   
#  |_| \_\___|\__,_|_| |_|\___|_|  |_| |_|\___|\__\___/|_|   
# """
#     print(color_text(banner, "cyan"))
#     print(color_text("        [ Red Team Modular Toolkit 🕵️‍♂️ ]", "yellow"))

def banner_johnny5():
    banner = r"""
     _       _                       ____  
    | | ___ | |__  _ __  _ __  _   _| ___| 
 _  | |/ _ \| '_ \| '_ \| '_ \| | | |___ \ 
| |_| | (_) | | | | | | | | | | |_| |___) |
 \___/ \___/|_| |_|_| |_|_| |_|\__, |____/ 
                               |___/       

"""
