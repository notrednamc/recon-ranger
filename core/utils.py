import logging

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