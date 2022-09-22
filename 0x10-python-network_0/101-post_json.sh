#!/bin/bash
# sends a JSON POST request to the given url
curl -s -X POST "Content-Type: application/json" -d @"$2" "$1"