import re
import requests
from core.base_module import RedTeamModule
from modules.dns_enum import DNSModule

class OSINTModule(RedTeamModule):
    def __init__(self, target, options=None, api_keys=None):
        super().__init__(target, options)
        self.api_keys = api_keys or {}
        self.results = {}

    def log_markdown(self, message, level="info"):
        icons = {
            "info": "ℹ️",
            "success": "✅",
            "fail": "❌",
            "warn": "⚠️",
            "action": "🔍",
        }
        print(f"- {icons.get(level, '')} {message}")

    def run(self):
        print(f"\n## 🔎 OSINT Module: `{self.target}`\n")
        self.email_enum()
        self.github_enum()
        self.linkedin_placeholder()
        self.dns_enum()

    def email_enum(self):
        self.log_markdown("Looking for email addresses", "action")
        emails = set()

        # Regex from website
        try:
            r = requests.get(f"http://{self.target}", timeout=5)
            found = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", r.text)
            emails.update(found)
        except Exception as e:
            self.log_markdown(f"Regex scan failed: {e}", "fail")

        # Hunter.io API
        hunter_key = self.api_keys.get("hunter")
        if hunter_key:
            self.log_markdown("Using Hunter.io API (placeholder)", "info")
            # Placeholder for real API call
            # response = requests.get(...)
            self.log_markdown("Hunter.io API lookup not implemented yet", "warn")
        else:
            self.log_markdown("Hunter.io API key not set. Skipping API lookup.", "warn")

        if emails:
            for email in emails:
                self.log_markdown(f"Email found: `{email}`", "success")
            self.results["emails"] = list(emails)
        else:
            self.log_markdown("No emails found", "fail")

    def github_enum(self):
        self.log_markdown("Searching GitHub for users related to target", "action")
        github_users = []

        headers = {"Accept": "application/vnd.github.v3+json"}
        github_key = self.api_keys.get("github")
        if github_key:
            headers["Authorization"] = f"token {github_key}"

        try:
            url = f"https://api.github.com/search/users?q={self.target}"
            r = requests.get(url, headers=headers, timeout=5)
            if r.status_code == 200:
                data = r.json()
                for user in data.get("items", [])[:5]:
                    login = user.get("login")
                    profile = user.get("html_url")
                    self.log_markdown(f"GitHub: [{login}]({profile})", "success")
                    github_users.append(profile)
                self.results["github_profiles"] = github_users
            else:
                self.log_markdown(f"GitHub API returned status {r.status_code}", "fail")
        except Exception as e:
            self.log_markdown(f"GitHub search failed: {e}", "fail")

    def linkedin_placeholder(self):
        self.log_markdown("LinkedIn search placeholder (not yet implemented)", "warn")
        # Eventually implement Bing/Google scraping or API-assisted search
        self.results["linkedin"] = []

    def dns_enum(self):
        self.log_markdown("Running DNS enumeration module", "action")
        try:
            dns_module = DNSModule(self.target)
            dns_module.run()
            self.results["dns"] = dns_module.results
        except Exception as e:
            self.log_markdown(f"DNS module failed: {e}", "fail")
