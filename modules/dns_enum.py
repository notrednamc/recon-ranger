from core.base_module import RedTeamModule
from core.utils import color_text
import socket
import logging
import subprocess
from dns import resolver
from dns.exception import DNSException
import nmap
import termcolor
from termcolor import colored
import platform

class DNSModule(RedTeamModule):
    def run(self):
        # Prepare the markdown report
        # self.report_file = f"dns_report_{self.target}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        print(colored(f"# DNS Recon Report for `{self.target}`", "white", attrs=["bold"]))
        # self.log_report(f"# DNS Recon Report for `{self.target}`\n")
        self.zone_transfer()
        self.query_dns_records()
        self.subdomain_enum()
        self.reverse_dns_lookup()
        self.check_dnssec()
        self.dns_service_version()

        # print(color_text(f"\n[+] Report saved to {self.report_file}\n", "green"))

    def log_report(self, text):
        with open(self.report_file, "a") as file:
            file.write(text + "\n")

    def zone_transfer(self):
        # self.log_report("## Zone Transfer Attempt\n")
        print(color_text(f"## DNS Zone Transfer for {self.target}", "cyan"))

        if self.target.endswith(".local"):
            print(color_text(f"- 🔎 Resolving .local target: {self.target}", "yellow"))
            resolved_ip = self.resolve_local_hostname(self.target)
            if resolved_ip:
                print(color_text(f"- ✅ Resolved {self.target} to {resolved_ip}", "green"))
                target_ip = resolved_ip
        else:
            print(color_text(f"- ❌ Could not resolve {self.target}. Skipping AXFR.", "red"))
            return

        try:
            axfr_query = f"dig @{self.target} AXFR"
            output = subprocess.check_output(axfr_query, shell=True, stderr=subprocess.STDOUT)
            output_decoded = output.decode()
            print(color_text(f"### Zone Transfer Output: {output_decoded}", "green"))
            # self.log_report("```bash\n" + output_decoded + "\n```\n")
        except subprocess.CalledProcessError as e:
            output_decoded = e.output.decode()
            if "couldnt't get address" in output_decoded:
                msg = f"- Could not resolve target {self.target}: {output_decoded} {e}"
                print(color_text(f"❌ {msg}", "red"))
            else:
                msg = f"- Zone Transfer failed: {e}"
                # self.log_report(f"❌ {msg}\n")

    def query_dns_records(self):
        print(color_text(f"## DNS Record Enumeration", "cyan"))
        # self.log_report("## DNS Record Enumeration\n")
        record_types = ['A', 'MX', 'NS', 'TXT', 'CNAME', 'SOA']
        for record in record_types:
            try:
                print(color_text(f"### Querying {record} records for {self.target}", "cyan"))
                # self.log_report(f"### {record} Records")
                result = resolver.resolve(self.target, record)
                for ip in result:
                    msg = f"{record} record: {ip}"
                    print(color_text(f"- ✅ {msg}", "green"))
                    # self.log_report(f"- ✅ {msg}")
            except DNSException as e:
                msg = f"{record} record query failed: {e}"
                print(color_text(f"- ❌ {msg}", "red"))
                # self.log_report(f"- ❌ {msg}")

    def subdomain_enum(self):
        # self.log_report("## Subdomain Brute-Forcing\n")
        wordlist = self.options.get("wordlist")
        if not wordlist or not self._validate_file(wordlist):
            msg = "Wordlist not found or unreadable"
            print(color_text(f"❌ {msg}", "red"))
            # self.log_report(f"❌ {msg}")
            return

        print(color_text(f"## Brute-forcing subdomains using {wordlist}", "cyan"))
        print(color_text(f"- Wordlist: `{wordlist}`", "yellow"))
        # self.log_report(f"Using wordlist: `{wordlist}`\n")
        try:
            with open(wordlist, "r") as f:
                for line in f:
                    subdomain = line.strip()
                    fqdn = f"{subdomain}.{self.target}"
                    try:
                        ip = socket.gethostbyname(fqdn)
                        msg = f"Found: {fqdn} -> {ip}"
                        print(color_text(f"- ✅ {msg}", "green"))
                        # self.log_report(f"- ✅ {msg}")
                    except Exception:
                        print(color_text(f"- ❌ {fqdn}", "red"))
                        # self.log_report(f"- ❌ Failed: {fqdn}")
        except Exception as e:
            msg = f"Error reading wordlist: {e}"
            print(color_text(f"❌ {msg}", "red"))
            # self.log_report(f"❌ {msg}")

    def reverse_dns_lookup(self):
        print(color_text(f"## Performing Reverse DNS lookup for {self.target}", "cyan"))
        # self.log_report("## Reverse DNS Lookup\n")
        try:
            ip = socket.gethostbyname(self.target)
            reverse_dns = socket.gethostbyaddr(ip)
            msg = f"Reverse DNS lookup: {reverse_dns}"
            print(color_text(f"- ✅ {msg}", "green"))
            # self.log_report(f"- ✅ {msg}")
        except Exception as e:
            msg = f"Reverse DNS lookup failed: {e}"
            print(color_text(f"- ❌ {msg}", "red"))
            # self.log_report(f"- ❌ {msg}")

    def check_dnssec(self):
        print(color_text(f"## DNSSEC Check for: {self.target}", "cyan"))
        # self.log_report("## DNSSEC Check\n")
        try:
            result = subprocess.check_output(f"dig +dnssec {self.target}", shell=True)
            decoded = result.decode()
            if 'ad' in decoded.lower():
                msg = f"DNSSEC is enabled for {self.target}"
                print(color_text(f"- ✅ {msg}", "green"))
                # self.log_report(f"- ✅ {msg}")
            else:
                msg = f"DNSSEC is not enabled for {self.target}"
                print(color_text(f"- ❌ {msg}", "red"))
                # self.log_report(f"- ❌ {msg}")
        except subprocess.CalledProcessError as e:
            msg = f"DNSSEC check failed: {e}"
            print(color_text(f"- ❌ {msg}", "red"))
            # self.log_report(f"- ❌ {msg}")

    def dns_service_version(self):
        print(color_text(f"## DNS Service Version Detection for {self.target}", "cyan"))
        # self.log_report("## DNS Service Version Detection\n")
        nm = nmap.PortScanner()
        try:
            nm.scan(self.target, '53', '-sV')
            if 'hostnames' in nm[self.target]:
                for hostname in nm[self.target]['hostnames']:
                    msg = f"DNS Service Version: {hostname['name']}"
                    print(color_text(f"- ✅ {msg}", "green"))
                    # self.log_report(f"- ✅ {msg}")
            else:
                msg = "DNS service version detection failed"
                print(color_text(f"- ❌ {msg} for {self.target}", "red"))
                # self.log_report(f"- ❌ {msg}")
        except Exception as e:
            msg = f"DNS Service Version detection failed: {e}"
            print(color_text(f"- ❌ {msg}", "red"))
            # self.log_report(f"- ❌ {msg}")

    def _validate_file(self, path):
        try:
            with open(path, "r"):
                return True
        except:
            return False

    def resolve_local_hostname(self, hostname):
        """
        Attempts to resolve .local hostnames using avahi-resolve (Linux) or dns-sd (macOS).
        Returns the IP address as a string, or None if resolution fails.
        """
        try:
            if platform.system() == "Linux":
                cmd = ["avahi-resolve", "-n", hostname]
            elif platform.system() == "Darwin":
                # macOS
                cmd = ["dns-sd", "-G", "v4", hostname]
            else:
                print(color_text("[-] Unsupported OS for .local resolution", "red"))
                return None

            result = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode()
            
            if platform.system() == "Linux":
                if result:
                    return result.strip().split()[-1]
            elif platform.system() == "Darwin":
                # Output line should contain "Add 0 1 ... A.B.C.D"
                for line in result.splitlines():
                    if "Add" in line and "." in line:
                        return line.strip().split()[-1]
        except subprocess.CalledProcessError as e:
            print(color_text(f"- ❌ resolution failed: {e.output.decode()}", "red"), end="")
        return None