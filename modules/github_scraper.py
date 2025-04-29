import requests
import time
from config import api_keys
from core.utils import require_key
from rich import print as rprint

class GitHubDorker:
    def __init__(self, target, options=None):
        super().__init__(target, options or {})
        if self.options:
            rprint(f"[yellow]- Options passed are not needed for this module.")
        self.token = require_key(api_keys.GITHUBTOKEN, "GITHUBTOKEN")
        # self.web_report_url = web_report_url
        self.headers = {"Authorization": f"token {self.token}"}
        self.dorks = [
            "filename:.env",
            "AWS_SECRET_ACCESS_KEY",
            "filename:config api_key",
            "extension:json api_key",
            "password filename:settings.py"
        ]

        ## Set error message
        if not self.token:
            raise ValueError(rprint(f"[bold red]- GitHub token is missing. Set GITHUBTOKEN in config/api_keys.py[/bold red]"))
        
    def search_github(self, query):
        url = f"https://api.github.com/search/code?q={query}"
        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                return response.json().get("items", [])
            else:
                rprint(f"[red]- GitHub API Error {response.status_code}: {response.text}[/red]")
                return []
        except Exception as e:
            rprint(f"[red]- Request failed: {e}[/red]")
            return []

    # def report_finding(self, tool, query, result):
    #     payload = {
    #         "tool": tool,
    #         "query": query,
    #         "result": {
    #             "name": result.get("name"),
    #             "path": result.get("path"),
    #             "html_url": result.get("html_url"),
    #             "repo": result.get("repository", {}).get("full_name")
    #         },
    #         "timestamp": time.time()
    #     }
    #     if self.web_report_url:
    #         try:
    #             requests.post(self.web_report_url, json=payload)
    #         except Exception as e:
    #             print(f"[!] Failed to report to web backend: {e}")
    #     else:
    #         print("[*] Reporting URL not set. Here's the payload:")
    #         print(payload)

    def run(self):
        for dork in self.dorks:
            rprint(f"[yellow]- Searching: {dork}[/yellow]")
            results = self.search_github(dork)
            for res in results:
                rprint(f"[green]-    Found: {res['html_url']}[/green]")
                self.report_finding("github_dorker", dork, res)
            time.sleep(2)  # Respect rate limit
