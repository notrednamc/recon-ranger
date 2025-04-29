# 🛡️ Red Team Recon: External Phase Notes

## 1. Subdomain Enumeration
**Goal**: Discover as many subdomains as possible to expand the attack surface.

**Tools & Usage**:
- `crt.sh` – Certificate transparency logs.
- `SecurityTrails` – Passive enumeration via API.
- `Subfinder` – Fast passive subdomain discovery.
- `Amass` – Active and passive recon.
- `Assetfinder` – Simple, fast subdomain discovery.
- `dnsx` – DNS probing of discovered domains.

---

## 2. WHOIS & Domain Info
**Goal**: Understand ownership and registration details.

**Tools & Usage**:
- `whois` – Domain info via CLI.
- `pywhois` – Programmatic lookups in Python.
- `SecurityTrails` – Historical WHOIS and DNS records.
- `ViewDNS` – Web-based recon suite.

---

## 3. Email Harvesting
**Goal**: Collect addresses for phishing or password spraying.

**Tools & Usage**:
- `theHarvester` – Pull emails from search engines and public sources.
- `Hunter.io` – Find company-associated emails.
- `LinkedIn Dorking` – Manual or automated searches.
- `emailrep.io` – Analyze email exposure and risk.

---

## 4. Employee Enumeration
**Goal**: Identify staff and naming conventions.

**Tools & Usage**:
- `LinkedInt` – Employee enumeration from LinkedIn.
- `GitHub recon` – Find devs and internal code.
- `sherlock` – Track usernames across platforms.
- `Google Dorks` – Search for name/email patterns.
- `Recon-ng` – Framework with LinkedIn & GitHub modules.

---

## 5. Infrastructure Mapping
**Goal**: Identify exposed services and tech stacks.

**Tools & Usage**:
- `nmap` – Port scan, service discovery (`-sV -sC`).
- `rustscan` – Fast scanning with `nmap` integration.
- `naabu` – Quick port discovery.
- `httpx` – Probe HTTP(S) endpoints.
- `whatweb` / `wappalyzer` – Web tech fingerprinting.
- `Shodan` – External device/service exposure.

---

## 6. Certificate Transparency Analysis
**Goal**: Find hidden/internal subdomains.

**Tools & Usage**:
- `crt.sh` – Cert transparency search.
- `Censys` – Certs and connected infrastructure.
- `cero` (by ProjectDiscovery) – Subdomains via CT logs.
- `Shodan` – Cert and host intel.

---

## 7. OSINT & Public Exposure
**Goal**: Locate leaked credentials, metadata, and public infrastructure.

**Tools & Usage**:
- `GitHub Dorks` – Find sensitive info in repos.
- `TruffleHog` – Secret key and token scanner.
- `Google Dorking` – Locate public-facing vulnerabilities or files.
- `ExifTool` – Pull metadata from files/images.
- `HaveIBeenPwned` –  Breach exposure check.

---

## 8. Passive vs Active Enumeration

### Passive
- `Amass` (passive mode)
- `crt.sh`
- `SecurityTrails`
- `archive.org` (Wayback Machine)
- `Censys`, `Shodan`
- `dnsx`

### Active
- `nmap`, `naabu`, `httpx`
- `dig`, `nslookup`
- `dnsrecon`, `dnscan`
- Manual probing of services and headers

---

*This list is a living doc — add tools or techniques as your workflow evolves.*

