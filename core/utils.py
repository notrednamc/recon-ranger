import logging
from pathlib import Path

## Load the API Keys file in config/api_keys.txt
def load_api_keys(file_path='config/api_keys.txt'):
    api_keys = {}

    path = Path(file_path)
    if not path.is_file() or path.stat().st_size == 0:
        print(color_text(f"\n[ No API keys found in config/api_keys.txt ]", "red"))
        return api_keys  # Empty dict if none found

    with path.open("r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue  # Skip blank lines and comments
            if ":" in line:
                label, key = line.split(":", 1)
                api_keys[label.strip()] = key.strip()
            else:
                print(f"[!] Skipping malformed line: {line}")
    # print(api_keys)
    return api_keys

def setup_logger():
    logging.basicConfig(
        filename="logs/debug.log",
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

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

