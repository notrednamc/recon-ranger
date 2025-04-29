# ReconRanger — A Modular OSINT & Enumeration Toolkit

![ReconRanger Banner](https://via.placeholder.com/1000x200.png?text=ReconRanger+Toolkit)

**ReconRanger** is a modular Python toolkit designed for red teamers, penetration testers, and security researchers. It helps you gather OSINT and perform enumeration on target domains and networks quickly and flexibly.

---

## Features
- **Subdomain Enumeration**
  - crt.sh scraping
  - SecurityTrails API support
- **WHOIS Lookups**
- **Email Harvesting**
- **.local Hostname Resolution**
- **DNS Zone Transfers**
- **Nmap Port Scanning Integration**
- Easily extensible plugin-style architecture

## Planned Features
- Mass scanning of Class A,B,C,D ranges
- Other recon modules, internal or external
- Taking suggestions
---

## Installation
- Python Version 3.8+ recommended

1. Clone the repo:
```sh
git clone https://github.com/yourname/ReconRanger.git && cd ReconRanger
```

2. Install Dependencies: (venv Recommended)
```sh
python -m venv reconranger      ## Create venv
source reconranger/bin/activate ## Activate venv
# deactivate                    ## To stop venv
# rm -r venv                    ## To delete venv

pip install -r requirements.txt
```

3. Add you API keys (optional, e.g. Shodan) in config/api_keys.json or as environment variables via .env
- Supported key names are preloaded
- JSON format
---

## Adding Modules
```sh
To add your own:
Create a file in modules/sub_modules/ (e.g., my_enum.py)
Add your function (e.g., def my_enum(target):)
Import and map it in the OSINTModule loader
Done!
```
---

## Usage
- Command syntax
```sh
python3 main.py --module <module_Name> --target <IP/Domain> --options
python3 main.py --module host_discovery --target 192.168.1.10 --ports 22,80,443
```
---

### Example Output
```sh
### Subdomain Enumeration for google.com
- www.google.com
- mail.google.com

### WHOIS Lookup for google.com
- Registrar: MarkMonitor
- Creation Date: 1997-09-15

### Zone Transfer
- Zone transfer failed: Transfer failed: REFUSED
```
---

## API Key Support
- Some modules use APIs. Add your keys like so:
```sh
config/api_keys.json

{
  "securitytrails": "your_api_key"
}
```

- Or via .env:
```sh
SECURITYTRAILS=your_api_key
```
---

## Contributing
- PRs and feature requests are welcome! Open an issue or fork and go.

## Legal Disclaimer
- This tool is intended only for authorized testing and research. Do not use it against systems without permission. You are responsible for your own actions.

## Contact
- Built with ❤️ by Gnomes







```python
class MyTool:
    def __init__(self, target, options=None):
        self.target = target
        self.options = options or {}

    def run(self):
        # Your core logic here
        print(f"Running MyTool on {self.target}")
```