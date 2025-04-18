import subprocess
from core.utils import color_text
from modules.sub_modules.resolve_local_hostname import resolve_local_hostname

def dns_zone_transfer(self):
    print(color_text(f"\n### DNS Zone Transfer for {self.target}", "cyan"))
    try:
        ## Resolvethe hostname to IP for dig command
        resolved_ip = resolve_local_hostname(self)
        if not resolved_ip:
            print(color_text("- Could not resolve hostname. Skipping AXFR.", "red"))
            return
        else:
            print(color_text(f"- Attempting to resolve hostname: {self.target}", "yellow"))
            print(color_text(f"- Resolved {self.target} to {resolved_ip}", "green"))

        ## Dig command
        output = subprocess.check_output(
            f"dig @{resolved_ip} AXFR", shell=True, stderr=subprocess.STDOUT
        ).decode().strip()

        if not output:
            print(color_text("- Zone transfer completed but returned no results.", "yellow"))
        elif "Transfer failed" in output or "connection timed out" in output.lower():
            print(color_text(f"- Zone transfer failed:\n{output}", "red"))
        else:
            print(color_text("\n#### Zone Transfer Output\n" + output, "green"))
    except subprocess.CalledProcessError as e:
        print(color_text(f"- Zone transfer failed: {e.output.decode().strip()}", "red"))
