#!/bin/bash
# sends a JSON POST request to the given url
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
