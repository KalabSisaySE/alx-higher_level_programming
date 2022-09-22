#!/bin/bash
# sends a POST request to the given url and email must be sent with the value test@gmail.com subject must be sent with the value I will always be here for PLD
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
