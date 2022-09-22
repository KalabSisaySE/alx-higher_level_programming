#!/bin/bash
# sends a request to the given url and displays only the status code of the response
curl -so /dev/null --write-out "%{http_code}" "$1"