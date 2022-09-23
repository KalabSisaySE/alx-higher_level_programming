#!/usr/bin/python3
"""the `2-post_email` module
takes in a URL and an email as an argument and
sends a POST request to the passed URL with the email as a parameter and
displays the body of the response
"""


if __name__ == "__main__":
    from sys import argv
    from urllib import request, parse

    data = parse.urlencode({"email": argv[2]}).encode("utf-8")

    req = request.Request(argv[1], data=data)
    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
