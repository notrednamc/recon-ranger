
from core.utils import get_default_wordlist
from core.utils import color_text
import socket

def subdomain_enum(self):
    ## Load provided wordlist, or get the default
    wordlist = self.options.get("wordlist") or get_default_wordlist()

    ## Validate the file
    if not self._validate_file(wordlist):
        msg = f"Wordlist not found or unreadable: {wordlist}"
        print(color_text(f"{msg}", "red"))
        return

    print(color_text(f"\n#### Brute-forcing subdomains using {wordlist}", "cyan"))
    print(color_text(f"- Wordlist: `{wordlist}`", "yellow"))
    
    try:
        with open(wordlist, "r") as file:
            for line in file:
                subdomain = line.strip()
                fqdn = f"{subdomain}.{self.target}"
                try:
                    ip = socket.gethostbyname(fqdn)
                    msg = f"Found: {fqdn} -> {ip}"
                    print(color_text(f"- {msg}", "green"))
                except Exception:
                    print(color_text(f"- {fqdn}", "red"))
    except Exception as e:
        msg = f"Error reading wordlist: {e}"
        print(color_text(f"{msg}", "red"))