#!/bin/bash
# Sends a GET request and displays body only if status code is 200
curl -sL -w "%{http_code}" "$1" -o temp_body && [ "$(tail -c 3 temp_body)" = "200" ] && head -c -3 temp_body && echo "" || rm -f temp_body

