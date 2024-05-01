#!/bin/bash
# Description: Send a PUT request to 0.0.0.0:5000/catch_me with a specific header.
curl -s -L -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
