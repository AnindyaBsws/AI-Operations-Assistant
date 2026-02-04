import requests
import os

class GitHubTool:
    def search_repo(self, query: str):
        url = "https://api.github.com/search/repositories"
        headers = {"Authorization": f"token {os.getenv('GITHUB_TOKEN')}"}
        params = {"q": query, "sort": "stars", "order": "desc"}
        res = requests.get(url, headers=headers, params=params)
        return res.json()
