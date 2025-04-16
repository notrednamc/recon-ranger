import subprocess
from core.utils import color_text

def dns_zone_transfer(self):
    print(color_text(f"\n### DNS Zone Transfer for {self.target}", "cyan"))

    if self.target.endswith(".local"):
        print(color_text(f"- 🔎 Attempting to resolve .local hostname: {self.target}", "yellow"))
        resolved_ip = self.resolve_local_hostname(self.target)
        if not resolved_ip:
            print(color_text("- ❌ Could not resolve hostname. Skipping AXFR.", "red"))
            return
        print(color_text(f"- ✅ Resolved {self.target} to {resolved_ip}", "green"))

    try:
        output = subprocess.check_output(f"dig @{self.target} AXFR", shell=True, stderr=subprocess.STDOUT)
        print(color_text("\n#### Zone Transfer Output:\n" + output.decode(), "green"))
    except subprocess.CalledProcessError as e:
        print(color_text(f"- ❌ Zone transfer failed: {e.output.decode().strip()}", "red"))