#!/usr/bin/python3
""" the `1-hbtn_header` module
sends a request to the given URL and
displays the value of the X-Request-Id"""


if __name__ == "__main__":
    from sys import argv
    from urllib import request

    req = request.Request(argv[1])
    with request.urlopen(req) as response:
        print(response.headers.get("X-Request-Id"))
