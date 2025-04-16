from core.utils import color_text
import requests

def query_hackertarget(self):
    try:
        print(color_text(f"### Querying HackerTarget", "yellow"))
        print("[*] Querying HackerTarget...")
        url = f"https://api.hackertarget.com/hostsearch/?q={self.target}"
        resp = requests.get(url, timeout=10)

        if "error" not in resp.text.lower():
            for line in resp.text.splitlines():
                sub = line.split(",")[0]
                if self.target in sub:
                    self.subdomains.add(sub.strip())
    except Exception as e:
        print(f"[!] HackerTarget error: {e}")
