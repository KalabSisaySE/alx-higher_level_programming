#!/usr/bin/python3
"""the `8-json_api` module
takes in a letter and sends a POST request to
`http://0.0.0.0:5000/search_user` with the letter as a parameter
"""


if __name__ == "__main__":
    from sys import argv
    import requests

    if len(argv) == 1:
        letter = ""
    else:
        letter = argv[1]
    payload = {"q": letter}

    res = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = res.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")