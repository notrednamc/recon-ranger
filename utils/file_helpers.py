import os

def get_default_wordlist(filename="subdomains.txt"):
    base_dir = os.path.dirname(__file__)
    return os.path.abspath(os.path.join(base_dir, "..", "data", "wordlists", filename))
