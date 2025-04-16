Each module will inherit from a base class and implement a run() method. Inputs will be passed via argparse or CLI command syntax like tool.py dns example.com.

Planned capabilities:
Module	        Purpose
osint	        Passive recon using public sources (e.g., WHOIS, social, GitHub)
dns_enum	    DNS resolution, zone transfer attempts, subdomain brute-forcing
host_discovery	Ping sweep, ARP scan for live hosts
port_scan	    TCP/UDP scans using sockets or Nmap
api_tester	    Swagger/OpenAPI brute force, fuzzing
dir_enum	    Web directory enumeration with wordlists





API Keys need to be in name:key format in console/api_keys.txt