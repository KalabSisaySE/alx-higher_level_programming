#!/usr/bin/python3
""" the `100-github_commits` module
lists 10 commits (from the most recent to oldest)
"""


if __name__ == "__main__":
    from sys import argv
    import requests

    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])

    response = requests.get(url)
    commits = response.json()
    try:
        for i in range(10):
            sha = commits[i].get("sha")
            author_name = commits[i].get("commit").get("author").get("name")
            print("{}: {}".format(sha, author_name))

    except IndexError:
        pass