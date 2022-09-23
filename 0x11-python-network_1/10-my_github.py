#!/usr/bin/python3
"""the `10-my_github` module
takes GitHub credentials (username and password) and
uses the GitHub API to display the id
"""


if __name__ == "__main__":
    from sys import argv
    import requests
    from requests.auth import HTTPBasicAuth

    auth = HTTPBasicAuth(argv[1], argv[2])
    response = requests.get("https://api.github.com/user", auth=auth)
    print(response.json().get("id"))
