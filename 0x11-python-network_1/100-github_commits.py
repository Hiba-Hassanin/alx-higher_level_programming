#!/usr/bin/python3
"""
Script to list 10 most recent commits of
a repository on GitHub
"""

import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = requests.get(url)
    commits = response.json()

    if response.status_code != 200:
        print(f"Error: {commits['message']}")
        sys.exit(1)

    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
