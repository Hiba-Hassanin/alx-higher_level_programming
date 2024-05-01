#!/bin/bash
# Description: Takes in a URL, sends a GET request to the URL, displays if status code is 200.
curl -s -L -X GET "$1" -o /tmp/body && cat /tmp/body