#!/bin/bash
# Description: Sends a JSON POST request to URL passed as first argument, displays the body of response.
curl -s -d "@$2" -H "Content-Type: application/json" -X POST "$1"
