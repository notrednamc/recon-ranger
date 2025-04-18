from core.utils import color_text
import socket

def reverse_dns_lookup(self):
    print(color_text("\n### Performing Reverse DNS Lookup", "cyan"))
    try:
        ip = socket.gethostbyname(self.target)
        hostname, _, _ = socket.gethostbyaddr(ip)
        print(color_text(f"- {ip} resolves to {hostname}", "green"))
    except Exception as e:
        print(color_text(f"- Reverse lookup failed: {e}", "red"))