#!/usr/bin/python3
"""the `3-error_code` module
takes in a URL as an argument and
sends a request to the URL and
displays the body of the response (decoded in utf-8)
"""


if __name__ == "__main__":
    from sys import argv
    from urllib import request, error

    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode("UTF-8"))
    except error.HTTPError as e:
        print("Error code:", e.code)
