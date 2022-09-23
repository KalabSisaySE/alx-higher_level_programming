#!/usr/bin/python3
"""the `7-error_code` module
sends a request to the given URL and
displays the body of the response
"""


if __name__ == "__main__":
    from urllib import response
    from sys import argv
    import requests
    url = argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)