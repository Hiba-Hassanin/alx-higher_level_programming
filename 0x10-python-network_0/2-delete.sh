#!/bin/bash
# Description: Sends a delete request to the URL as first argument, displays body of the response.
curl -sX DELETE "$1"
