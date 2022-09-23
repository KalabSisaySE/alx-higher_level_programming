#!/usr/bin/python3
"""the `5-hbtn_header` module
takes in a URL as an argument and
sends a request to the URL and
displays the value of the variable X-Request-Id in the response header
"""


if __name__ == "__main__":
    from sys import argv
    import requests
    url = argv[1]

    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))