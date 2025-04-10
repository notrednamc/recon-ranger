from core.base_module import RedTeamModule
import subprocess

class HostDiscoveryModule(RedTeamModule):
    def run(self):
        print(f"[+] Starting ping sweep on {self.target}")
        # If CIDR range: 192.168.1.0/24
        # for each IP:
        #     ping once, if reply, print host
