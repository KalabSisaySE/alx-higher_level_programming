#!/usr/bin/python3
"""the `0-htbn_status` module
fetches a url and displays the bodu of response"""

if __name__ == "__main__":
    from urllib import request

    with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf-8")))
