import requests
from core.utils import color_text

def query_crtsh(self):
    try:
        print(color_text(f"### Querying crt.sh...", "yellow"))
        # print("[*] Querying crt.sh...")
        url = f"https://crt.sh/?q=%25.{self.target}&output=json"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=10)

        if resp.status_code == 200:
            data = resp.json()
            for entry in data:
                name = entry.get("name_value", "")
                for sub in name.split("\n"):
                    if self.target in sub:
                        self.subdomains.add(sub.strip())
    except Exception as e:
        print(f"[!] crt.sh error: {e}")