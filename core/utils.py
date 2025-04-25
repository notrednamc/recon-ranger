from pathlib import Path
import os
import importlib
from rich import print as rprint
import json

## Load the project path
BASE_PATH = Path(__file__).resolve().parents[1]

## Validate API Key has a value
def require_key(value, key_name):
    if not value:
        raise ValueError(f"Missing API key: {key_name}")

# ## Load the API Keys file in config/api_keys.txt
# def load_api_keys(file_path='config/api_keys.txt'):
#     api_keys = {}
#     full_path = BASE_PATH / file_path

#     if not full_path.is_file() or full_path.stat().st_size == 0:
#         rprint(f"\n[red][ No API keys found in /{full_path} ][/red]")
#         return api_keys  # Empty dict if none found
    
#     with full_path.open("r") as f:
#         api_keys = json.load(f)
    
#     rprint(f"\n[bold yellow][ API Keys Loaded ][/bold yellow]")
#     for key, value in api_keys.items():
#         rprint(f"[bold green][ {key}:{value} ][/bold green]")

#     return api_keys

## Load method to be used into calling class 'self'
def load_and_bind_methods(self, method_map):
    for name, import_path in method_map.items():
        try:
            # Split the import path into module, class name
            module_path, class_name = import_path.rsplit('.', 1)
            
            # Dynamically import the module
            module = importlib.import_module(module_path)
            
            # Get the class from the module
            klass = getattr(module, class_name)
            
            # Check if the class is callable (i.e., a class)
            if not callable(klass):
                raise TypeError(f"{class_name} is not callable (likely not a class)")
            
            # Create an instance of the class
            instance = klass(self.target, options=self.options)

            # Dynamically get the method, assuming it’s a `run` method
            if hasattr(instance, 'run'):
                method = getattr(instance, 'run')
                self.methods[name] = method
            else:
                raise AttributeError(f"{class_name} does not have a 'run' method")
        except Exception as e:
            print(f"[!] Could not bind method `{name}` from `{import_path}`: {e}")

## If no word list is provided, use the default (simple wordlist for now)
## TODO: Integrate Seclists Subdomain Wordlist
def get_default_wordlist(filename="subdomains.txt"):
    base_dir = os.path.dirname(__file__)
    return os.path.join("data", "wordlists", filename)

# ## Debug logger, not currently in use
# def setup_logger():
#     logging.basicConfig(
#         filename="logs/debug.log",
#         level=logging.DEBUG,
#         format="%(asctime)s [%(levelname)s] %(message)s",
#     )