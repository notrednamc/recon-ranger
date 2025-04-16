from core.utils import color_text
import nmap

def dns_service_version(self):
    print(color_text("\n### DNS Service Version Detection", "cyan"))
    nm = nmap.PortScanner()
    try:
        nm.scan(self.target, '53', '-sV')
        if self.target in nm.all_hosts():
            services = nm[self.target].get('tcp', {}).get(53, {})
            if 'product' in services:
                print(color_text(f"- ✅ DNS Service: {services['product']} {services.get('version', '')}", "green"))
            else:
                print(color_text("- ❌ No service info detected on port 53", "red"))
        else:
            print(color_text("- ❌ Target not found in Nmap results", "red"))
    except Exception as e:
        print(color_text(f"- ❌ Nmap scan failed: {e}", "red"))