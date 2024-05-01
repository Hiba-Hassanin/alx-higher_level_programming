#!/bin/bash
# Description: Takes in a URL, sends POST request to URL with specified parameters, displays body of response.
curl -sX POST "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
