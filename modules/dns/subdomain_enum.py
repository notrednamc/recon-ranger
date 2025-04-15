
from utils.file_helpers import get_default_wordlist
from core.utils import color_text

def subdomain_enum(self):
    wordlist = self.options.get("wordlist") or get_default_wordlist()

    if not self._validate_file(wordlist):
        msg = f"Wordlist not found or unreadable: {wordlist}"
        print(color_text(f"❌ {msg}", "red"))
        return

    print(color_text(f"#### Brute-forcing subdomains using {wordlist}", "cyan"))
    print(color_text(f"- Wordlist: `{wordlist}`", "yellow"))
    
    try:
        with open(wordlist, "r") as f:
            for line in f:
                subdomain = line.strip()
                fqdn = f"{subdomain}.{self.target}"
                try:
                    ip = socket.gethostbyname(fqdn)
                    msg = f"Found: {fqdn} -> {ip}"
                    print(color_text(f"- ✅ {msg}", "green"))
                except Exception:
                    print(color_text(f"- ❌ {fqdn}", "red"))
    except Exception as e:
        msg = f"Error reading wordlist: {e}"
        print(color_text(f"❌ {msg}", "red"))