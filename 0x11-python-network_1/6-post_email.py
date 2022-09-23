#!/usr/bin/python3
"""the `6-post_email` module
takes in a URL and an email address as an argument and
sends a POST request to the passed URL with the email as a parameter and
displays the body of the response
"""

if __name__ == "__main__":
    from sys import argv
    from requests

    payload = {'email': argv[2]}
    r = requests.post(argv[1], data=payload)
    print(r.text)
