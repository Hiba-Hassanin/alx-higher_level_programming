#!/bin/bash
# Description: Takes URL as argument, sends a GET request to URL with custom header,displays body of response.
curl -s -H "X-School-User-Id: 98" "$1"
