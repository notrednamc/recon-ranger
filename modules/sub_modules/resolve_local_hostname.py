import platform
from core.utils import color_text
import subprocess

def resolve_local_hostname(self, hostname):
    print(color_text("\n### Resolving .local hostname", "cyan"))
    try:
        if platform.system() == "Linux":
            cmd = ["avahi-resolve", "-n", hostname]
        elif platform.system() == "Darwin":
            cmd = ["dns-sd", "-G", "v4", hostname]
        else:
            print(color_text("- ❌ Unsupported OS for .local resolution", "red"))
            return None

        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode()

        if platform.system() == "Linux" and result:
            return result.strip().split()[-1]
        elif platform.system() == "Darwin":
            for line in result.splitlines():
                if "Add" in line and "." in line:
                    return line.strip().split()[-1]
    except subprocess.CalledProcessError as e:
        print(color_text(f"- ❌ Hostname resolution failed: {e.output.decode()}", "red"))
    return None