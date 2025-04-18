from core.utils import color_text
import subprocess

def check_dns_sec(self):
    print(color_text(f"\n### DNSSEC Check for {self.target}", "cyan"))
    try:
        output = subprocess.check_output(f"dig +dnssec {self.target}", shell=True)
        decoded = output.decode().lower()
        
        ## ad denotes the presense of dnssec
        if 'ad' in decoded:
            print(color_text(f"- DNSSEC is enabled for {self.target}", "green"))
        else:
            print(color_text(f"- DNSSEC not detected for {self.target}", "red"))
    except subprocess.CalledProcessError as e:
        print(color_text(f"- DNSSEC check failed: {e}", "red"))