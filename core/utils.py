from pathlib import Path
import os
import importlib
from rich import print as rprint
import json

## Load the API Keys file in config/api_keys.txt
def load_api_keys(file_path='config/api_keys.txt'):
    api_keys = {}
    path = Path(file_path)
    if not path.is_file() or path.stat().st_size == 0:
        print(color_text(f"\n[ No API keys found in config/api_keys.txt ]", "red"))
        return api_keys  # Empty dict if none found
    
    with path.open("r") as f:
        api_keys = json.load(f)
    
    rprint(f"\n[bold yellow][ API Keys Loaded ][/bold yellow]")
    for key, value in api_keys.items():
        rprint(f"[bold green][ {key}:{value} ][/bold green]")

    return api_keys

## Load method to be used into calling class 'self'
def load_and_bind_methods(instance, methods_map):
    for method_name, module_path in methods_map.items():
        try:
            module_name, func_name = module_path.rsplit('.', 1)
            module = importlib.import_module(module_name)
            func = getattr(module, func_name)
            bound_func = func.__get__(instance)
            setattr(instance, method_name, bound_func)

            #  Register the method in the dictionary
            if hasattr(instance, "bind_method"):
                instance.bind_method(method_name, bound_func)
                
        except Exception as e:
            print(f"[!] Could not bind method `{method_name}` from `{module_path}`: {e}")

## In no word list is provided, use the default (simple wordlist for now)
## TODO: Integrate Seclists Subdomain Wordlist
def get_default_wordlist(filename="subdomains.txt"):
    base_dir = os.path.dirname(__file__)
    return os.path.join("data", "wordlists", filename)

## Custom colors
## Remove this infavor of rprint
def color_text(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "blue": "\033[94m",
        "yellow": "\033[93m",
        "cyan": "\033[96m",
        "reset": "\033[0m",
    }
    return f"{colors.get(color, '')}{text}{colors['reset']}"

# ## Debug logger, not currently in use
# def setup_logger():
#     logging.basicConfig(
#         filename="logs/debug.log",
#         level=logging.DEBUG,
#         format="%(asctime)s [%(levelname)s] %(message)s",
#     )