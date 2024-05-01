#!/bin/bash
# Description: Takes in a URL, sends a GET request to the URL, displays if status code is 200.
curl -sX GET $1 -L