#!/bin/bash
# sends a GET request to the given url and X-School-User-Id must be sent with the value 98
curl -s -X GET -H "X-School-User-Id: 98" "$1"
